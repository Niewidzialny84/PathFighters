using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class necromancerScript : MonoBehaviour
{
    public GameObject thrall;
    private float summonTime;

    // Start is called before the first frame update
    void Start()
    {
        summonTime = 10.0f;
    }

    // Update is called once per frame
    void Update()
    {
        if (summonTime > 0.0f)
        {
            summonTime -= Time.deltaTime;
        }
        else
        {
            Collider2D closestPath = Physics2D.OverlapCircle(this.transform.position, 0.7f, LayerMask.GetMask("Path"));
            int toPlayer = gameObject.GetComponent<towerScript>().getPlayer();

            bool blocked = false;
            Collider2D[] inGate = Physics2D.OverlapCircleAll(new Vector3(toPlayer == 1 ? -5.9f : 5.9f, closestPath.transform.position.y, 0), 0.2f, LayerMask.GetMask("Unit"));
            for (int i = 0; i < inGate.Length; i++)
            {
                if (inGate[i].GetComponent<unitScript>().belongsToPlayer == toPlayer)
                {
                    blocked = true;
                    break;
                }
            }

            if (!blocked)
            {
                var tempUnit = Instantiate(thrall, new Vector3(toPlayer == 1 ? -5.9f : 5.9f, closestPath.transform.position.y, 0), Quaternion.identity);
                tempUnit.GetComponent<unitScript>().belongsToPlayer = toPlayer;
                summonTime = 10.0f;
            }
        }
    }
}
