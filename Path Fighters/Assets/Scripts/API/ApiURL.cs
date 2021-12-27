using UnityEngine.Networking;
using System.Text;
public class ApiURL
{
    public static string URL = "http://molly.ovh:5001/";

    #region Login
    public static string LOGIN_URL = URL + "login";
    public static string LOGOUT_URL = URL + "logout";
    public static string REFRESH_URL = URL + "refresh";
    public static string REGISTER_URL = URL + "register";
    #endregion

    #region User
    public static string USER_ALL_URL = URL + "user";
    public static string USER_URL = USER_ALL_URL + "/id/{0}";
    #endregion

    #region Stats
    public static string STATS_URL = URL + "stats";
    public static string STATS_USER_URL = STATS_URL + "/{0}";
    public static string STATS_USER_WIN = STATS_USER_URL + "/add-win";
    public static string STATS_USER_LOSE = STATS_USER_URL + "/add-fail";
    #endregion

    public static LoginReturn currentLoginReturn;

    public static UnityWebRequest formatGet(string url, string auth)
    {
        var www = new UnityWebRequest(url, "GET");
        www.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        www.SetRequestHeader("Authorization", "Bearer " + auth);
        return www;
    }

    public static UnityWebRequest formatPost(string url, string json)
    {
        var www = new UnityWebRequest(url, "POST");
        byte[] bodyRaw = Encoding.UTF8.GetBytes(json);
        www.uploadHandler = (UploadHandler)new UploadHandlerRaw(bodyRaw);
        www.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        www.SetRequestHeader("Content-Type", "application/json");
        return www;
    }

    public static UnityWebRequest formatPatch(string url, string json, string auth)
    {
        var www = new UnityWebRequest(url, "PATCH");
        byte[] bodyRaw = Encoding.UTF8.GetBytes(json);
        www.uploadHandler = (UploadHandler)new UploadHandlerRaw(bodyRaw);
        www.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        www.SetRequestHeader("Content-Type", "application/json");
        www.SetRequestHeader("Authorization", "Bearer " + auth);
        return www;
    }

    public static UnityWebRequest formatDelete(string url, string auth)
    {
        var www = new UnityWebRequest(url, "DELETE");
        www.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        www.SetRequestHeader("Authorization", "Bearer " + auth);
        return www;
    }
}