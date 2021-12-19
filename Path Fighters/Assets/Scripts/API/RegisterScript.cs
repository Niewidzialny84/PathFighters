using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

public class RegisterScript : MonoBehaviour
{
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

        var www = ApiURL.formatPost(ApiURL.REGISTER_URL, json);

        yield return www.SendWebRequest();

        if (www.responseCode == 201)
        {
            // Call success callback

            // Show results as text
            Debug.Log(www.downloadHandler.text);
        }
        else
        {
            // Call the error callback

            Debug.Log(www.error);
            Debug.Log(json);
        }
    }
}
