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

}
