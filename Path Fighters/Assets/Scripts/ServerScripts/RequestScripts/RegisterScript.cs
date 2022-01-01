using System.Collections;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.UI;
using TMPro;

public class RegisterScript : MonoBehaviour
{
    public UnityEvent<string> OnRegisterSuccess;

    public UnityEvent<string> OnRegisterFailure;

    [SerializeField] private TMP_InputField usernameInputField = default;
    [SerializeField] private TMP_InputField emailInputField = default;
    [SerializeField] private TMP_InputField emailInputConfirmField = default;
    [SerializeField] private TMP_InputField passwordInputField = default;
    [SerializeField] private TMP_InputField passwordInputConfirmField = default;

    public void OnRegisterButtonClick()
    {
        string username = usernameInputField.text;
        string email = emailInputField.text;
        string emailConfirm = emailInputConfirmField.text;
        string password = passwordInputField.text;
        string passwordConfirm = passwordInputConfirmField.text;

        if (username == "" || email == "" || emailConfirm == "" || password == "" || passwordConfirm == "")
        {
            OnRegisterFailure.Invoke("Please fill in all fields.");
            return;
        }

        if (email != emailConfirm)
        {
            OnRegisterFailure.Invoke("Emails do not match.");
            return;
        }

        if (password != passwordConfirm)
        {
            OnRegisterFailure.Invoke("Passwords do not match.");
            return;
        }

        RegisterClient(username, email, password);
    }

    public void Start()
    {
        OnRegisterSuccess.AddListener(SuccessHandler);
        OnRegisterFailure.AddListener(FailureHandler);
    }

    public void SuccessHandler(string msg)
    {
        Debug.Log(msg);
        //TODO: Add success message
    }

    public void FailureHandler(string msg)
    {
        Debug.Log(msg);
        //TODO: Add fail message
    }

    #region request
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
    #endregion
}