using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Localization;
using TMPro;
using System.Text.RegularExpressions;

public class Register : MonoBehaviour
{
    [SerializeField] TextMeshProUGUI _login;
    [SerializeField] TextMeshProUGUI _email;
    [SerializeField] TextMeshProUGUI _confirm_email;
    [SerializeField] TextMeshProUGUI _password;
    [SerializeField] TextMeshProUGUI _confirm_password;
    // Start is called before the first frame update
    public void RegisterClick()
    {
        if(!CheckData())
        {
            InvalidData();
            return;
        }
        Success();
    }
    bool CheckData()
    {
        var email= _email.text.Remove(_email.text.Length-1);
        var password = _password.text.Remove(_password.text.Length - 1);
        var regex = @"\A(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)\Z";
        bool isValid = Regex.IsMatch(email, regex);
        if (_email.text != _confirm_email.text || !isValid)
        {
            return false;
        }
        if(_password.text != _confirm_password.text)
        {
            return false;
        }
        if (_email.text.Length==0 || _password.text.Length == 0|| _login.text.Length==0)
        {
            return false;
        }
        return true;
    }
    public void Success()
    {
        InfoPopup popup = UIController.Instance.CreatePopup();
        LocalizedString message = new LocalizedString();
        message.TableReference = "Main Menu Text";
        message.TableEntryReference = "Reg_PopupSuccess";
        popup.Init(UIController.Instance.MainCanvas, message.GetLocalizedString());

    }
    public void Fail()
    {
        InfoPopup popup = UIController.Instance.CreatePopup();
        LocalizedString message = new LocalizedString();
        message.TableReference = "Main Menu Text";
        message.TableEntryReference = "Reg_PopupFail";
        popup.Init(UIController.Instance.MainCanvas, message.GetLocalizedString());

    }
    public void InvalidData()
    {
        InfoPopup popup = UIController.Instance.CreatePopup();
        LocalizedString message = new LocalizedString();
        message.TableReference = "Main Menu Text";
        message.TableEntryReference = "Reg_InvalidData";
        popup.Init(UIController.Instance.MainCanvas, message.GetLocalizedString());

    }
}
