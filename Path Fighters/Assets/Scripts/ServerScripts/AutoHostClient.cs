using System.Collections;
using System.Collections.Generic;
using Mirror;
using UnityEngine;

namespace MirrorBasics {
    public class AutoHostClient : MonoBehaviour {

        [SerializeField] NetworkManager networkManager;

        void Start () {
            if (!Application.isBatchMode) { //Headless build
                Debug.Log ($"=== Client Build ===");
                networkManager.StartClient ();
            } else {
                Debug.Log ($"=== Server Build ===");
            }
        }

        public void JoinLocal () {
            networkManager.networkAddress = "localhost";
            networkManager.StartClient ();
        }

    }
}