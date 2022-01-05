using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class towerScript : MonoBehaviour
{
    public float cost;
    public float attackHight;
    private int belongsToPlayer;
    private int attckDirection;

    public float reach;
    public float attackDelay; // This describes how long the delay between attacks is
    private float actualAttackDelay; // This is used to show how much of the delay is left.
    public int damage;

    public GameObject projectile;

    [SerializeField] private Animator animator;
    [SerializeField] private AudioSource attackS;

    // Start is called before the first frame update
    void Start()
    {
        if(this.transform.position.y <= 0.5)
        {
            attackHight = -0.5f;
        }
        else if(this.transform.position.y >= 3.5)
        {
            attackHight = 3.5f;
        }
        else
        {
            attackHight = 1.5f;
        }

        if (this.transform.position.x > 0)
        {
            belongsToPlayer = 2;
            attckDirection = -1;
        }
        else
        {
            belongsToPlayer = 1;
            attckDirection = 1;
        }

        actualAttackDelay = attackDelay;

        if (belongsToPlayer == 2)
        {
            this.transform.localScale = new Vector3(-1f, 1f, 0f);
        }

    }

    // Update is called once per frame
    void Update()
    {
        //Reduce the actual attack delay to allow the unit to be ready to attack.
        if (this.actualAttackDelay > 0f)
        {
            this.actualAttackDelay -= Time.deltaTime;
        }

        if (this.actualAttackDelay <= 0f)
        {
            try
            {
                attackS.Play();
            }
            catch (Exception e)
            {
            }


            RaycastHit2D[] inReach = Physics2D.RaycastAll(new Vector2(-6f * this.attckDirection, attackHight), new Vector2((1f * attckDirection), 0f), reach, (LayerMask.GetMask("Unit")));
            for (int i = 0; i < inReach.Length; i++)
            {
                var enemy = inReach[i].collider.gameObject;
                if (enemy.GetComponent<unitScript>().belongsToPlayer != this.belongsToPlayer)
                {
                    actualAttackDelay = attackDelay;

                    var tempProjectile = Instantiate(projectile, new Vector3(this.belongsToPlayer == 1 ? -5.9f : 5.9f, this.transform.position.y, 0), Quaternion.identity);
                    tempProjectile.GetComponent<projectileScript>().setTarget(enemy);
                    tempProjectile.GetComponent<projectileScript>().setDamage(damage);

                    try
                    {
                        animator.ResetTrigger("attack");
                        animator.SetTrigger("attack");
                    }
                    catch (Exception e)
                    {
                    }

                    break;
                }
            }
        }
    }

    public int getPlayer()
    {
        return belongsToPlayer;
    }
}
