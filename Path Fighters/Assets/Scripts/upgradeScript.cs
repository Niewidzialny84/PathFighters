using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class upgradeScript : MonoBehaviour
{
    public bool active;
    public float researche;
    public float researcheGoal;
    public GameObject previousUpgrade;
    public int order;

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
        else if (this.active)
        {
            this.active = false;
            GameObject gameHandler = GameObject.FindGameObjectWithTag("GameController");
            gameHandler.GetComponent<gameHandlerScript>().upgrades[gameHandler.GetComponent<gameHandlerScript>().activePlayer - 1, this.order] = true;
        }
    }

    // This will activate if the mouse cursor is currently above
    void OnMouseOver()
    {
        if (Input.GetMouseButtonDown(0) && (previousUpgrade == null || previousUpgrade.GetComponent<upgradeScript>().IsDeveloped()) && !this.IsDeveloped())
        {
            Activate();
        }
    }

    // This funktion is responsible for activationg the right selectable and deactivate all others
    void Activate()
    {
        GameObject[] upgrades = GameObject.FindGameObjectsWithTag("upgrade");

        foreach (GameObject upgrade in upgrades)
        {
            upgrade.GetComponent<upgradeScript>().active = false;
        }

        this.active = true;
    }

    bool IsDeveloped()
    {
        if (this.researche >= this.researcheGoal) return true;
        return false;
    }
}
