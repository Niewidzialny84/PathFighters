using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using UnityEngine.Localization;
using UnityEngine.UI;

public class deleteAccountPressed : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        Action action = () =>
        {
            DeleteAccount();
        };
        Button button = GetComponent<Button>();
        button.onClick.AddListener(() =>
        {
            SingleInputPopup doubleInput = UIController.Instance.CreateSingleInputPopup();
            LocalizedString title, leftButton, rightButton, password; 
            title = new LocalizedString();
            leftButton = new LocalizedString();
            rightButton = new LocalizedString();
      
            password = new LocalizedString();

            title.TableReference = "Main Menu Text";
            title.TableEntryReference = "SP_DeleteAccount";

            leftButton.TableReference = "Main Menu Text";
            leftButton.TableEntryReference = "DP_Cancel";

            rightButton.TableReference = "Main Menu Text";
            rightButton.TableEntryReference = "DP_Confirm";

            password.TableReference = "Main Menu Text";
            password.TableEntryReference = "SP_Password";


            doubleInput.Init(UIController.Instance.MainCanvas, title.GetLocalizedString(), leftButton.GetLocalizedString(), rightButton.GetLocalizedString(), password.GetLocalizedString(), action);
        });
    }
    void DeleteAccount()
    {
        Debug.Log("Account Deleted");
    }
    // Update is called once per frame
    void Update()
    {

    }
}
