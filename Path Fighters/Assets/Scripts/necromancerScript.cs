using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;

public class necromancerScript : NetworkBehaviour
{
    public GameObject thrall;
    private float summonTime;

    [SerializeField] private AudioSource summonS;

    // Start is called before the first frame update
    void Start()
    {
        summonTime = 10.0f;
    }

    // Update is called once per frame
    void Update()
    {
        if (isServer)
        {
            return;
        }
        if (summonTime > 0.0f)
        {
            summonTime -= Time.deltaTime;
        }
        else
        {
            int toPlayer = gameObject.GetComponent<towerScript>().getPlayer();
            Collider2D closestPath = Physics2D.OverlapCircle(new Vector3(toPlayer == 1 ? -5.9f : 5.9f, gameObject.GetComponent<towerScript>().attackHight, 0), 0.2f, LayerMask.GetMask("Path"));
            

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
                summonS.Play();

                var tempUnit = Instantiate(thrall, new Vector3(toPlayer == 1 ? -5.9f : 5.9f, closestPath.transform.position.y, 0), Quaternion.identity);
                tempUnit.GetComponent<unitScript>().belongsToPlayer = toPlayer;
                summonTime = 10.0f;
            }
        }
    }
}
