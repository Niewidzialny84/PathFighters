using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class localTech : MonoBehaviour
{

    public struct Upgrades
    {
        public bool goblinBuff;
        public bool attackBuff;
    }

    public Upgrades player1;
    public Upgrades player2;

    // Start is called before the first frame update
    void Start()
    {
        player1.attackBuff = false;
        player2.attackBuff = false;
        player1.goblinBuff = false;
        player2.goblinBuff = false;
    }
}
