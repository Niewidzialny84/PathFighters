using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.Networking;

public class RegisterScript : MonoBehaviour
{
    public UnityEvent<string> OnRegisterSuccess;

    public UnityEvent<string> OnRegisterFailure;

    /// <summary>
    /// Register a new user
    /// </summary>
    /// <param name="username"></param>
    /// <param name="email"></param>
    /// <param name="password"></param>
    public void RegisterClient(string username, string email, string password)
    {
        StartCoroutine(__RegisterClient(username, email, password));
    }

    private IEnumerator __RegisterClient(string username, string email, string password)
    {
        password = HashingHelper.GenerateSHA256(password);
        RegisterData registerData = new RegisterData(username, email, password);
        string json = JsonUtility.ToJson(registerData);

        var www = ApiFormater.formatPost(ApiURL.REGISTER_URL, json);

        yield return www.SendWebRequest();

        if (www.responseCode == 201)
        {
            // Call success callback
            OnRegisterSuccess.Invoke("Success");

            // Show results as text
            Debug.Log(www.downloadHandler.text);
        }
        else
        {
            // Call the error callback
            OnRegisterFailure.Invoke("Failure");

            Debug.Log(www.error);
        }
    }
}