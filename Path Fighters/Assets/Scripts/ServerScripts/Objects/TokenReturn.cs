using System;

[Serializable]
public class TokenReturn 
{
    public string jwt_token;

    public TokenReturn(string jwt_token)
    {
        this.jwt_token = jwt_token;
    }

}