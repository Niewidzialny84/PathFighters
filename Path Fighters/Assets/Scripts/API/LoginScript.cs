using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.Networking;

public class LoginScript : MonoBehaviour
{
    public UnityEvent<LoginReturn> OnLoginSuccess;

    public UnityEvent<string> OnLoginFailure;

    public void LoginClient(string username, string password)
    {
        StartCoroutine(__LoginClient(username, password));
    }

    private IEnumerator __LoginClient(string username, string password)
    {
        password = HashingHelper.GenerateSHA256(password);
        LoginData loginData = new LoginData(username, password);
        string json = JsonUtility.ToJson(loginData);

        var www = ApiURL.formatPost(ApiURL.LOGIN_URL, json);

        yield return www.SendWebRequest();

        if (www.responseCode == 200)
        {
            LoginReturn loginReturn = JsonUtility.FromJson<LoginReturn>(www.downloadHandler.text);

            // Call success callback
            OnLoginSuccess.Invoke(loginReturn);

            // Show results as text
            Debug.Log(www.downloadHandler.text);
        }
        else
        {
            // Call the error callback
            OnLoginFailure.Invoke("Failure");

            Debug.Log(www.error);
        }
    }
}
