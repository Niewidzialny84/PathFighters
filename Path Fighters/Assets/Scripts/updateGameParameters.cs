using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;



public class updateGameParameters : MonoBehaviour
{
    [SerializeField] TextMeshProUGUI _UserHP;
    [SerializeField] TextMeshProUGUI _EnemyHP;
    [SerializeField] TextMeshProUGUI _UserGold;
    public TextMeshProUGUI _Research;
    // Start is called before the first frame update
    public void Update()
    {
        GameObject gameHandler = GameObject.Find("gameHandler");
        gameHandlerScript handlerScript = gameHandler.GetComponent<gameHandlerScript>();

        _UserHP.text = (handlerScript.baseHitPoints[0]).ToString();
        _EnemyHP.text = (handlerScript.baseHitPoints[1]).ToString();
        _UserGold.text = (handlerScript.gold).ToString("F0");
        //_Research.text = ( i * 2).ToString();
    }
}
