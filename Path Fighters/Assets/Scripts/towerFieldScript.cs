using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class towerFieldScript : MonoBehaviour
{
    private GameObject localTower;
    public int belongsToPlayer;

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
            buildTower();
        }
    }

    // This may also destroy the tower
    void buildTower()
    {
        GameObject gameHandler = GameObject.FindGameObjectWithTag("GameController");
        GameObject tower = gameHandler.GetComponent<gameHandlerScript>().selectedObject;

        //Check if the active player may build at this spot
        if (gameHandler.GetComponent<gameHandlerScript>().activePlayer == this.belongsToPlayer)
        {
            //Create selected tower
            if (tower != null && tower.layer == 8 && localTower == null && gameHandler.GetComponent<gameHandlerScript>().gold >= tower.GetComponent<towerScript>().cost)
            {
                var tempUnit = Instantiate(tower, new Vector3(this.transform.position.x, this.transform.position.y, 0), Quaternion.identity);
                gameHandler.GetComponent<gameHandlerScript>().gold -= tower.GetComponent<towerScript>().cost;
                localTower = tempUnit;
            }
            //Destroy tower
            else if (tower == null && localTower != null)
            {
                if(gameHandler.GetComponent<gameHandlerScript>().upgrades[this.belongsToPlayer - 1, 9]) { gameHandler.GetComponent<gameHandlerScript>().gold += (localTower.GetComponent<towerScript>().cost * 0.35f); }
                else { gameHandler.GetComponent<gameHandlerScript>().gold += (localTower.GetComponent<towerScript>().cost * 0.2f); }
                Destroy(localTower);
                localTower = null;
            }
        }
    }
}
