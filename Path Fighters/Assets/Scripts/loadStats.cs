using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class loadStats : MonoBehaviour
{
    // Start is called before the first frame update
  void Start()
    {
        TextMeshProUGUI played = GameObject.Find("Main Camera/Canvas/Background/ButtonsBackground/TotalVal").GetComponent<TextMeshProUGUI>();
        TextMeshProUGUI won = GameObject.Find("Main Camera/Canvas/Background/ButtonsBackground/WonVal").GetComponent<TextMeshProUGUI>();
        TextMeshProUGUI lost = GameObject.Find("Main Camera/Canvas/Background/ButtonsBackground/LostVal").GetComponent<TextMeshProUGUI>();
        played.text = "10";
        won.text = "4";
        lost.text = "6";
    }

}
