using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;

public class MenuScript : MonoBehaviour
{

    [SerializeField]
    LoginScreen LoginScreen = default;
    
    [SerializeField]
    RegisterScreen RegisterScreen = default;

    [SerializeField]
    MainScreen MainScreen = default;

    [SerializeField]
    NetworkManager NetworkManager = default;

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
        NetworkManager.StartClient();
    }

    void Start()
    {
        GoToLoginScreen();
    }
}
