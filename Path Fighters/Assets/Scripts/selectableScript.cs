using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class selectableScript : MonoBehaviour
{
    public GameObject setToSelected;
    public bool active;
    public int reaserchLevel;

    [SerializeField] private Animator animator;

    // Start is called before the first frame update
    void Start()
    {
        this.active = false;
    }

    // Update is called once per frame
    void Update()
    {
        try
        {
            animator.SetBool("Active", this.active);
        }
        catch (Exception e)
        {
        }
    }

    // This will activate if the mouse cursor is currently above
    void OnMouseOver()
    {
        if (Input.GetMouseButtonDown(0))
        {
            Activate();
        }
    }

    // This funktion is responsible for activationg the right selectable and deactivate all others
    void Activate()
    {
        GameObject gameHandler = GameObject.FindGameObjectWithTag("GameController");
        if (reaserchLevel == -1 || gameHandler.GetComponent<gameHandlerScript>().upgrades[gameHandler.GetComponent<gameHandlerScript>().activePlayer - 1, this.reaserchLevel]) 
        {
            GameObject[] selectables = GameObject.FindGameObjectsWithTag("selectable");

            foreach (GameObject selectable in selectables)
            {
                selectable.GetComponent<selectableScript>().active = false;
            }

            gameHandler.GetComponent<gameHandlerScript>().selectedObject = setToSelected;
            this.active = true;
        }
    }
}
