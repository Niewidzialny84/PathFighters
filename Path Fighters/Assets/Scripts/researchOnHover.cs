using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.Localization;
public class researchOnHover : MonoBehaviour
{
    [SerializeField] Research _type;
    [SerializeField] TextMeshProUGUI _logField;
    // Start is called before the first frame update
    public void OnMouseExit()
    {
        _logField.text = "";
    }
    public void Unlock_Knight()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "Unlock_Knight";
        _logField.text = log.GetLocalizedString();
    }
    public void Unlock_Orc()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "Unlock_Orc";
        _logField.text = log.GetLocalizedString();
    }
    public void Unlock_Dwarf()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "Unlock_Dwarf";
        _logField.text = log.GetLocalizedString();
    }
    public void Unlock_Elf()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "Unlock_Elf";
        _logField.text = log.GetLocalizedString();
    }
    public void Unlock_Wizard()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "Unlock_Wizard";
        _logField.text = log.GetLocalizedString();
    }
    public void Upgrade_Warriors_Spirit()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "Upgrade_Warriors_Spirit";
        _logField.text = log.GetLocalizedString();
    }
    public void Upgrade_Looting_Upgrade()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "Upgrade_Looting_Upgrade";
        _logField.text = log.GetLocalizedString();
    }
    public void Upgrade_Goblins()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "Upgrade_Goblins";
        _logField.text = log.GetLocalizedString();
    }
    public void Unlock_Balista()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "Unlock_Balista";
        _logField.text = log.GetLocalizedString();
    }
    public void Unlock_Catapult()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "Unlock_Catapult";
        _logField.text = log.GetLocalizedString();
    }
    public void Unlock_Warlock()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "Unlock_Warlock";
        _logField.text = log.GetLocalizedString();
    }
    public void Unlock_Necromant()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "Unlock_Necromant";
        _logField.text = log.GetLocalizedString();
    }
    public void Upgrade_Income()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "Upgrade_Income";
        _logField.text = log.GetLocalizedString();
    }
    public void Unlock_Health()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "Unlock_Health";
        _logField.text = log.GetLocalizedString();
    }
 

    public void OnMouseOver()
    {
        switch (_type)
        {
            case Research.Unlock_Knight:
                Unlock_Knight();
                break;
            case Research.Unlock_Orc:
                Unlock_Orc();
                break;
            case Research.Unlock_Dwarf:
                Unlock_Dwarf();
                break;
            case Research.Unlock_Elf:
                Unlock_Elf();
                break;
            case Research.Unlock_Wizard:
                Unlock_Wizard();
                break;
            case Research.Uprgrade_Warriors_Spirit:
                Upgrade_Warriors_Spirit();
                break;
            case Research.Upgrade_Looting_Upgrade:
                Upgrade_Looting_Upgrade();
                break;
            case Research.Upgrade_Goblins:
                Upgrade_Goblins();
                break;
            case Research.Unlock_Balista:
                Unlock_Balista();
                break;
            case Research.Unlock_Catapult:
                Unlock_Catapult();
                break;
            case Research.Unlock_Warlock:
                Unlock_Warlock();
                break;
            case Research.Unlock_Necromant:
                Unlock_Necromant();
                break;
            case Research.Upgrade_Income:
                Upgrade_Income();
                break;
            case Research.Unlock_Health:
                Unlock_Health();
                break;

        }

    }
    // Update is called once per frame
    void Update()
    {

    }
}
public enum Research
{
    Unlock_Knight,
    Unlock_Orc,
    Unlock_Dwarf,
    Unlock_Elf,
    Unlock_Wizard,
    Uprgrade_Warriors_Spirit,
    Upgrade_Looting_Upgrade,
    Upgrade_Goblins,
    Unlock_Balista,
    Unlock_Catapult,
    Unlock_Warlock,
    Unlock_Necromant,
    Upgrade_Income,
    Unlock_Health

}
