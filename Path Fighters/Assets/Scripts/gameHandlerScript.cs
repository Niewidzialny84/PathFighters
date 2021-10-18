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


    // TODO DELETE THIS
    bool aP = true;

    // Start is called before the first frame update
    void Start()
    {
        //This will be handeled by the server
        activePlayer = 1;
        recruitmentTime = 5.0f;
        gold = 500.4f;
    }

    // Update is called once per frame
    void Update()
    {
        if(recruitmentTime > 0f)
        {
            recruitmentTime -= (1.0f * Time.deltaTime);
        }

        if(gold < 1000000000000f)
        {
            gold += (10f * Time.deltaTime);
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
        UnityEditor.Handles.color = Color.white;
        UnityEditor.Handles.Label( this.transform.position, gold.ToString("F0"));
    }
}
