using UnityEngine;
using UnityEngine.SceneManagement;
using TMPro;
using Mirror;
using UnityEngine.Localization;

/*
    Documentation: https://mirror-networking.gitbook.io/docs/components/network-authenticators
    API Reference: https://mirror-networking.com/docs/api/Mirror.NetworkAuthenticator.html
*/

public class Authenticator : NetworkAuthenticator
{
    #region Messages

    public struct AuthRequestMessage : NetworkMessage 
    { 
        public LoginReturn loginReturn; 
    }

    public LoginReturn loginReturn { get; set; }

    public struct AuthResponseMessage : NetworkMessage { public bool valid; }

    #endregion

    #region Server

    /// <summary>
    /// Called on server from StartServer to initialize the Authenticator
    /// <para>Server message handlers should be registered in this method.</para>
    /// </summary>
    public override void OnStartServer()
    {
        // register a handler for the authentication request we expect from client
        NetworkServer.RegisterHandler<AuthRequestMessage>(OnAuthRequestMessage, false);
    }

    /// <summary>
    /// Called on server from OnServerAuthenticateInternal when a client needs to authenticate
    /// </summary>
    /// <param name="conn">Connection to client.</param>
    public override void OnServerAuthenticate(NetworkConnection conn) { }

    /// <summary>
    /// Called on server when the client's AuthRequestMessage arrives
    /// </summary>
    /// <param name="conn">Connection to client.</param>
    /// <param name="msg">The message payload</param>
    public void OnAuthRequestMessage(NetworkConnection conn, AuthRequestMessage msg)
    {
        Debug.Log("OnAuthRequestMessage");
        Debug.Log(msg.loginReturn.user.username);

        AuthResponseMessage authResponseMessage = new AuthResponseMessage();

        

        string username = msg.loginReturn.user.username;

        GameObject[] players = GameObject.FindGameObjectsWithTag("NetworkPlayer");
        foreach (var o in players)
        {
            if (o.GetComponent<Player>().username.Equals(username))
            {
                Debug.Log($"Znaleziono{username}");
                authResponseMessage.valid = false;
                conn.Send(authResponseMessage);
                //ServerReject(conn);
                return;
            }
        }

        GameObject player = Instantiate(NetworkManager.singleton.playerPrefab);
        player.GetComponent<Player>().username = msg.loginReturn.user.username;

        authResponseMessage.valid = true;
        conn.Send(authResponseMessage);
        NetworkServer.AddPlayerForConnection(conn, player);

        // Accept the successful authentication
        ServerAccept(conn);
    }

    #endregion

    #region Client

    /// <summary>
    /// Called on client from StartClient to initialize the Authenticator
    /// <para>Client message handlers should be registered in this method.</para>
    /// </summary>
    public override void OnStartClient()
    {
        // register a handler for the authentication response we expect from server
        NetworkClient.RegisterHandler<AuthResponseMessage>(OnAuthResponseMessage, false);
    }

    /// <summary>
    /// Called on client from OnClientAuthenticateInternal when a client needs to authenticate
    /// </summary>
    public override void OnClientAuthenticate()
    {
        Debug.Log("Authenticator.OnClientAuthenticate");

        AuthRequestMessage authRequestMessage = new AuthRequestMessage();
        authRequestMessage.loginReturn = loginReturn;
        
        NetworkClient.Send(authRequestMessage);
    }

    /// <summary>
    /// Called on client when the server's AuthResponseMessage arrives
    /// </summary>
    /// <param name="msg">The message payload</param>
    public void OnAuthResponseMessage(AuthResponseMessage msg)
    {
        Debug.Log($"On Auth Response Message {msg}");
        if (msg.valid)
        {
            // Authentication has been accepted
            ClientAccept();
        }
        else
        {
            
            // Authentication has been rejected
            ClientReject();
            Debug.Log(msg);
            InfoPopup popup = UIController.Instance.CreatePopup();
            LocalizedString message = new LocalizedString();
            message.TableReference = "Main Menu Text";
            message.TableEntryReference = "AlreadyLogged";
            popup.Init(UIController.Instance.MainCanvas, message.GetLocalizedString());
        }
        
    }

    #endregion
}