using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class UIController : MonoBehaviour
{
    // Start is called before the first frame update
    public static UIController Instance;
    public Transform MainCanvas;
    public void Start()
    {
        if (Instance != null)
        {
            GameObject.Destroy(this.gameObject);
            return;
        }
        Instance = this;
    }
    public InfoPopup CreatePopup()
    {
        GameObject popup = Instantiate(Resources.Load("InfoPopup") as GameObject);
        return popup.GetComponent<InfoPopup>();
    }
}
