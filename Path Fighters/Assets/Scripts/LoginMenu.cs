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
    public void LeaveLobby()
    {
        Player.localPlayer.LeaveLobby();
        //SceneManager.LoadScene("Main Menu");
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
    public void CreateGame()
    {
        Player.localPlayer.HostGame(true);
        ParamsPasser.lobbyType = LobbyType.Create;
    }
    public void JoinGame()
    {
        var tmp = GameObject.Find("JoinGamePopUp").GetComponent<joinGame>();
        tmp.Popup();
        ParamsPasser.lobbyType = LobbyType.Join;
    }

}
public static class ParamsPasser
{
    public static LobbyType lobbyType { get; set; }
} 
public enum LobbyType
{
    Create,
    Join,
    Fast
}
