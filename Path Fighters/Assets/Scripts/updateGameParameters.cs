using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;



public class updateGameParameters : MonoBehaviour
{
    int i = 0;
    [SerializeField] TextMeshProUGUI _UserHP;
    [SerializeField] TextMeshProUGUI _EnemyHP;
    [SerializeField] TextMeshProUGUI _UserGold;
    [SerializeField] TextMeshProUGUI _Research;
    // Start is called before the first frame update
    public void Update()
    {
        GameObject gameHandler = GameObject.Find("gameHandler");
        gameHandlerScript handlerScript = gameHandler.GetComponent<gameHandlerScript>();

        i++;
        _UserHP.text = (handlerScript.baseHitPoints[0]).ToString();
        _EnemyHP.text = (handlerScript.baseHitPoints[1]).ToString();
        _UserGold.text = (handlerScript.gold).ToString();
        _Research.text = ( i * 2).ToString();
    }
}
