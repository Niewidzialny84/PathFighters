using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class unitScript : MonoBehaviour
{
    public float speed;
    public int hitPoints;
    public int belongsToPlayer;
    private string status;
    private int moveDirection;

    private float rayDistance = 0.03f;
    private LayerMask ignoreMask;

    // Start is called before the first frame update
    void Start()
    {
        ignoreMask = LayerMask.GetMask("Path");
        this.status = "Moving";

        if(belongsToPlayer == 1)
        {
            moveDirection = -1;
        }
        else
        {
            moveDirection = 1;
        }
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
            //The 0.11f magic number is temporary and it is just outside the radius of the soldier to not hit himself
            if (!Physics2D.Raycast(new Vector2(this.transform.position.x - (0.11f * moveDirection), this.transform.position.y), new Vector2((-1f * moveDirection), 0f), rayDistance, ~ignoreMask) && this.transform.position.x >= -6 && this.transform.position.x <= 6)
            {
                this.transform.position += new Vector3((-this.speed * moveDirection) * Time.deltaTime, 0, 0);
            }
            Debug.DrawLine(new Vector2(this.transform.position.x + (-0.11f * moveDirection), this.transform.position.y), new Vector2(this.transform.position.x + (-0.14f * moveDirection), this.transform.position.y), Color.green);
        }
    }
}
