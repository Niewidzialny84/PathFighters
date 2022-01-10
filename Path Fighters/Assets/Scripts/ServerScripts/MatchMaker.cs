using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;
using Mirror;
using UnityEngine;

    public class MatchMaker : NetworkBehaviour {

        public static MatchMaker instance;

        public readonly SyncList<Match> matches = new SyncList<Match> ();
        public readonly SyncList<String> matchIDs = new SyncList<String> ();

        [SerializeField] int maxMatchPlayers = 2;

        void Start () {
            if(instance == null)
            {
                instance = this;
            }
        }

        void Awake() {
            GameObject[] objs = GameObject.FindGameObjectsWithTag("MatchMaker");

            if (objs.Length > 1)
            {
                Destroy(this.gameObject);
            }

            DontDestroyOnLoad(this.gameObject);
        }

        public bool HostGame (string _matchID, Player _player, bool publicMatch, out int playerIndex) {
            playerIndex = -1;

            if (!matchIDs.Contains (_matchID)) {
                matchIDs.Add (_matchID);
                Match match = new Match (_matchID, _player, publicMatch);
                matches.Add (match);
                Debug.Log ($"Match generated");
                _player.currentMatch = match;
                playerIndex = 1;
                return true;
            } else {
                Debug.Log ($"Match ID already exists");
                return false;
            }
        }

        public bool JoinGame (string _matchID, Player _player, out int playerIndex) {
            playerIndex = -1;

            if (matchIDs.Contains (_matchID)) {

                for (int i = 0; i < matches.Count; i++) {
                    if (matches[i].matchID == _matchID) {
                        if (!matches[i].inMatch && !matches[i].matchFull) {
                            matches[i].players.Add (_player);
                            _player.currentMatch = matches[i];
                            playerIndex = matches[i].players.Count;

                            matches[i].players[0].PlayerCountUpdated (matches[i].players);

                            if (matches[i].players.Count == maxMatchPlayers) {
                                matches[i].matchFull = true;
                            }

                            break;
                        } else {
                            return false;
                        }
                    }
                }

                Debug.Log ($"Match joined");
                return true;
            } else {
                Debug.Log ($"Match ID does not exist");
                return false;
            }
        }

        public bool SearchGame (Player _player, out int playerIndex, out string matchID) {
            playerIndex = -1;
            matchID = "";

            for (int i = 0; i < matches.Count; i++) {
                Debug.Log ($"Checking match {matches[i].matchID} | inMatch {matches[i].inMatch} | matchFull {matches[i].matchFull} | publicMatch {matches[i].publicMatch}");
                if (!matches[i].inMatch && !matches[i].matchFull && matches[i].publicMatch) {
                    if (JoinGame (matches[i].matchID, _player, out playerIndex)) {
                        matchID = matches[i].matchID;
                        return true;
                    }
                }
            }

            return false;
        }

        public void BeginGame (string _matchID) {
            for (int i = 0; i < matches.Count; i++) {
                if (matches[i].matchID == _matchID) {
                    matches[i].inMatch = true;
                    foreach (var player in matches[i].players) {
                        player.StartGame ();
                    }
                    break;
                }
            }
        }

        public static string GetRandomMatchID () {
            string _id = string.Empty;
            for (int i = 0; i < 5; i++) {
                int random = UnityEngine.Random.Range (0, 36);
                if (random < 26) {
                    _id += (char) (random + 65);
                } else {
                    _id += (random - 26).ToString ();
                }
            }
            Debug.Log ($"Random Match ID: {_id}");
            return _id;
        }

        public void PlayerDisconnected (Player player, string _matchID) {
            for (int i = 0; i < matches.Count; i++) {
                if (matches[i].matchID == _matchID) {
                    int playerIndex = matches[i].players.IndexOf (player);
                    if (matches[i].players.Count > playerIndex) matches[i].players.RemoveAt (playerIndex);
                    Debug.Log ($"Player disconnected from match {_matchID} | {matches[i].players.Count} players remaining");

                    if (matches[i].players.Count == 0) {
                        Debug.Log ($"No more players in Match. Terminating {_matchID}");
                        matches.RemoveAt (i);
                        matchIDs.Remove (_matchID);
                    } else {
                        matches[i].players[0].PlayerCountUpdated (matches[i].players);
                    }
                    break;
                }
            }
        }

    }

    public static class MatchExtensions {
        public static Guid ToGuid (this string id) {
            MD5CryptoServiceProvider provider = new MD5CryptoServiceProvider ();
            byte[] inputBytes = Encoding.Default.GetBytes (id);
            byte[] hashBytes = provider.ComputeHash (inputBytes);

            return new Guid (hashBytes);
        }
    }
