using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class codeInit : MonoBehaviour
{
    public static codeInit instance;
    public Color buttonColor = new Color(87, 44, 8, 255);
    public Color fadedbuttonColor = new Color(87, 44, 8, 0);
    public Color textColor = new Color(217, 175, 136, 255);
    [SerializeField] TextMeshProUGUI _Code;
    [SerializeField] TMP_InputField _InputField;

    [SerializeField] TMP_Text User1;

    [SerializeField] TMP_Text User2;
    [SerializeField] TMP_Text startText;
    [SerializeField] Button startButton;

    // Start is called before the first frame update
    void Start()
    {
        instance = this;

        //startButton.GetComponent<Image>().color = fadedbuttonColor;
        //startText.color = fadedbuttonColor;
        startButton.enabled = false;
        switch(ParamsPasser.lobbyType)
        {
            case LobbyType.Create:
                CreatedGame();
                break;
            case LobbyType.Fast:
                Debug.Log("??? Game");

                _InputField.text = "----";
                break;
            case LobbyType.Join:
                JoinedGame();
                break;
        }
            
    }

    public void BeginGame()
    {
        Player.localPlayer.BeginGame();
    }

    public void UpdatePlayers(List<Player> players)
    {
        Debug.Log($"Update Players {players.Count} ");

        if (players.Count == 1)
            User1.text = players[0].username;
        if(players.Count == 2)     
            User2.text = players[1].username;
    }
    
    public void JoinedGame()
    {
        Debug.Log("Joined Game");
        string code = Player.localPlayer.matchID;
        _Code.text = code;
        _InputField.text = code;
        User2.text = Player.localPlayer.username;

        List<Player> l = Player.localPlayer.currentMatch.players;
        foreach(Player p in l)
        {
            if(p.username != Player.localPlayer.username)
            {
                User1.text = p.username;
            }
        }
    }

    public void CreatedGame() 
    {
        string code = Player.localPlayer.matchID;
        _Code.text = code;
        Debug.Log("Create Game");
        _InputField.text = code;
        User1.text = Player.localPlayer.username;
    }
    public void Update()
    {
        if (User2.text != "---")
        {
            startButton.enabled = true;
            startButton.interactable = true;
            //startButton.GetComponent<Image>().color = buttonColor;
            //startText.color = textColor;
        }
        if (User2.text == "---" && startButton.enabled == true)
        {
            startButton.interactable = false;
            startButton.enabled = false;
            //startButton.GetComponent<Image>().color = fadedbuttonColor;
            //startText.color = fadedbuttonColor;
        }
    }
}
