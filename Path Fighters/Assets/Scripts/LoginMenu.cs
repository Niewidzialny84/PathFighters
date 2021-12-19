using UnityEngine;
using UnityEngine.SceneManagement;
using TMPro;

public class LoginMenu : MonoBehaviour
{
    [SerializeField] private TMP_InputField usernameInputField = default;
    [SerializeField] private TMP_InputField passwordInputField = default;

    public void ExitButton()
    {
        Application.Quit();
        Debug.Log("Closing");
    }
    public void Login()
    {
        Debug.Log(usernameInputField.text);
       // Debug.Log(StartCoroutine(API.Login.GetUser(usernameInputField.text)));

        //SceneManager.LoadScene("Main Menu");
    }
    public void Register()
    {
        SceneManager.LoadScene("Register Scene");
    }
    public void StartGame()
    {
        SceneManager.LoadScene("Start Game Scene");
    }
    public void ReturnToMainMenu()
    {
        SceneManager.LoadScene("Main Menu");
    }
    public void ReturnToLoginScene()
    {
        SceneManager.LoadScene("Login Window");
    }
}
