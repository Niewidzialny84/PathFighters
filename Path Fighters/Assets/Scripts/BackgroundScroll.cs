using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BackgroundScroll : MonoBehaviour
{
    public float speed = 5f;
    private Vector2 StartPosition;
    private float modifier = 1f;

    void Start()
    {
        StartPosition = transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        float newPos = Mathf.Repeat(Time.time * speed, 220);
        transform.position = StartPosition + Vector2.left * (newPos*modifier);
        if((StartPosition + Vector2.left * (newPos * modifier)).Equals(StartPosition+(new Vector2(220,0))))
        {
            modifier = modifier * (-1f);
        }
        
    }
}