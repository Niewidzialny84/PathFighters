using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;

public class towerFieldScript : NetworkBehaviour
{
    [SerializeField] private GameObject localTower;
    public int belongsToPlayer;

    [SerializeField] private Animator animator;

    // Start is called before the first frame update
    void Start()
    {
        if (this.transform.position.x > 0)
        {
            belongsToPlayer = 2;
        }
        else
        {
            belongsToPlayer = 1;
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (isServer) return;
        GameObject gameHandler = GameObject.FindGameObjectWithTag("GameController");
        if (gameHandler.GetComponent<gameHandlerScript>().activePlayer == this.belongsToPlayer)
        {
            animator.SetBool("active", true);
        }
        else
        {
            animator.SetBool("active", false);
        }
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
            bool blocked = false;
            Collider2D isTower = Physics2D.OverlapCircle(new Vector3(this.transform.position.x, this.transform.position.y, 0), 0.2f, LayerMask.GetMask("Tower"));
            if(isTower != null)
            {
                blocked = true;
            }

            //Create selected tower
            if (tower != null && tower.layer == 8 && !blocked && gameHandler.GetComponent<gameHandlerScript>().gold >= tower.GetComponent<towerScript>().cost)
            {
                var v = new Vector3(this.transform.position.x, this.transform.position.y, 0);
                //var tempUnit = Instantiate(tower, v, Quaternion.identity);
                gameHandler.GetComponent<gameHandlerScript>().gold -= tower.GetComponent<towerScript>().cost;
                int i = Player.getPrefabFromName(tower.name);
                Player.localPlayer.SpawnTower(i, v, this.belongsToPlayer);
            }
        }
    }

    public void setLocalTower(GameObject tower)
    {
        localTower = tower;
    }
}
