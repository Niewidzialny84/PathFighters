using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class gameHandlerScript : MonoBehaviour
{
    //This contains the selected object type
    public GameObject selectedObject;
    //This contains the active player
    public int activePlayer;

    // Start is called before the first frame update
    void Start()
    {
        //This will be handeled by the server
        activePlayer = 1;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
