using System.Collections;
using UnityEngine;
using System;
using UnityEngine.Localization;
using UnityEngine.UI;
using UnityEngine.Events;
using TMPro;

public class Surrender : MonoBehaviour
{
    private LoginReturn loginReturn;
    // Start is called before the first frame update
    void Start()
    {

        Action action = () =>
        {
            AcceptSurrender();
        };
        Button button = GetComponent<Button>();
        button.onClick.AddListener(() =>
        {
            YesNoPopup yesNoPopup = UIController.Instance.CreateYesNoPopup();
            
            LocalizedString title, leftButton, rightButton, text;
            title = new LocalizedString();
            leftButton = new LocalizedString();
            rightButton = new LocalizedString();
            text = new LocalizedString();

            title.TableReference = "Game Localization";
            title.TableEntryReference = "G_Surrender";

            leftButton.TableReference = "Game Localization";
            leftButton.TableEntryReference = "No";

            rightButton.TableReference = "Game Localization";
            rightButton.TableEntryReference = "Yes";

            text.TableReference = "Game Localization";
            text.TableEntryReference = "G_Surrender_Info";

            yesNoPopup.Init(UIController.Instance.MainCanvas, title.GetLocalizedString(), leftButton.GetLocalizedString(), rightButton.GetLocalizedString(), text.GetLocalizedString(), action);
        });
    }
    void AcceptSurrender()
    {
        Player.localPlayer.surrenderGame(GameObject.Find("gameHandler").GetComponent<gameHandlerScript>().activePlayer);

        //loginReturn = GameObject.Find("NetworkManager").GetComponent<Variables>().loginReturn;
        //AddLose(loginReturn.user.id, loginReturn.jwt_token);
        //InfoPopup popup = UIController.Instance.CreatePopup();
        //LocalizedString message = new LocalizedString();
        //message.TableReference = "Game Localization";
        //message.TableEntryReference = "G_Defeat";
        //popup.Initialize(UIController.Instance.MainCanvas, message.GetLocalizedString());
    }
    // Update is called once per frame
    public void AddLose(int id, string auth)
    {
        StartCoroutine(__AddLose(id, auth, false));
    }

    private IEnumerator __AddLose(int id, string auth, bool refresh)
    {
        string json = " ";

        var url = string.Format(ApiURL.STATS_USER_LOSE, id);
        var www = ApiFormater.formatPatch(url, json, auth);

        yield return www.SendWebRequest();

        if (www.responseCode == 200)
        {
            // Call success callback 

            // Show results as text
            Debug.Log(www.downloadHandler.text);
        }
        else
        {
            if (refresh == false)
            {
                Debug.Log("Refresh token after error");

                json = JsonUtility.ToJson(new LoginData(loginReturn.user.username, loginReturn.user.password));
                www = ApiFormater.formatPost(ApiURL.REFRESH_URL, json);

                yield return www.SendWebRequest();

                if (www.responseCode == 200)
                {
                    TokenReturn token = JsonUtility.FromJson<TokenReturn>(www.downloadHandler.text);

                    GameObject.Find("NetworkManager").GetComponent<Variables>().loginReturn.jwt_token = token.jwt_token;

                    StartCoroutine(__AddLose(id, token.jwt_token, true));
                }
                else
                {
                    Debug.Log(www.error);
                }
            }
            else
            {
                // Call the error callback
                Debug.Log(www.error);
            }
        }
    }
}
