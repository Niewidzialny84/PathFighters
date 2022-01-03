using System;

[Serializable]
public class StatsReturn
{
    public int id;
    public int userid;
    public int total;
    public int fails;
    public int wins;

    public StatsReturn(int id, int userid, int total, int fails, int wins)
    {
        this.id = id;
        this.userid = userid;
        this.total = total;
        this.fails = fails;
        this.wins = wins;
    }
}