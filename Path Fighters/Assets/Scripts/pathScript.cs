using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class pathScript : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    // This will activate if the mouse cursor is currently above
    void OnMouseOver()
    {
        if (Input.GetMouseButtonDown(0))
        {
            spawnUnit();
        }
    }

    void spawnUnit()
    {
        GameObject gameHandler = GameObject.FindGameObjectWithTag("GameController");
        GameObject unit = gameHandler.GetComponent<gameHandlerScript>().selectedObject;
        int activePlayer = gameHandler.GetComponent<gameHandlerScript>().activePlayer;

        //This will make sure that units do not overlap if spawned in gate while another friendly unit is blocking it
        bool blocked = false;
        Collider2D[] inGate = Physics2D.OverlapCircleAll(new Vector3(activePlayer == 1 ? -5.9f : 5.9f, this.transform.position.y, 0), 0.2f, LayerMask.GetMask("Unit"));
        for (int i = 0; i < inGate.Length; i++)
        {
            if(inGate[i].GetComponent<unitScript>().belongsToPlayer == activePlayer)
            {
                blocked = true;
                break;
            }
        }

        if (unit != null && unit.layer == 7 && gameHandler.GetComponent<gameHandlerScript>().recruitmentTime <= 0f && gameHandler.GetComponent<gameHandlerScript>().gold >= unit.GetComponent<unitScript>().cost && !blocked)
        {
            var tempUnit = Instantiate(unit, new Vector3(activePlayer==1 ? -5.9f : 5.9f, this.transform.position.y, 0), Quaternion.identity);
            gameHandler.GetComponent<gameHandlerScript>().gold -= unit.GetComponent<unitScript>().cost;
            tempUnit.GetComponent<unitScript>().belongsToPlayer = activePlayer;
            gameHandler.GetComponent<gameHandlerScript>().recruitmentTime = 1.0f;
        }
    }
}
