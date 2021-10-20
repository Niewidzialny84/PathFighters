using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class projectileScript : MonoBehaviour
{
    private GameObject target;
    private int damage;
    private bool hit;
    public float speed;

    public void setTarget(GameObject target)
    {
        this.target = target;
    }

    public void setDamage(int damage)
    {
        this.damage = damage;
    }

    // Start is called before the first frame update
    void Start()
    {
        hit = false;
    }

    // Update is called once per frame
    void Update()
    {
        if (target == null)
        {
            Destroy(gameObject);
        }
        else
        {
            transform.position = Vector2.MoveTowards(this.transform.position, target.transform.position, this.speed * Time.deltaTime);

            if (this.transform.position == target.transform.position)
            {
                if(!hit) target.GetComponent<unitScript>().hitPoints -= Mathf.Max(1, (this.damage - target.GetComponent<unitScript>().armor));
                hit = true;
                Destroy(gameObject, 0.1f);
            }
        }
    }
}
