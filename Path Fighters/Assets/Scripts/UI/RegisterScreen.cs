using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class RegisterScreen : MonoBehaviour
{
    [SerializeField] private TMP_InputField usernameInputField = default;
    [SerializeField] private TMP_InputField emailInputField = default;
    [SerializeField] private TMP_InputField passwordInputField = default;
    [SerializeField] private RegisterScript registerScript = default;
    [SerializeField] private TMP_Text infoText = default;

    public void Start()
    {
        registerScript.OnRegisterFailure.AddListener(OnRegisterFailure);
        registerScript.OnRegisterSuccess.AddListener(OnRegisterSuccess);
    }
    public void RegisterClient()
    {
        registerScript.RegisterClient(usernameInputField.text, emailInputField.text, passwordInputField.text);
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

    public void OnRegisterSuccess(string message)
    {
        infoText.text = message;
    }

    public void OnRegisterFailure(string message)
    {
        infoText.text = message;
    }
}
