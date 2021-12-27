using System;

[Serializable]
public class LoginReturn {
    public UserData user;

    public string jwt_token;

    public LoginReturn(UserData user, string jwt_token) {
        this.user = user;
        this.jwt_token = jwt_token;
    }
}