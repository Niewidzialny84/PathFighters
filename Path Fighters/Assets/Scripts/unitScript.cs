using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class unitScript : MonoBehaviour
{
    public float speed;

    private float rayDistance = 0.03f;
    private LayerMask ignoreMask;

    // Start is called before the first frame update
    void Start()
    {
        ignoreMask = LayerMask.GetMask("Path");
    }

    // Update is called once per frame
    void Update()
    {

        if (!Physics2D.Raycast(new Vector2(this.transform.position.x + 0.11f, this.transform.position.y), new Vector2(1f, 0f), rayDistance, ~ignoreMask) && this.transform.position.x < 6)
        {
            this.transform.position += new Vector3(this.speed * Time.deltaTime, 0, 0);
        }
        Debug.DrawLine(new Vector2(this.transform.position.x + 0.11f, this.transform.position.y), new Vector2(this.transform.position.x+0.14f, this.transform.position.y), Color.green);
    }
}
