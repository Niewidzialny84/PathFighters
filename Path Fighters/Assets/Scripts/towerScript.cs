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

    // Start is called before the first frame update
    void Start()
    {
        if(this.transform.position.y <= 0.5)
        {
            attackHight = 0f;
        }
        else if(this.transform.position.y >= 3.5)
        {
            attackHight = 4f;
        }
        else
        {
            attackHight = 2f;
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

                    break;
                }
            }
        }
    }
}
