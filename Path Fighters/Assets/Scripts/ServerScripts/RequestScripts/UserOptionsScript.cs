using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.Networking;

public class UserOptionsScript : MonoBehaviour
{
    #region DeleteAccount
    public UnityEvent<string> OnDeleteAccountSuccess;
    public void DeleteAccount(int id, string auth)
    {
        StartCoroutine(__DeleteAccount(id, auth));
    }

    private IEnumerator __DeleteAccount(int id,string auth)
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
            // Call the error callback
            Debug.Log(www.error);
        }
    }
    #endregion

    #region ChangePassword
    public void ChangePassword(int id, string password, string auth)
    {
        StartCoroutine(__ChangePassword(id, password, auth));
    }

    private IEnumerator __ChangePassword(int id, string password,string auth)
    {
        password = HashingHelper.GenerateSHA256(password);
        UserPasswordData data = new UserPasswordData(password);
        string json = JsonUtility.ToJson(data);

        var url = string.Format(ApiURL.USER_URL, id);
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
            // Call the error callback
            Debug.Log(www.error);
        }
    }
    #endregion
}