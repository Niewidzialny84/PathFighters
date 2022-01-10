using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;

public class unitScript : NetworkBehaviour
{
    public int belongsToPlayer;
    private int moveDirection;
    private float rayDistance; // The gap between friendly units

    public float speed;
    private float rayOffset; // There needs to be a offset so the ray doesn't collide with origin
    public float reach;
    public float meleeReach; // This will control if ranged units are shooting or fighting in melee which will decrease their damage. !!!THIS IS 0 FOR ALL MELEE UNITS AS THEY USE JUST REACH!!!
    public float attackDelay; // This describes how long the delay between attacks is
    private float actualAttackDelay; // This is used to show how much of the delay is left.

    public GameObject projectile;

    public int armor;
    public int damage;
    public int hitPoints;

    public float cost;

    [SerializeField] private Animator animator;
    [SerializeField] private AudioSource deathS, attackS;

    //State machine enumerator
    enum State
    {
        Moving, //Idle and moving will have similar animations
        Fighting,
        Dying
    }
    State state;

    // This is called when unit moves over the half distance to the enemy base
    void EndDefenderFury()
    {
        this.damage -= 1;
        //If right upgrades are developed this will boost the unit
        GameObject gameHandler = GameObject.FindGameObjectWithTag("GameController");
        if (gameHandler.GetComponent<gameHandlerScript>().upgrades[this.belongsToPlayer - 1, 5])
        {
            if (this.reach < 1.1)
            {
                this.damage += 3;
            }
            else
            {
                this.damage += 1;
            }
            this.speed = this.speed * 1.2f;
        }
    }
    private bool defender;

    // This is called when the unit moves
    void Advance(float moveSpeed)
    {
        if (!Physics2D.Raycast(new Vector2(this.transform.position.x - ((GetComponent<CircleCollider2D>().radius + rayOffset) * this.moveDirection), this.transform.position.y), new Vector2((-1f * this.moveDirection), 0f), rayDistance, (LayerMask.GetMask("Unit") | LayerMask.GetMask("Gate"))))
        {
            this.transform.position += new Vector3((-moveSpeed * this.moveDirection) * Time.deltaTime, 0, 0);
        }
    }

    // Start is called before the first frame update
    void Start()
    {
        if(!isServer)
        {
            rayDistance = 0.05f;
            rayOffset = 0.01f;

            this.state = State.Moving;

            if (belongsToPlayer == 1)
            {
                moveDirection = -1;
            }
            else
            {
                moveDirection = 1;
                this.transform.localScale = new Vector3(-1f, 1f, 0f);
            }
            actualAttackDelay = 0f;

            this.defender = true;

            //Here will be some bonuses due to upgrades
            GameObject gameHandler = GameObject.FindGameObjectWithTag("GameController");
            if (gameHandler.GetComponent<gameHandlerScript>().upgrades[this.belongsToPlayer - 1, 3] && this.speed == 0.5f)
            {
                this.speed += 0.1f;
                this.reach = this.reach * 1.4f;
                this.cost -= 5;
            }
        }
    }


    // Update is called once per frame
    void Update()
    {
        // Check if unit is defending or attacking
        if (this.belongsToPlayer == 1 && this.transform.position.x > 0 && this.defender)
        {
            EndDefenderFury();
            this.defender = false;
        }
        else if (this.belongsToPlayer == 2 && this.transform.position.x < 0 && this.defender)
        {
            EndDefenderFury();
            this.defender = false;
        }

        //Reduce the actual attack delay to allow the unit to be ready to attack.
        if (this.actualAttackDelay > 0f)
        {
            this.actualAttackDelay -= Time.deltaTime;
        }

        if (this.state == State.Moving)
        {
            // Check if not entering combat
            bool enemyInReach = false;
            RaycastHit2D[] inReach = Physics2D.RaycastAll(new Vector2(this.transform.position.x - ((GetComponent<CircleCollider2D>().radius + rayOffset) * moveDirection), this.transform.position.y), new Vector2((-1f * moveDirection), 0f), reach, (LayerMask.GetMask("Unit") | LayerMask.GetMask("Gate")));
            for (int i = 0; i < inReach.Length; i++)
            {
                if (inReach[i].collider.gameObject.layer == 7 && inReach[i].collider.gameObject.GetComponent<unitScript>().belongsToPlayer != this.belongsToPlayer)
                {
                    enemyInReach = true;
                    break;
                }
                else if (inReach[i].collider.gameObject.layer == 9 && inReach[i].collider.gameObject.GetComponent<gateScript>().belongsToPlayer != this.belongsToPlayer)
                {
                    enemyInReach = true;
                    break;
                }
            }
            if (enemyInReach)
            {
                this.state = State.Fighting;
                actualAttackDelay = attackDelay;
            }
            // Move the unit
            Advance(this.speed);
        }
        //This is the combat section!
        else if (this.state == State.Fighting)
        {
            // Actual attack
            if (this.actualAttackDelay <= 0f)
            {
                attackS.Play();
                RaycastHit2D[] inReach = Physics2D.RaycastAll(new Vector2(this.transform.position.x - ((GetComponent<CircleCollider2D>().radius + rayOffset) * moveDirection), this.transform.position.y), new Vector2((-1f * moveDirection), 0f), reach, (LayerMask.GetMask("Unit") | LayerMask.GetMask("Gate")));
                for (int i = 0; i < inReach.Length; i++)
                {
                    var enemy = inReach[i].collider.gameObject;
                    if (enemy.layer == 7 && enemy.GetComponent<unitScript>().belongsToPlayer != this.belongsToPlayer)
                    {
                        if (Mathf.Abs(this.transform.position.x - enemy.transform.position.x) <= this.meleeReach + GetComponent<CircleCollider2D>().radius + enemy.GetComponent<CircleCollider2D>().radius)
                        {
                            enemy.GetComponent<unitScript>().hitPoints -= Mathf.Max(1, ((int)(this.damage/2) - enemy.GetComponent<unitScript>().armor));
                        }
                        else if(this.projectile != null)
                        {
                            var tempProjectile = Instantiate(projectile, this.transform.position, Quaternion.identity);
                            tempProjectile.GetComponent<projectileScript>().setTarget(enemy);
                            tempProjectile.GetComponent<projectileScript>().setDamage(damage);
                        }
                        else
                        {
                            enemy.GetComponent<unitScript>().hitPoints -= Mathf.Max(1, (this.damage - enemy.GetComponent<unitScript>().armor));
                        }
                        break;
                    }
                    else if (enemy.layer == 9 && enemy.GetComponent<gateScript>().belongsToPlayer != this.belongsToPlayer)
                    {
                        if (Mathf.Abs(this.transform.position.x - enemy.transform.position.x) <= this.meleeReach + GetComponent<CircleCollider2D>().radius/* + enemy.GetComponent<BoxCollider2D>().size.x*/)
                        {
                            enemy.GetComponent<gateScript>().receiveDamage((int)this.damage / 2);
                        }
                        else if (this.projectile != null)
                        {
                            var tempProjectile = Instantiate(projectile, this.transform.position, Quaternion.identity);
                            tempProjectile.GetComponent<projectileScript>().setTarget(enemy);
                            tempProjectile.GetComponent<projectileScript>().setDamage(damage);
                        }
                        else
                        {
                            enemy.GetComponent<gateScript>().receiveDamage(this.damage);
                        }
                        break;
                    }
                }
                this.state = State.Moving;
            }
            // Move slowly while in combat
            Advance(this.speed * 0.33f);
        }
        
        //Soldier dies and is destroyed. TODO: Combat; TODO: Animation?; TODO: Blood?
        if (this.hitPoints <= 0 && this.state != State.Dying)
        {
            deathS.Play();

            this.state = State.Dying;
            var gameHandler = GameObject.Find("gameHandler");
            if (this.belongsToPlayer != gameHandler.GetComponent<gameHandlerScript>().activePlayer) {
                if (gameHandler.GetComponent<gameHandlerScript>().upgrades[gameHandler.GetComponent<gameHandlerScript>().activePlayer - 1, 11]) { gameHandler.GetComponent<gameHandlerScript>().gold += cost * 0.5f; }
                else { gameHandler.GetComponent<gameHandlerScript>().gold += cost * 0.3f; }
            }
            Destroy(gameObject, 0.5f);
        }

        try
        {
            if (this.state == State.Fighting)
            {
                animator.SetBool("fighting", true);
            }
            else
            {
                animator.SetBool("fighting", false);
            }
        }
        catch (Exception e)
        {
        }
    }
}
