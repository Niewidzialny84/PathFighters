using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using UnityEngine.Localization;

public class changePassword : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        Action action = () =>
        {
            ChangePassword();
        };
        Button button = GetComponent<Button>();
        button.onClick.AddListener(() =>
        {
            DoubleInputPopup doubleInput = UIController.Instance.CreateDoubleInputPopup();
            LocalizedString title, leftButton, rightButton, oldPassword, newPassword;
            title = new LocalizedString();
            leftButton = new LocalizedString();
            rightButton = new LocalizedString();
            oldPassword = new LocalizedString();
            newPassword = new LocalizedString();

            title.TableReference = "Main Menu Text";
            title.TableEntryReference = "DP_ChangePassword";

            leftButton.TableReference = "Main Menu Text";
            leftButton.TableEntryReference = "DP_Cancel";

            rightButton.TableReference = "Main Menu Text";
            rightButton.TableEntryReference = "DP_Confirm";

            oldPassword.TableReference = "Main Menu Text";
            oldPassword.TableEntryReference = "DP_OldPass";

            newPassword.TableReference = "Main Menu Text";
            newPassword.TableEntryReference = "DP_NewPass";

            doubleInput.Init(UIController.Instance.MainCanvas, title.GetLocalizedString(), leftButton.GetLocalizedString(), rightButton.GetLocalizedString(), oldPassword.GetLocalizedString(), newPassword.GetLocalizedString(), action);
        });
    }
    void ChangePassword()
    {
        Debug.Log("Pressed Button");
    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
