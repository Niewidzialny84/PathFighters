using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class upgradeScript : MonoBehaviour
{
    public bool active;
    private float researche;
    public float researcheGoal;
    public GameObject previousUpgrade;
    public int order;

    [SerializeField] private AudioSource researchS;

    public Animator animator;

    // Start is called before the first frame update
    void Start()
    {
        this.researche = 0.0f;
        this.active = false;

        if(order == 0 || order == 7)
        {
            try
            {
                animator.SetTrigger("Able");
            }
            catch (Exception e)
            {
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        GameObject canvas = GameObject.FindGameObjectWithTag("canvas");

        if (this.active && researche <= researcheGoal)
        {
            researche += Time.deltaTime;
            canvas.GetComponent<updateGameParameters>()._Research.text = (researcheGoal - researche).ToString("F0");
        }
        else if (this.active)
        {
            GameObject[] selectables = GameObject.FindGameObjectsWithTag("selectable");

            foreach (GameObject s in selectables)
            {
                if (s.GetComponent<selectableScript>().reaserchLevel == order)
                {
                    s.GetComponent<selectableScript>().SetAnimator();
                }
            }

            canvas.GetComponent<updateGameParameters>()._Research.text = "-";
            researchS.Play();

            this.active = false;
            GameObject gameHandler = GameObject.FindGameObjectWithTag("GameController");
            var belongsToPlayer = gameHandler.GetComponent<gameHandlerScript>().activePlayer;
            gameHandler.GetComponent<gameHandlerScript>().upgrades[belongsToPlayer - 1, this.order] = true;
            if (order == 13)
            {
                Player.localPlayer.updateTech(order, belongsToPlayer, Player.localPlayer.matchID);
            }
            else if (order == 3)
            {
                Player.localPlayer.updateTech(order, belongsToPlayer, Player.localPlayer.matchID);
            }
            else if (order == 5)
            {
                Player.localPlayer.updateTech(order, belongsToPlayer, Player.localPlayer.matchID);
            }

            try
            {
                animator.SetTrigger("Ready");
            }
            catch (Exception e)
            {
            }
            if (order != 6 && order != 13)
            {
                GameObject[] upgrades = GameObject.FindGameObjectsWithTag("upgrade");

                foreach (GameObject upgrade in upgrades)
                {
                    if (upgrade.GetComponent<upgradeScript>().order == this.order + 1)
                    {
                        try
                        {
                            upgrade.GetComponent<upgradeScript>().animator.SetTrigger("Able");
                        }
                        catch (Exception e)
                        {
                        }
                    }
                }
            }
        }
    }

    // This will activate if the mouse cursor is currently above
    void OnMouseOver()
    {
        if (Input.GetMouseButtonDown(0) && (previousUpgrade == null || previousUpgrade.GetComponent<upgradeScript>().IsDeveloped()) && !this.IsDeveloped())
        {
            activate();
        }
    }

    // This funktion is responsible for activationg the right selectable and deactivate all others
    void activate()
    {
        GameObject[] upgrades = GameObject.FindGameObjectsWithTag("upgrade");

        foreach (GameObject upgrade in upgrades)
        {
            upgrade.GetComponent<upgradeScript>().active = false;
            try
            {
                upgrade.GetComponent<upgradeScript>().animator.SetBool("WIP", false);
            }
            catch (Exception e)
            {
            }
        }

        this.active = true;
        try
        {
            animator.SetBool("WIP", true);
        }
        catch (Exception e)
        {
        }
    }

    bool IsDeveloped()
    {
        if (this.researche >= this.researcheGoal) return true;
        return false;
    }
}
