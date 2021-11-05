using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HPbarScript : MonoBehaviour
{
    public int maxHP;

    // Start is called before the first frame update
    void Start()
    {
        this.maxHP = gameObject.GetComponentInParent<unitScript>().hitPoints;
    }

    // Update is called once per frame
    void Update()
    {
        float barLength = 6 * ((float)gameObject.GetComponentInParent<unitScript>().hitPoints / (float)this.maxHP);
        this.transform.localScale = new Vector3(Mathf.Max(0.5f,barLength), 1f, 0f);
    }
}
