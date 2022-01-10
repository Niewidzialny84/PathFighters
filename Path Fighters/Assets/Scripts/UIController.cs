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
    public DoubleInputPopup CreateDoubleInputPopup()
    {
        GameObject popup = Instantiate(Resources.Load("DoubleInputPopup") as GameObject);
        return popup.GetComponent<DoubleInputPopup>();
    }
    public SingleInputPopup CreateSingleInputPopup()
    {
        GameObject popup = Instantiate(Resources.Load("SingleInputPopup") as GameObject);
        return popup.GetComponent<SingleInputPopup>();
    }
    public YesNoPopup CreateYesNoPopup()
    {
        GameObject popup = Instantiate(Resources.Load("YesNoPopup") as GameObject);
        return popup.GetComponent<YesNoPopup>();
    }
}

