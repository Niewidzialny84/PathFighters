using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MenuScript : MonoBehaviour
{

    [SerializeField]
    LoginScreen LoginScreen;
    
    [SerializeField]
    RegisterScreen RegisterScreen;

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
    }

    public void RegisterButton()
    {
        HideAll();
        RegisterScreen.Show();
    }

    public void GoToLoginScreen()
    {
        HideAll();
        LoginScreen.Show();
    }

    void Start()
    {
        GoToLoginScreen();
    }
}
