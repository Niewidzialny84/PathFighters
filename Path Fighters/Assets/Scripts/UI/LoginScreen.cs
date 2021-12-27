using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class LoginScreen : MonoBehaviour
{
    [SerializeField] 
    private TMP_InputField usernameInputField = default;

    [SerializeField] 
    private TMP_InputField passwordInputField = default;

    [SerializeField]
    public LoginScript loginScript = default;

    [SerializeField]
    TMP_Text infoText = default;

    public void Init()
    {
        loginScript.OnLoginFailure.AddListener(OnLoginFailure);
        loginScript.OnLoginSuccess.AddListener(OnLoginSuccess);
    }

    public void LoginClient()
    {
        loginScript.LoginClient(usernameInputField.text, passwordInputField.text);
    }

    public void Show()
    {
        infoText.text = "";
        gameObject.SetActive(true);
    }

    public void Hide()
    {
        gameObject.SetActive(false);
    }

    public void OnLoginSuccess(LoginReturn data)
    {
        Debug.Log("Login Success");
    }

    public void OnLoginFailure(string message)
    {
        infoText.text = message;
    }
}
