using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class LoginMenu : MonoBehaviour
{
   public void ExitButton()
    {
        Application.Quit();
        Debug.Log("Closing");
    }
    public void Login()
    {
        SceneManager.LoadScene("Main Menu");
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
    public void Stats()
    {
        SceneManager.LoadScene("Stats Scene");
    }

    public void Settings()
    {
        SceneManager.LoadScene("Settings Scene");
    }
}
