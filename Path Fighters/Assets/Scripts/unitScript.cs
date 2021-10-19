using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class unitScript : MonoBehaviour
{
    public float speed;
    public int hitPoints;
    public int belongsToPlayer;
    private int moveDirection;

    private float rayOffset;
    private float rayDistance;

    public float cost;

    //State machine enumerator
    enum State
    {
        Moving, //Idle and moving will have similar animations
        Fighting,
        Dying
    }
    private State state;

    // Start is called before the first frame update
    void Start()
    {
        rayDistance = 0.03f;
        rayOffset = 0.01f;

        this.state = State.Moving;

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
            this.state = State.Dying;
            Destroy(gameObject, 0.5f);
        }

        if (this.state != State.Dying)
        {
            if (!Physics2D.Raycast(new Vector2(this.transform.position.x - ((GetComponent<CircleCollider2D>().radius + rayOffset) * moveDirection), this.transform.position.y), new Vector2((-1f * moveDirection), 0f), rayDistance, (LayerMask.GetMask("Unit") | LayerMask.GetMask("Gate"))))
            {
                this.transform.position += new Vector3((-this.speed * moveDirection) * Time.deltaTime, 0, 0);
            }
        }
        Debug.DrawLine(new Vector2(this.transform.position.x + (-(GetComponent<CircleCollider2D>().radius + 0.01f) * moveDirection), this.transform.position.y), new Vector2(this.transform.position.x + (-0.14f * moveDirection), this.transform.position.y), Color.green);
    }
}
