using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class codeInit : MonoBehaviour
{
    [SerializeField] TextMeshProUGUI _Code;
    [SerializeField] TMP_InputField _InputField;

    // Start is called before the first frame update
    void Start()
    {
        
        switch(ParamsPasser.lobbyType)
        {
            case LobbyType.Create:
                _Code.text = GetCode();
                Debug.Log("Create Game");
                _InputField.text = GetCode();
                break;
            case LobbyType.Fast:
                Debug.Log("Create Game");

                _InputField.text = "----";
                break;
            case LobbyType.Join:
                Debug.Log("Join Game");
                _InputField.text = "----";
                break;
        }
            
    }
    string GetCode()
    {
        return "1234";
    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
