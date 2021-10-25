using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class upgradeScript : MonoBehaviour
{
    public bool active;
    public float researche;
    public float researcheGoal;

    // Start is called before the first frame update
    void Start()
    {
        this.researche = 0.0f;
        this.active = false;
    }

    // Update is called once per frame
    void Update()
    {
        if (this.active && researche <= researcheGoal)
        {
            researche += Time.deltaTime;
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
        GameObject[] selectables = GameObject.FindGameObjectsWithTag("upgrade");

        foreach (GameObject selectable in selectables)
        {
            selectable.GetComponent<upgradeScript>().active = false;
        }

        this.active = true;
    }
}
