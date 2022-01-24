using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;

public class techScript : NetworkBehaviour
{

    public struct Upgrades
    {
        public bool goblinBuff;
        public bool attackBuff;
    }

    [SyncVar] public Upgrades player1;
    [SyncVar] public Upgrades player2;

    // Start is called before the first frame update
    void Start()
    {
        player1.attackBuff = false;
        player2.attackBuff = false;
        player1.goblinBuff = false;
        player2.goblinBuff = false;
    }
}
