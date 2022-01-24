using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;

public class investorScript : NetworkBehaviour
{
    private float paymentTime;

    // Start is called before the first frame update
    void Start()
    {
        paymentTime = 1.0f;
    }

    // Update is called once per frame
    void Update()
    {
        if (isServer)
        {
            return;
        }
        if (paymentTime > 0.0f)
        {
            paymentTime -= Time.deltaTime;
        }
        else
        {
            var gameHandler = GameObject.FindGameObjectWithTag("GameController");
            if (gameObject.GetComponent<towerScript>().getPlayer() == gameHandler.GetComponent<gameHandlerScript>().activePlayer)
            {
                gameHandler.GetComponent<gameHandlerScript>().gold += 1f;
            }
            paymentTime = 1.0f;
        }
    }
}
