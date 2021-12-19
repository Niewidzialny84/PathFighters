using UnityEngine.Networking;
using System.Text;
public class ApiURL
{
    public static string URL = "http://molly.ovh:5001/";

    public static string REGISTER_URL = URL + "register";

    public static UnityWebRequest formatPost(string url, string json)
    {
        var www = new UnityWebRequest(url, "POST");
        byte[] bodyRaw = Encoding.UTF8.GetBytes(json);
        www.uploadHandler = (UploadHandler)new UploadHandlerRaw(bodyRaw);
        www.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        www.SetRequestHeader("Content-Type", "application/json");
        return www;
    }
}