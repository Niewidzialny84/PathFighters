using System.Collections;
using UnityEngine;
using UnityEngine.Events;

public class StatsScript : MonoBehaviour
{
    public void GetStats(int id, string auth)
    {
        StartCoroutine(__GetStats(id, auth));
    }

    private IEnumerator __GetStats(int id, string auth)
    {
        var url = string.Format(ApiURL.STATS_USER_URL, id);
        var www = ApiFormater.formatGet(url, auth);

        yield return www.SendWebRequest();

        if (www.responseCode == 200)
        {
            StatsReturn loginReturn = JsonUtility.FromJson<StatsReturn>(www.downloadHandler.text);
            
            // Call success callback 
            Debug.Log(www.downloadHandler.text);
        }
        else
        {
            // Call the error callback
            Debug.Log(www.error);
        }
    }
}