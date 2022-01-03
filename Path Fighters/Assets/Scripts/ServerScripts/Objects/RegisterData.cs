using System;

[Serializable]
public class RegisterData
{
    public string username;
    public string email;
    public string password;

    public RegisterData(string username, string email, string password)
    {
        this.username = username;
        this.email = email;
        this.password = password;
    }
}