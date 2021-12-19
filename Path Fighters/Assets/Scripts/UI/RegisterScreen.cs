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
    public void RegisterClient()
    {
        registerScript.RegisterClient(usernameInputField.text, emailInputField.text, passwordInputField.text);
    }

    public void Show()
    {
        gameObject.SetActive(true);
    }

    public void Hide()
    {
        gameObject.SetActive(false);
    }
}
