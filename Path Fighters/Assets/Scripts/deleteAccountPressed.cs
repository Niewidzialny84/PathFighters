using System.Collections;
using UnityEngine;
using System;
using UnityEngine.Localization;
using UnityEngine.UI;
using UnityEngine.Events;
using TMPro;
using Mirror;

public class deleteAccountPressed : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        OnDeleteAccountSuccess.AddListener(SuccessHandler);
        Action action = () =>
        {
            DeleteAccount();
            Debug.Log("Closing");
        };
        Button button = GetComponent<Button>();
        button.onClick.AddListener(() =>
        {
            SingleInputPopup doubleInput = UIController.Instance.CreateSingleInputPopup();
            LocalizedString title, leftButton, rightButton, password; 
            title = new LocalizedString();
            leftButton = new LocalizedString();
            rightButton = new LocalizedString();
      
            password = new LocalizedString();

            title.TableReference = "Main Menu Text";
            title.TableEntryReference = "SP_DeleteAccount";

            leftButton.TableReference = "Main Menu Text";
            leftButton.TableEntryReference = "DP_Cancel";

            rightButton.TableReference = "Main Menu Text";
            rightButton.TableEntryReference = "DP_Confirm";

            password.TableReference = "Main Menu Text";
            password.TableEntryReference = "SP_Password";

            doubleInput.Init(UIController.Instance.MainCanvas, title.GetLocalizedString(), leftButton.GetLocalizedString(), rightButton.GetLocalizedString(), password.GetLocalizedString(), action);
        });
    }
    void DeleteAccount()
    {
        loginReturn = GameObject.Find("NetworkManager").GetComponent<Variables>().loginReturn;
        Debug.Log(loginReturn.user.id + " in delete account");
        if (loginReturn != null)
        {
            string pass = GameObject.Find("SingleInputPopup(Clone)").GetComponent<SingleInputPopup>().GetComponentInChildren<TMP_InputField>().text;
            pass = HashingHelper.GenerateSHA256(pass);

            if (pass == "" || loginReturn.user.password != pass)
            {
                InfoPopup popup = UIController.Instance.CreatePopup();
                LocalizedString message = new LocalizedString();
                message.TableReference = "Main Menu Text";
                message.TableEntryReference = "Reg_InvalidData";
                popup.Init(UIController.Instance.MainCanvas, message.GetLocalizedString());
                return;
            }

            DeleteAccount(loginReturn.user.id, loginReturn.jwt_token);
            

            Debug.Log("Account Deleted");
        }
    }

    public void SuccessHandler(String msg)
    {
        Debug.Log("Account deleted disconecting client");
        GameObject.Find("NetworkManager").GetComponent<NetworkManager>().StopClient();
        Application.Quit();
    }

    #region DeleteAccount
    private LoginReturn loginReturn;
    public UnityEvent<string> OnDeleteAccountSuccess;
    public void DeleteAccount(int id, string auth)
    {
        StartCoroutine(__DeleteAccount(id, auth, false));
    }

    private IEnumerator __DeleteAccount(int id,string auth, bool refresh)
    {
        var url = string.Format(ApiURL.USER_URL, id);
        var www = ApiFormater.formatDelete(url, auth);

        yield return www.SendWebRequest();

        if (www.responseCode == 200)
        {
            // Call success callback 
            OnDeleteAccountSuccess.Invoke("Success");

            // Show results as text
            Debug.Log(www.downloadHandler.text);
        }
        else
        {
            if(refresh == false)
            {
                Debug.Log("Refresh token after error");

                var json = JsonUtility.ToJson(new LoginData(loginReturn.user.username, loginReturn.user.password));
                www = ApiFormater.formatPost(ApiURL.REFRESH_URL, json);
                
                yield return www.SendWebRequest();

                if(www.responseCode == 200)
                {
                    TokenReturn token = JsonUtility.FromJson<TokenReturn>(www.downloadHandler.text);
                    
                    GameObject.Find("NetworkManager").GetComponent<Variables>().loginReturn.jwt_token = token.jwt_token;
                    
                    StartCoroutine(__DeleteAccount(id, token.jwt_token, true));
                } else
                {
                    Debug.Log(www.error);
                }
            }
            // Call the error callback
            Debug.Log(www.error);
        }
    }

    #endregion

}
