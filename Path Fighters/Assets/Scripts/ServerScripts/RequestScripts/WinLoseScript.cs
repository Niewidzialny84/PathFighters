using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.Networking;

public class WinLoseScript : MonoBehaviour
{
    #region Win
    public void AddWin(int id, string auth)
    {
        StartCoroutine(__AddWin(id, auth));
    }

    private IEnumerator __AddWin(int id, string auth)
    {
        string json = null;

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
            // Call the error callback
            Debug.Log(www.error);
        }
    }
    #endregion

    #region Lose
    public void AddLose(int id, string auth)
    {
        StartCoroutine(__AddLose(id, auth));
    }

    private IEnumerator __AddLose(int id, string auth)
    {
        string json = null;

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
            // Call the error callback
            Debug.Log(www.error);
        }
    }
    #endregion
}