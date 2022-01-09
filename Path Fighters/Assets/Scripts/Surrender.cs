using System.Collections;
using UnityEngine;
using System;
using UnityEngine.Localization;
using UnityEngine.UI;
using UnityEngine.Events;
using TMPro;

public class Surrender : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        Action action = () =>
        {
            AcceptSurrender();
        };
        Button button = GetComponent<Button>();
        button.onClick.AddListener(() =>
        {
            YesNoPopup yesNoPopup = UIController.Instance.CreateYesNoPopup();
            
            LocalizedString title, leftButton, rightButton, oldPassword, text;
            title = new LocalizedString();
            leftButton = new LocalizedString();
            rightButton = new LocalizedString();
            text = new LocalizedString();

            title.TableReference = "Main Menu Text";
            title.TableEntryReference = "G_Surrender";

            leftButton.TableReference = "Main Menu Text";
            leftButton.TableEntryReference = "No";

            rightButton.TableReference = "Main Menu Text";
            rightButton.TableEntryReference = "Yes";

            text.TableReference = "Main Menu Text";
            text.TableEntryReference = "G_Surrender_Info";

            yesNoPopup.Init(UIController.Instance.MainCanvas, title.GetLocalizedString(), leftButton.GetLocalizedString(), rightButton.GetLocalizedString(), text.GetLocalizedString(), action);
        });
    }
    void AcceptSurrender()
    {

    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
