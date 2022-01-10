using System;
using System.Collections;
using System.Collections.Generic;
using Mirror;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.Localization;

    [RequireComponent (typeof (NetworkMatch))]
    public class Player : NetworkBehaviour {

        public static Player localPlayer;
        [SyncVar] public string username;
        [SyncVar] public string matchID;
        [SyncVar] public int playerIndex;

        NetworkMatch networkMatch;

        [SyncVar] public Match currentMatch;

        Guid netIDGuid;

        void Awake () {
            networkMatch = GetComponent<NetworkMatch> ();

            GameObject[] objs = GameObject.FindGameObjectsWithTag("NetworkPlayer");

            if (objs.Length > 1)
            {
                Debug.Log("More than one player");
                //Destroy(this.gameObject);
            }

            DontDestroyOnLoad(this.gameObject);
        }

        public override void OnStartServer () {
            netIDGuid = netId.ToString ().ToGuid ();
            networkMatch.matchId = netIDGuid;
        }

        public override void OnStartClient () {
            Debug.Log($"OnStartClient {username}");
            if (isLocalPlayer) {
                localPlayer = this;
            } else {
                Debug.Log ($"Spawning other player UI Prefab");
                //playerLobbyUI = UILobby.instance.SpawnPlayerUIPrefab (this);
            }
        }

        public override void OnStopClient () {
            Debug.Log ($"Client Stopped {username}");
            ClientDisconnect ();
        }

        public override void OnStopServer () {
            Debug.Log ($"Client Stopped on Server {username}");
            ServerDisconnect ();
        }

        /* 
            HOST MATCH
        */

        public void HostGame (bool publicMatch) {
            string matchID = MatchMaker.GetRandomMatchID ();
            CmdHostGame (matchID, publicMatch);
        }

        [Command]
        void CmdHostGame (string _matchID, bool publicMatch) {
            matchID = _matchID;
            if (MatchMaker.instance.HostGame (_matchID, this, publicMatch, out playerIndex)) {
                Debug.Log ($"<color=green>Game hosted successfully</color>");
                networkMatch.matchId = _matchID.ToGuid ();
                TargetHostGame (true, _matchID, playerIndex);
            } else {
                Debug.Log ($"<color=red>Game hosted failed</color>");
                TargetHostGame (false, _matchID, playerIndex);
            }
        }

        [TargetRpc]
        void TargetHostGame (bool success, string _matchID, int _playerIndex) {
            playerIndex = _playerIndex;
            matchID = _matchID;
            Debug.Log ($"MatchID: {matchID} == {_matchID}");
            SceneManager.LoadScene("Lobby Scene");
        }

        /* 
            JOIN MATCH
        */

        public void JoinGame (string _inputID) {
            CmdJoinGame (_inputID);
        }

        [Command]
        void CmdJoinGame (string _matchID) {
            matchID = _matchID;
            if (MatchMaker.instance.JoinGame (_matchID, this, out playerIndex)) {
                Debug.Log ($"<color=green>Game Joined successfully</color>");
                networkMatch.matchId = _matchID.ToGuid ();
                TargetJoinGame (true, _matchID, playerIndex);

                //Host
                //if (isServer && playerLobbyUI != null) {
                //    playerLobbyUI.SetActive (true);
                //}
            } else {
                Debug.Log ($"<color=red>Game Joined failed</color>");
                TargetJoinGame (false, _matchID, playerIndex);
            }
        }

        [TargetRpc]
        void TargetJoinGame (bool success, string _matchID, int _playerIndex) {
            playerIndex = _playerIndex;
            matchID = _matchID;
            Debug.Log ($"MatchID: {matchID} == {_matchID}");
            //UILobby.instance.JoinSuccess (success, _matchID);

            if(success)
            {
                SceneManager.LoadScene("Lobby Scene");

            } else 
            {
                InfoPopup popup = UIController.Instance.CreatePopup();
                LocalizedString message = new LocalizedString();
                message.TableReference = "Main Menu Text";
                message.TableEntryReference = "Reg_InvalidData";
                popup.Init(UIController.Instance.MainCanvas, message.GetLocalizedString());
            }
        }

        /* 
            DISCONNECT
        */

        public void DisconnectGame () {
            CmdDisconnectGame ();
        }

        [Command]
        void CmdDisconnectGame () {
            ServerDisconnect ();
        }

        void ServerDisconnect () {
            MatchMaker.instance.PlayerDisconnected (this, matchID);
            RpcDisconnectGame ();
            networkMatch.matchId = netIDGuid;
        }

        [ClientRpc]
        void RpcDisconnectGame () {
            ClientDisconnect ();
        }

        void ClientDisconnect () {
            //if (playerLobbyUI != null) {
            //    if (!isServer) {
            //        Destroy (playerLobbyUI);
            //    } else {
            //        playerLobbyUI.SetActive (false);
            //    }
            //}
        }

        /* 
            SEARCH MATCH
        */

        public void SearchGame () {
            CmdSearchGame ();
        }

        [Command]
        void CmdSearchGame () {
            if (MatchMaker.instance.SearchGame (this, out playerIndex, out matchID)) {
                Debug.Log ($"<color=green>Game Found Successfully</color>");
                networkMatch.matchId = matchID.ToGuid ();
                TargetSearchGame (true, matchID, playerIndex);

                //Host
                //if (isServer && playerLobbyUI != null) {
                //    playerLobbyUI.SetActive (true);
                //}
            } else {
                Debug.Log ($"<color=red>Game Search Failed</color>");
                TargetSearchGame (false, matchID, playerIndex);
            }
        }

        [TargetRpc]
        void TargetSearchGame (bool success, string _matchID, int _playerIndex) {
            playerIndex = _playerIndex;
            matchID = _matchID;
            Debug.Log ($"MatchID: {matchID} == {_matchID} | {success}");
            UILobby.instance.SearchGameSuccess (success, _matchID);
        }

        /* 
            MATCH PLAYERS
        */

        [Server]
        public void PlayerCountUpdated (List<Player> players) {
            TargetPlayerCountUpdated (players);
        }

        [TargetRpc]
        void TargetPlayerCountUpdated (List<Player> players) {
            codeInit.instance.UpdatePlayers(players);
            //if (playerCount > 1) {
                //UILobby.instance.SetStartButtonActive(true);
            //} else {
                //UILobby.instance.SetStartButtonActive(false);
            //}
        }

        /* 
            BEGIN MATCH
        */

        public void BeginGame () {
            CmdBeginGame ();
        }

        [Command]
        void CmdBeginGame () {
            MatchMaker.instance.BeginGame (matchID);
            Debug.Log ($"<color=red>Game Beginning</color>");
        }

        public void StartGame () { //Server
            TargetBeginGame ();
        }

        [TargetRpc]
        void TargetBeginGame () {
            Debug.Log ($"MatchID: {matchID} | Beginning");
            //Additively load game scene
            //SceneManager.LoadScene ("SampleScene", LoadSceneMode.Additive);
            //SceneManager.LoadScene ("SampleScene");
            NetworkManager.singleton.ServerChangeScene ("SampleScene");
            
        }

        public void SpawnObj()
        {
            spawnObj();
        }

        [Command]
        void spawnObj()
        {
            Debug.Log("Spawnobj");
            // GameObject obj = Instantiate(NetworkManager.singleton.spawnPrefabs[19]);
            // GameObject[] objects = GameObject.FindGameObjectsWithTag("path");

            // foreach (GameObject p in objects)
            // {
            //     Debug.Log($"{p.name}");
            //     GameObject o = Instantiate(p.gameObject);
            //     NetworkServer.Spawn(o);
            // }
            GameObject prefab = NetworkManager.singleton.spawnPrefabs[19];
            Debug.Log($"{prefab.name}");
            float val = 3.5f;
            for (int i=1; i<=3;i++)
            {
                GameObject obj1 = Instantiate(prefab, new Vector3(0, val, 0), Quaternion.identity);
                Debug.Log($"{obj1.name}");
                NetworkServer.Spawn(obj1);
                val -= 2.0f;
            }
            //GameObject obj = Instantiate(Resources.Load("Prefabs/Path")) as GameObject;
            //Debug.Log($"Spawning {obj.name}");
            //NetworkServer.SpawnObjects();
            //NetworkServer.Spawn(obj.gameObject);


        }

        public void SpawnUnit(int unit, Vector3 pos, int player)
        {
            Debug.Log($"Spawnunit {unit}; {pos}; {player}");
            CmdSpawnUnit(unit, pos, player);
        }

        [Command]
        private void CmdSpawnUnit(int unit, Vector3 pos, int player)
        {
            // Debug.Log($"Spawning unit {unit.name}");
            GameObject o = NetworkManager.singleton.spawnPrefabs[unit];
            GameObject obj = Instantiate(o, pos, Quaternion.identity);
            Debug.Log($"Spawning unit {obj.name}");
            NetworkServer.Spawn(obj);
            abc(obj, player);
        }

        [ClientRpc]
        private void abc(GameObject o, int player)
        {
            Debug.Log($"{o.name}");
            try 
            {
                o.GetComponent<unitScript>().belongsToPlayer = player;
            } 
            catch (Exception e)
            {
                Debug.Log("Exception in abc as unitScript was null" + e.GetType());
            }
        }

        public static int getPrefabFromName(string name)
        {
            List<GameObject> prefabs = NetworkManager.singleton.spawnPrefabs;
            int i = 0;
            foreach (GameObject p in prefabs)
            {
                if (p.name == name)
                {
                    break;
                }
                i++;
            }
            return i;
        } 
    }
