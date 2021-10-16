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

        if (unit != null && unit.layer == 7)
        {
            var tempUnit = Instantiate(unit, new Vector3(activePlayer==1 ? -6 : 6, this.transform.position.y, 0), Quaternion.identity);
            tempUnit.GetComponent<unitScript>().belongsToPlayer = activePlayer;
        }
    }
}
