using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class gameHandlerScript : MonoBehaviour
{
    //This contains the selected object type
    public GameObject selectedObject;
    //This contains the active player
    public int activePlayer;


    // TODO DELETE THIS
    bool aP = true;

    // Start is called before the first frame update
    void Start()
    {
        //This will be handeled by the server
        activePlayer = 1;
    }

    // Update is called once per frame
    void Update()
    {
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
}
