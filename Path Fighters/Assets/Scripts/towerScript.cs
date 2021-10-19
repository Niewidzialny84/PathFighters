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

    // Start is called before the first frame update
    void Start()
    {
        if(this.transform.position.y <= 0)
        {
            attackHight = -0.5f;
        }
        else if(this.transform.position.y >= 3)
        {
            attackHight = 3.5f;
        }
        else
        {
            attackHight = 1.5f;
        }

        if (this.transform.position.x < 0)
        {
            belongsToPlayer = 2;
            this.attckDirection = 1;
        }
        else
        {
            belongsToPlayer = 1;
            this.attckDirection = -1;
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
            RaycastHit2D[] inReach = Physics2D.RaycastAll(new Vector2(5.8f * this.attckDirection, attackHight), new Vector2((-1f * attckDirection), 0f), reach, (LayerMask.GetMask("Unit")));
            for (int i = 0; i < inReach.Length; i++)
            {
                var enemy = inReach[i].collider.gameObject;
                if (enemy.GetComponent<unitScript>().belongsToPlayer != this.belongsToPlayer)
                {
                    enemy.GetComponent<unitScript>().hitPoints -= Mathf.Max(1, (this.damage - enemy.GetComponent<unitScript>().armor));
                    actualAttackDelay = attackDelay;
                    break;
                }
            }
        }
    }
}
