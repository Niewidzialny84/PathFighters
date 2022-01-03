using System.Collections;
using UnityEngine;
using UnityEngine.Events;
using TMPro;
using Mirror;

public class LoginScript : MonoBehaviour
{
    public UnityEvent<LoginReturn> OnLoginSuccess;

    public UnityEvent<string> OnLoginFailure;

    [SerializeField] private TMP_InputField usernameInputField = default;
    [SerializeField] private TMP_InputField passwordInputField = default;

    public void OnLoginButtonClick()
    {
        string username = usernameInputField.text;
        string password = passwordInputField.text;

        if (username == "" || password == "")
        {
            OnLoginFailure.Invoke("Please fill in all fields.");
            return;
        }

        LoginClient(username, password);
    }

    public void Start()
    {
        OnLoginSuccess.AddListener(SuccessHandler);
        OnLoginFailure.AddListener(FailureHandler);
    }

    public void SuccessHandler(LoginReturn msg)
    {
        Debug.Log("Login Successful");
        gameObject.GetComponent<Authenticator>().loginReturn = msg;
        GameObject.Find("NetworkManager").GetComponent<NetworkManager>().StartClient();
        GameObject.Find("NetworkManager").GetComponent<Variables>().loginReturn = msg;
    }

    public void FailureHandler(string msg)
    {
        Debug.Log(msg);
        //TODO: Add fail message
    }

    #region request
    public void LoginClient(string username, string password)
    {
        StartCoroutine(__LoginClient(username, password));
    }

    private IEnumerator __LoginClient(string username, string password)
    {
        password = HashingHelper.GenerateSHA256(password);
        LoginData loginData = new LoginData(username, password);
        string json = JsonUtility.ToJson(loginData);

        var www = ApiFormater.formatPost(ApiURL.LOGIN_URL, json);

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
    #endregion
}