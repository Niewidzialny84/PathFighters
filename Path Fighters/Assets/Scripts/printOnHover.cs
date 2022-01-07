using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.Localization;
public class printOnHover : MonoBehaviour
{
    [SerializeField] Entities _type;
    [SerializeField] TextMeshProUGUI _logField;
    // Start is called before the first frame update
   public void OnMouseExit()
    {
        _logField.text = "";
    }
    public void U_Goblin()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "U_Goblin";
        _logField.text = log.GetLocalizedString();
    }
    public void U_Crossbowman()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "U_Crossbowman";
        _logField.text = log.GetLocalizedString();
    }
    public void U_Knight()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "U_Knight";
        _logField.text = log.GetLocalizedString();
    }
    public void U_Elf()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "U_Elf";
        _logField.text = log.GetLocalizedString();
    }
    public void U_Orc()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "U_Orc";
        _logField.text = log.GetLocalizedString();
    }
    public void U_Dwarf()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "U_Dwarf";
        _logField.text = log.GetLocalizedString();
    }
    public void U_Wizard()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "U_Wizard";
        _logField.text = log.GetLocalizedString();
    }
    public void T_Delete()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "T_Delete";
        _logField.text = log.GetLocalizedString();
    }
    public void T_Archers()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "T_Archers";
        _logField.text = log.GetLocalizedString();
    }
    public void T_Investor()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "T_Investor";
        _logField.text = log.GetLocalizedString();
    }
    public void T_Balista()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "T_Balista";
        _logField.text = log.GetLocalizedString();
    }
    public void T_Catapult()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "T_Catapult";
        _logField.text = log.GetLocalizedString();
    }
    public void T_Necromancer()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "T_Necromancer";
        _logField.text = log.GetLocalizedString();
    }
    public void T_Warlock()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "T_Warlock";
        _logField.text = log.GetLocalizedString();
    }
    public void G_Language()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "G_Language";
        _logField.text = log.GetLocalizedString();
    }
    public void G_Surrender()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "G_Surrender";
        _logField.text = log.GetLocalizedString();
    }
    public void G_Master_Volume()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "G_Master_Volume";
        _logField.text = log.GetLocalizedString();
    }
    public void G_Music_Volume()
    {
        LocalizedString log = new LocalizedString();
        log.TableReference = "Game Localization";
        log.TableEntryReference = "G_Music_Volume";
        _logField.text = log.GetLocalizedString();
    }
    public void OnMouseOver()
    {
        switch (_type)
        {
            case Entities.Goblin:
              U_Goblin();
              break;
            case Entities.Crossbowman:
                U_Crossbowman();
                break;
            case Entities.Knight:
                U_Knight();
                break;
            case Entities.Elf:
                U_Elf();
                break;
            case Entities.Orc:
                U_Orc();
                break;
            case Entities.Dwarf:
                U_Dwarf();
                break;
            case Entities.Wizard:
                U_Wizard();
                break;
            case Entities.Delete_Tower:
                T_Delete();
                break;
            case Entities.Archers_Tower:
                T_Archers();
                break;
            case Entities.Investors_Tower:
                T_Investor();
                break;
            case Entities.Balista_Tower:
                T_Balista();
                break;
            case Entities.Catapult_Tower:
                T_Catapult();
                break;
            case Entities.Necromancer_Tower:
                T_Necromancer();
                break;
            case Entities.Warlock_Tower:
                T_Warlock();
                break;
            case Entities.Language:
                G_Language();
                break;
            case Entities.Surrender:
                G_Surrender();
                break;
            case Entities.Master_Volume:
                G_Master_Volume();
                break;
            case Entities.Music_Volume:
                G_Music_Volume();
                break;

        }

    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
public enum Entities
{
    Goblin,
    Crossbowman,
    Knight,
    Elf,
    Orc,
    Dwarf,
    Wizard,
    Delete_Tower,
    Archers_Tower,
    Investors_Tower,
    Balista_Tower,
    Catapult_Tower,
    Necromancer_Tower,
    Warlock_Tower,
    Language,
    Surrender,
    Master_Volume,
    Music_Volume
}
