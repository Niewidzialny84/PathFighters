using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;
using System;
    
[System.Serializable]
public class Match {
    public string matchID;
    public bool publicMatch;
    public bool inMatch;
    public bool matchFull;
    public List<Player> players = new List<Player> ();

    public Match (string matchID, Player player, bool publicMatch) {
        matchFull = false;
        inMatch = false;
        this.matchID = matchID;
        this.publicMatch = publicMatch;
        players.Add (player);
    }

    public Match () { }
}