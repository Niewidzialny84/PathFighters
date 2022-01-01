using System.Collections;
using UnityEngine;
using UnityEngine.Events;
using Mirror;
using TMPro;

public class StatsScript : MonoBehaviour
{
    [SerializeField] private TextMeshProUGUI total = default;
    [SerializeField] private TextMeshProUGUI win = default;
    [SerializeField] private TextMeshProUGUI lose = default;

    private LoginReturn loginReturn;

    public void Start()
    {
        loginReturn = GameObject.Find("NetworkManager").GetComponent<Variables>().loginReturn;
        Debug.Log(loginReturn.user.id + " in stats script");
        if (loginReturn != null)
        {
            GetStats(loginReturn.user.id, loginReturn.jwt_token);
        }
    }

    public void SuccessHandler(StatsReturn msg)
    {
        Debug.Log("Stats Successful");

        total.text = msg.total.ToString();
        win.text = msg.wins.ToString();
        lose.text = msg.fails.ToString();
    }
    
    #region request
    public void GetStats(int id, string auth)
    {
        StartCoroutine(__GetStats(id, auth, false));
    }

    private IEnumerator __GetStats(int id, string auth, bool refresh)
    {
        var url = string.Format(ApiURL.STATS_USER_URL, id);
        var www = ApiFormater.formatGet(url, auth);

        yield return www.SendWebRequest();

        if (www.responseCode == 200)
        {
            StatsReturn stats = JsonUtility.FromJson<StatsReturn>(www.downloadHandler.text);

            SuccessHandler(stats);
            // Call success callback 
            Debug.Log(www.downloadHandler.text);
        }
        else
        {
            if(refresh == false)
            {
                Debug.Log("Refresh token after error");

                var json = JsonUtility.ToJson(new LoginData(loginReturn.user.username, loginReturn.user.password));
                www = ApiFormater.formatPost(ApiURL.REFRESH_URL, json);
                
                yield return www.SendWebRequest();

                if(www.responseCode == 200)
                {
                    TokenReturn token = JsonUtility.FromJson<TokenReturn>(www.downloadHandler.text);
                    
                    GameObject.Find("NetworkManager").GetComponent<Variables>().loginReturn.jwt_token = token.jwt_token;
                    
                    StartCoroutine(__GetStats(id, token.jwt_token, true));
                } else
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
}