using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.Localization;
public class gameHandlerScript : MonoBehaviour
{
    //This contains the selected object type
    public GameObject selectedObject;
    //This contains the active player
    public int activePlayer;
    //The gold available for the active player
    public float gold;
    //The time a player needs to wait between spawning new units. This will be handeled locally so there is no need to split it between players
    public float recruitmentTime;


    LoginReturn loginReturn;


    public int[] baseHitPoints = new int[2];
    public bool[,] upgrades = new bool[2,14];

    private float pauseEndTime;
    private bool disabled;

    enum State
    {
        Active,
        Defeated,
        Victorious
    }
    State state;

    // Start is called before the first frame update
    void Start()
    {
        //This will be handeled by the server
        if(Player.localPlayer.currentMatch.players.Count == 2)
        {
            activePlayer = 2;
        } else {
            activePlayer = 1;
        }

        Debug.Log("Active player: " + activePlayer);
        
        recruitmentTime = 5.0f;
        gold = 150.0f;

        this.state = State.Active;
        this.baseHitPoints[0] = 500;
        this.baseHitPoints[1] = 500;

        pauseEndTime = 0;

        for(int i = 0; i < 14; i++)
        {
            upgrades[0,i] = upgrades[1,i] = false;
        }

        disabled = false;
    }

    // Update is called once per frame
    void Update()
    {
        if (disabled)
        {
            selectedObject = null;
        }

        //if (pauseEndTime != 0 && Time.realtimeSinceStartup > pauseEndTime)
        //{
        //    Time.timeScale = 1f;
        //    //Here the game should end and the players should be moved to the summary screen
        //}

        if (this.state == State.Active)
        {
            if (this.baseHitPoints[0] <= 0 || this.baseHitPoints[1] <= 0)
            {
                if (this.baseHitPoints[this.activePlayer - 1] <= 0)
                {
                    disabled = true;
                    this.pauseEndTime = Time.realtimeSinceStartup + 3;
                    this.state = State.Defeated;
                    Defeated();
                }
                else
                {
                    disabled = true;
                    this.pauseEndTime = Time.realtimeSinceStartup + 3;
                    this.state = State.Victorious;
                    Victorious();
                }
            }
            if (recruitmentTime > 0f)
            {
                recruitmentTime -= (1.0f * Time.deltaTime);
            }

            if (gold < 1000000f)
            {
                if (upgrades[activePlayer - 1, 7]) { gold += (7f * Time.deltaTime); }
                else { gold += (4f * Time.deltaTime); }  
            }
        }
    }
    #region Win
    public void AddWin(int id, string auth)
    {
        StartCoroutine(__AddWin(id, auth,false));
    }

    private IEnumerator __AddWin(int id, string auth,bool refresh)
    {
        string json = " ";

        var url = string.Format(ApiURL.STATS_USER_WIN, id);
        var www = ApiFormater.formatPatch(url, json, auth);

        yield return www.SendWebRequest();

        if (www.responseCode == 200)
        {
            // Call success callback 

            // Show results as text
            Debug.Log(www.downloadHandler.text);
        }
        else
        {
            if (refresh == false)
            {
                Debug.Log("Refresh token after error");

                json = JsonUtility.ToJson(new LoginData(loginReturn.user.username, loginReturn.user.password));
                www = ApiFormater.formatPost(ApiURL.REFRESH_URL, json);

                yield return www.SendWebRequest();

                if (www.responseCode == 200)
                {
                    TokenReturn token = JsonUtility.FromJson<TokenReturn>(www.downloadHandler.text);

                    GameObject.Find("NetworkManager").GetComponent<Variables>().loginReturn.jwt_token = token.jwt_token;

                    StartCoroutine(__AddWin(id, token.jwt_token, true));
                }
                else
                {
                    Debug.Log(www.error);
                }
            }
            else
            {
                // Call the error callback
                Debug.Log(www.error);
            }
            // Call the error callback
        }
    }
    #endregion

    #region Lose
    public void AddLose(int id, string auth)
    {
        StartCoroutine(__AddLose(id, auth,false));
    }

    private IEnumerator __AddLose(int id, string auth, bool refresh)
    {
        string json = " ";

        var url = string.Format(ApiURL.STATS_USER_LOSE, id);
        var www = ApiFormater.formatPatch(url, json, auth);

        yield return www.SendWebRequest();

        if (www.responseCode == 200)
        {
            // Call success callback 

            // Show results as text
            Debug.Log(www.downloadHandler.text);
        }
        else
        {
            if (refresh == false)
            {
                Debug.Log("Refresh token after error");

                json = JsonUtility.ToJson(new LoginData(loginReturn.user.username, loginReturn.user.password));
                www = ApiFormater.formatPost(ApiURL.REFRESH_URL, json);

                yield return www.SendWebRequest();

                if (www.responseCode == 200)
                {
                    TokenReturn token = JsonUtility.FromJson<TokenReturn>(www.downloadHandler.text);

                    GameObject.Find("NetworkManager").GetComponent<Variables>().loginReturn.jwt_token = token.jwt_token;

                    StartCoroutine(__AddLose(id, token.jwt_token, true));
                }
                else
                {
                    Debug.Log(www.error);
                }
            }
            else
            {
                // Call the error callback
                Debug.Log(www.error);
            }
        }
    }
    #endregion
    public void Defeated()
    {
        loginReturn = GameObject.Find("NetworkManager").GetComponent<Variables>().loginReturn;
        AddLose(loginReturn.user.id, loginReturn.jwt_token);
        InfoPopup popup = UIController.Instance.CreatePopup();
        LocalizedString message = new LocalizedString();
        message.TableReference = "Game Localization";
        message.TableEntryReference = "G_Defeat";
        popup.Initialize(UIController.Instance.MainCanvas, message.GetLocalizedString());
        

    }
    private void Victorious()
    {
        loginReturn = GameObject.Find("NetworkManager").GetComponent<Variables>().loginReturn;
        AddWin(loginReturn.user.id, loginReturn.jwt_token);
        InfoPopup popup = UIController.Instance.CreatePopup();
        LocalizedString message = new LocalizedString();
        message.TableReference = "Game Localization";
        message.TableEntryReference = "G_Victory";
        popup.Initialize(UIController.Instance.MainCanvas, message.GetLocalizedString());
    }

    public bool Disabled()
    {
        return disabled;
    }
}
