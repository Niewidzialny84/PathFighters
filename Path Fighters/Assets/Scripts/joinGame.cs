using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using UnityEngine.Localization;
using UnityEngine.SceneManagement;

public class joinGame : MonoBehaviour
{
    // Start is called before the first frame update
    public void Popup()
    {
        Action action = () =>
        {
            Join();
        };
        SingleInputPopup doubleInput = UIController.Instance.CreateSingleInputPopup();
        LocalizedString title, leftButton, rightButton, password;
        title = new LocalizedString();
        leftButton = new LocalizedString();
        rightButton = new LocalizedString();

        password = new LocalizedString();

        title.TableReference = "Main Menu Text";
        title.TableEntryReference = "Join the game";

        leftButton.TableReference = "Main Menu Text";
        leftButton.TableEntryReference = "DP_Cancel";

        rightButton.TableReference = "Main Menu Text";
        rightButton.TableEntryReference = "Join";

        password.TableReference = "Main Menu Text";
        password.TableEntryReference = "Join_code";

        doubleInput.Init(UIController.Instance.MainCanvas, title.GetLocalizedString(), leftButton.GetLocalizedString(), rightButton.GetLocalizedString(), password.GetLocalizedString(), action);
        
    }
    void Join()
    {
        if(CodeValidation())
        {
            SceneManager.LoadScene("Lobby Scene");
            ParamsPasser.lobbyType = LobbyType.Join;
        }
    }
    bool CodeValidation()
    {
        return true;
    }
    // Update is called once per frame
    void Update()
    {

    }
}
