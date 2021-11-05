using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class gateScript : MonoBehaviour
{
    public int belongsToPlayer;
    private GameObject gameHandler;

    public void receiveDamage(int damage)
    {
        gameHandler.GetComponent<gameHandlerScript>().baseHitPoints[this.belongsToPlayer - 1] -= damage;
    }

    // Start is called before the first frame update
    void Start()
    {
        gameHandler = GameObject.Find("gameHandler");
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
