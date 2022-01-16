using UnityEngine.Networking;
using System.Text;
public class ForceAcceptAll : CertificateHandler
{
    protected override bool ValidateCertificate(byte[] certificateData)
    {
        return true;
    }
}
public class ApiFormater
{
    #region GET
    public static UnityWebRequest formatGet(string url, string auth)
    {
        var www = new UnityWebRequest(url, "GET");
        var cert = new ForceAcceptAll();
        www.certificateHandler = cert;
        www.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        www.SetRequestHeader("Authorization", "Bearer " + auth);
        return www;
    }
    #endregion

    #region POST
    public static UnityWebRequest formatPost(string url, string json)
    {

        var www = new UnityWebRequest(url, "POST");
        var cert = new ForceAcceptAll();
        www.certificateHandler = cert;
        byte[] bodyRaw = Encoding.UTF8.GetBytes(json);
        www.uploadHandler = (UploadHandler)new UploadHandlerRaw(bodyRaw);
        www.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        www.SetRequestHeader("Content-Type", "application/json");
        return www;
    }

        public static UnityWebRequest formatPost(string url, string json, string auth)
    {
        var www = new UnityWebRequest(url, "POST");
        var cert = new ForceAcceptAll();
        www.certificateHandler = cert;
        byte[] bodyRaw = Encoding.UTF8.GetBytes(json);
        www.uploadHandler = (UploadHandler)new UploadHandlerRaw(bodyRaw);
        www.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        www.SetRequestHeader("Authorization", "Bearer " + auth);
        www.SetRequestHeader("Content-Type", "application/json");
        return www;
    }
    #endregion

    #region PATCH
    public static UnityWebRequest formatPatch(string url, string json, string auth)
    {
        var www = new UnityWebRequest(url, "PATCH");
        var cert = new ForceAcceptAll();
        www.certificateHandler = cert;
        byte[] bodyRaw = Encoding.UTF8.GetBytes(json);
        www.uploadHandler = (UploadHandler)new UploadHandlerRaw(bodyRaw);
        www.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        www.SetRequestHeader("Content-Type", "application/json");
        www.SetRequestHeader("Authorization", "Bearer " + auth);
        return www;
    }
    #endregion

    #region DELETE
    public static UnityWebRequest formatDelete(string url, string auth)
    {
        var www = new UnityWebRequest(url, "DELETE");
        var cert = new ForceAcceptAll();
        www.certificateHandler = cert;
        www.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        www.SetRequestHeader("Authorization", "Bearer " + auth);
        return www;
    }
    #endregion
}