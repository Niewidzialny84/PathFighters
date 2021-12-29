using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class gameHandlerScript : MonoBehaviour
{
    //This contains the selected object type
    public GameObject selectedObject;
    //This contains the active player
    public int activePlayer;
    //The gold available for the active player
    public float gold;
    //The time a player needs to wait between spawning new units. This will be handeled locally so there is no need to split it between players
    public float recruitmentTime;


    public int[] baseHitPoints = new int[2];
    public bool[,] upgrades = new bool[2,14];

    private float pauseEndTime;

    enum State
    {
        Active,
        Defeated,
        Victorious
    }
    State state;


    // TODO DELETE THIS
    bool aP = true;

    // Start is called before the first frame update
    void Start()
    {
        //This will be handeled by the server
        activePlayer = 1;
        recruitmentTime = 5.0f;
        gold = 150.0f;

        this.state = State.Active;
        this.baseHitPoints[0] = 500;
        this.baseHitPoints[1] = 500;

        pauseEndTime = 0;

        for(int i = 0; i < 14; i++)
        {
            upgrades[0,i] = upgrades[1,i] = false;
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (pauseEndTime != 0 && Time.realtimeSinceStartup > pauseEndTime)
        {
            Time.timeScale = 1f;
            //Here the game should end and the players should be moved to the summary screen
        }

        if (this.state == State.Active)
        {
            if (this.baseHitPoints[0] <= 0 || this.baseHitPoints[1] <= 0)
            {
                Time.timeScale = 0.1f;
                if (this.baseHitPoints[0] <= 0 || this.baseHitPoints[1] <= 0)
                {
                    this.pauseEndTime = Time.realtimeSinceStartup + 3;
                    this.state = State.Defeated;
                    //TODO: send that player is defeated with timestamp to the server for it to decide (based on time) who is the winner
                }
                else if (this.baseHitPoints[this.activePlayer - 1] <= 0)
                {
                    this.pauseEndTime = Time.realtimeSinceStartup + 3;
                    this.state = State.Defeated;
                    //TODO: send that player is defeated with timestamp to the server for it to decide (based on time) who is the winner
                }
                else
                {
                    this.pauseEndTime = Time.realtimeSinceStartup + 3;
                    this.state = State.Victorious;
                    //TODO: send that player is defeated with timestamp to the server for it to decide (based on time) who is the winner
                }
            }
            if (recruitmentTime > 0f)
            {
                recruitmentTime -= (1.0f * Time.deltaTime);
            }

            if (gold < 1000000000000f)
            {
                gold += (5f * Time.deltaTime);
            }
        }


        //THIS IS ONLY A TEST DELETE IS AFTERWARDS
        if (Input.GetMouseButtonDown(1))
        {
            if (aP)
            {
                activePlayer++;
                aP = false;
            }
            else if (!aP)
            {
                activePlayer--;
                aP = true;
            }
        }
    }

    void OnDrawGizmos()
    {
        // UnityEditor.Handles.color = Color.white;
        // UnityEditor.Handles.Label( this.transform.position, gold.ToString("F0"));
        // UnityEditor.Handles.Label(new Vector3(this.transform.position.x, this.transform.position.y + 0.3f ,0f), this.baseHitPoints[this.activePlayer - 1].ToString());
    }
}
