using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MenuScript : MonoBehaviour
{

    [SerializeField]
    LoginScreen LoginScreen = default;
    
    [SerializeField]
    RegisterScreen RegisterScreen = default;

    [SerializeField]
    MainScreen MainScreen = default;

    /// <summary>
    /// Exit the game
    /// </summary>
    public void ExitButton()
    {
        Application.Quit();
        Debug.Log("Closing");
    }

    private void HideAll()
    {
        LoginScreen.Hide();
        RegisterScreen.Hide();
        MainScreen.Hide();
    }

    public void RegisterButton()
    {
        HideAll();
        RegisterScreen.Show();
    }

    public void GoToLoginScreen()
    {
        HideAll();
        LoginScreen.Init();
        LoginScreen.Show();
        LoginScreen.loginScript.OnLoginSuccess.AddListener(GoToMainScreen);
    }

    public void GoToMainScreen(LoginReturn data)
    {
        HideAll();
        MainScreen.Show();
        ApiURL.currentLoginReturn = data;
    }

    void Start()
    {
        GoToLoginScreen();
    }
}
