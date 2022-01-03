using System;

[Serializable]
public class UserData
{
    public int id;
    public string username;
    public string email;
    public string password;

    public UserData(int id, string username, string email, string password)
    {
        this.id = id;
        this.username = username;
        this.email = email;
        this.password = password;
    }

    public UserData()
    {
        this.id = 0;
        this.username = "";
        this.email = "";
        this.password = "";
    }
}