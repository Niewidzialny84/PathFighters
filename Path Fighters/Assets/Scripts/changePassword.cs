using System.Collections;
using UnityEngine;
using System;
using UnityEngine.Localization;
using UnityEngine.UI;
using UnityEngine.Events;
using TMPro;
using Mirror;
using System.Text.RegularExpressions;

public class ChangePassword : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        OnChangeAccountSuccess.AddListener(SuccessHandler);

        Action action = () =>
        {
            ChangePass();
        };
        Button button = GetComponent<Button>();
        button.onClick.AddListener(() =>
        {
            DoubleInputPopup doubleInput = UIController.Instance.CreateDoubleInputPopup();
            LocalizedString title, leftButton, rightButton, oldPassword, newPassword;
            title = new LocalizedString();
            leftButton = new LocalizedString();
            rightButton = new LocalizedString();
            oldPassword = new LocalizedString();
            newPassword = new LocalizedString();

            title.TableReference = "Main Menu Text"; 
            title.TableEntryReference = "DP_ChangePassword";

            leftButton.TableReference = "Main Menu Text";
            leftButton.TableEntryReference = "DP_Cancel";

            rightButton.TableReference = "Main Menu Text";
            rightButton.TableEntryReference = "DP_Confirm";

            oldPassword.TableReference = "Main Menu Text";
            oldPassword.TableEntryReference = "DP_OldPass";

            newPassword.TableReference = "Main Menu Text";
            newPassword.TableEntryReference = "DP_NewPass";

            doubleInput.Init(UIController.Instance.MainCanvas, title.GetLocalizedString(), leftButton.GetLocalizedString(), rightButton.GetLocalizedString(), oldPassword.GetLocalizedString(), newPassword.GetLocalizedString(), action);
        });
    }
    void ChangePass()
    {
        loginReturn = GameObject.Find("NetworkManager").GetComponent<Variables>().loginReturn;
        Debug.Log(loginReturn.user.id + " in change passwd");
        if (loginReturn != null)
        {
            string oldPass = GameObject.Find("InputField1").GetComponent<TMP_InputField>().text;
            string newPass = GameObject.Find("InputField2").GetComponent<TMP_InputField>().text;

            oldPass = HashingHelper.GenerateSHA256(oldPass);
            if (!CheckPassword(newPass))
            {
                InfoPopup popup = UIController.Instance.CreatePopup();
                LocalizedString message = new LocalizedString();
                message.TableReference = "Main Menu Text";
                message.TableEntryReference = "DP_PasswordContains";
                popup.Init(UIController.Instance.MainCanvas, message.GetLocalizedString());
                return;
            }
            newPass = HashingHelper.GenerateSHA256(newPass);

            if (oldPass == "" || loginReturn.user.password != oldPass || newPass == "" || newPass == oldPass)
            {
                InfoPopup popup = UIController.Instance.CreatePopup();
                LocalizedString message = new LocalizedString();
                message.TableReference = "Main Menu Text";
                message.TableEntryReference = "Reg_InvalidData";
                popup.Init(UIController.Instance.MainCanvas, message.GetLocalizedString());
                return;
            }
           
            ChangePass(loginReturn.user.id, newPass, loginReturn.jwt_token);
        }
    }

    public void SuccessHandler(String msg)
    {
        Debug.Log("Password Changed");

        GameObject.Find("NetworkManager").GetComponent<Variables>().loginReturn.user.password = msg;

        InfoPopup popup = UIController.Instance.CreatePopup();
        LocalizedString message = new LocalizedString();
        message.TableReference = "Main Menu Text";
        message.TableEntryReference = "DP_Success";
        popup.Init(UIController.Instance.MainCanvas, message.GetLocalizedString());
        return;
    }
    public static bool CheckPassword(string passWord)
    {
        Debug.Log($"HALLOOO {passWord}");

        int validConditions = 0;
        if(passWord.Length<8) return false;
        foreach (char c in passWord)
        {
            if (c >= 'a' && c <= 'z')
            {
                validConditions++;
                break;
            }
        }
        foreach (char c in passWord)
        {
            if (c >= 'A' && c <= 'Z')
            {
                validConditions++;
                break;
            }
        }
        if (validConditions == 0) return false;
        foreach (char c in passWord)
        {
            if (c >= '0' && c <= '9')
            {
                validConditions++;
                break;
            }
        }
        if (validConditions == 1) return false;
        if (validConditions == 2)
        {
            char[] special = { '@', '#', '$', '%', '^', '&', '+', '=' }; // or whatever    
            if (passWord.IndexOfAny(special) == -1) return false;
        }
        return true;
        
    }

    #region ChangePassword

    private LoginReturn loginReturn;
    public UnityEvent<string> OnChangeAccountSuccess;
    public void ChangePass(int id, string password, string auth)
    {
        StartCoroutine(__ChangePassword(id, password, auth, false));
    }

    private IEnumerator __ChangePassword(int id, string password,string auth, bool refresh)
    {
        UserPasswordData data = new UserPasswordData(password);
        string json = JsonUtility.ToJson(data);

        var url = string.Format(ApiURL.USER_URL, id);
        var www = ApiFormater.formatPatch(url, json, auth);

        yield return www.SendWebRequest();

        if (www.responseCode == 200)
        {
            // Call success callback 
            OnChangeAccountSuccess.Invoke(password);

            // Show results as text
            Debug.Log(www.downloadHandler.text);
        }
        else
        {
            if(refresh == false)
            {
                Debug.Log("Refresh token after error");

                json = JsonUtility.ToJson(new LoginData(loginReturn.user.username, loginReturn.user.password));
                www = ApiFormater.formatPost(ApiURL.REFRESH_URL, json);
                
                yield return www.SendWebRequest();

                if(www.responseCode == 200)
                {
                    TokenReturn token = JsonUtility.FromJson<TokenReturn>(www.downloadHandler.text);
                    
                    GameObject.Find("NetworkManager").GetComponent<Variables>().loginReturn.jwt_token = token.jwt_token;
                    
                    StartCoroutine(__ChangePassword(id,password, token.jwt_token, true));
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
