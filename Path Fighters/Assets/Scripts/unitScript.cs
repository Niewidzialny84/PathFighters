using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class unitScript : MonoBehaviour
{
    public int belongsToPlayer;
    private int moveDirection;
    private float rayDistance; // The gap between friendly units

    public float speed;
    private float rayOffset; // There needs to be a offset so the ray doesn't collide with origin
    public float reach;
    public float attackDelay; // This describes how long the delay between attacks is
    private float actualAttackDelay; // This is used to show how much of the delay is left.
    public int armor;
    public int damage;
    public int hitPoints;

    public float cost;

    //State machine enumerator
    enum State
    {
        Moving, //Idle and moving will have similar animations
        Fighting,
        Dying
    }
    State state;

    // Start is called before the first frame update
    void Start()
    {
        rayDistance = 0.03f;
        rayOffset = 0.01f;

        this.state = State.Moving;

        if(belongsToPlayer == 1)
        {
            moveDirection = -1;
        }
        else
        {
            moveDirection = 1;
        }
        actualAttackDelay = attackDelay;
    }

    // Update is called once per frame
    void Update()
    {
        //Reduce the actual attack delay to allow the unit to be ready to attack.
        if (this.actualAttackDelay > 0f)
        {
            this.actualAttackDelay -= Time.deltaTime;
        }

        if (this.state == State.Moving)
        {
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
            }
            else if (!Physics2D.Raycast(new Vector2(this.transform.position.x - ((GetComponent<CircleCollider2D>().radius + rayOffset) * moveDirection), this.transform.position.y), new Vector2((-1f * moveDirection), 0f), rayDistance, (LayerMask.GetMask("Unit") | LayerMask.GetMask("Gate"))))
            {
                this.transform.position += new Vector3((-this.speed * moveDirection) * Time.deltaTime, 0, 0);
            }
        }
        //This is the combat section!
        else if (this.state == State.Fighting && this.actualAttackDelay <= 0f)
        {
            RaycastHit2D[] inReach = Physics2D.RaycastAll(new Vector2(this.transform.position.x - ((GetComponent<CircleCollider2D>().radius + rayOffset) * moveDirection), this.transform.position.y), new Vector2((-1f * moveDirection), 0f), reach, (LayerMask.GetMask("Unit") | LayerMask.GetMask("Gate")));
            for (int i = 0; i < inReach.Length; i++)
            {
                if (inReach[i].collider.gameObject.layer == 7 && inReach[i].collider.gameObject.GetComponent<unitScript>().belongsToPlayer != this.belongsToPlayer)
                {
                    inReach[i].collider.gameObject.GetComponent<unitScript>().hitPoints -= Mathf.Max(1, (this.damage/ inReach[i].collider.gameObject.GetComponent<unitScript>().armor));
                    actualAttackDelay = attackDelay;
                    break;
                }
                else if (inReach[i].collider.gameObject.layer == 9 && inReach[i].collider.gameObject.GetComponent<gateScript>().belongsToPlayer != this.belongsToPlayer)
                {
                    actualAttackDelay = attackDelay;
                    break;
                }
            }
            this.state = State.Moving;
        }
        Debug.DrawLine(new Vector2(this.transform.position.x + (-(GetComponent<CircleCollider2D>().radius + 0.01f) * moveDirection), this.transform.position.y), new Vector2(this.transform.position.x + (-0.14f * moveDirection), this.transform.position.y), Color.green);

        //Soldier dies and is destroyed. TODO: Combat; TODO: Animation?; TODO: Blood?
        if (this.hitPoints <= 0)
        {
            this.state = State.Dying;
            Destroy(gameObject, 0.5f);
        }
    }
}
