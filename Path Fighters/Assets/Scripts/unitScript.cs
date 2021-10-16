using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class unitScript : MonoBehaviour
{
    public float speed;
    public int hitPoints;
    public int belongsToPlayer;
    private string status;

    private float rayDistance = 0.03f;
    private LayerMask ignoreMask;

    // Start is called before the first frame update
    void Start()
    {
        ignoreMask = LayerMask.GetMask("Path");
        this.status = "Moving";

        //TODO: a variable 1P = 1; 2P = -1 should be set and used to reduce else if's later (for the movement and combat) once the players are included
    }

    // Update is called once per frame
    void Update()
    {
        //Soldier dies and is destroyed. TODO: Combat; TODO: Animation?; TODO: Blood?
        if (this.hitPoints <= 0)
        {
            this.status = "Dying";
            Destroy(gameObject, 0.5f);
        }

        if (this.status != "Dying")
        {
            if(belongsToPlayer == 1)
            {
                if (!Physics2D.Raycast(new Vector2(this.transform.position.x + 0.11f, this.transform.position.y), new Vector2(1f, 0f), rayDistance, ~ignoreMask) && this.transform.position.x < 6)
                {
                    this.transform.position += new Vector3(this.speed * Time.deltaTime, 0, 0);
                }
            }
            else if (belongsToPlayer == 2)
            {
                if (!Physics2D.Raycast(new Vector2(this.transform.position.x - 0.11f, this.transform.position.y), new Vector2(-1f, 0f), rayDistance, ~ignoreMask) && this.transform.position.x > -6)
                {
                    this.transform.position += new Vector3(-this.speed * Time.deltaTime, 0, 0);
                }
            }
            Debug.DrawLine(new Vector2(this.transform.position.x + 0.11f, this.transform.position.y), new Vector2(this.transform.position.x + 0.14f, this.transform.position.y), Color.green);
        }
    }
}
