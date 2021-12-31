using System;

[Serializable]
public class UserPasswordData
{
    public string password;

    public UserPasswordData(string password)
    {
        this.password = password;
    }
}