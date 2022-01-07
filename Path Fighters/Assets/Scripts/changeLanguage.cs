using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Localization;
using TMPro;
using UnityEngine.Localization.Settings;
using System;

public class changeLanguage : MonoBehaviour
{
    [SerializeField] Sprite _gbSprite;
    [SerializeField] Sprite _plSprite;
    [SerializeField] Button _button;
    [SerializeField] TMP_Dropdown _dropdown;
    // Start is called before the first frame update
    IEnumerator Start()
    {
        yield return LocalizationSettings.InitializationOperation;
        int english, polish;
        english = polish = -1;
      
        for (int i = 0; i < LocalizationSettings.AvailableLocales.Locales.Count; i++)
        {
            if (LocalizationSettings.AvailableLocales.Locales[i].ToString() == "Polish (Poland) (pl-PL)")
            {
                polish = i;
            }
            if (LocalizationSettings.AvailableLocales.Locales[i].ToString() == "English (United Kingdom) (en-GB)")
            {
                english = i;
            }
        }
        if (_dropdown != null)
        {
            try
            {
               
                if (LocalizationSettings.SelectedLocale == LocalizationSettings.AvailableLocales.Locales[polish])
                {
                    Debug.Log(_dropdown.value);
                    _dropdown.value = 1;
                    Debug.Log(_dropdown.value);
                    Debug.Log("Wrong");
                }
                else if (LocalizationSettings.SelectedLocale == LocalizationSettings.AvailableLocales.Locales[english])
                {
                    Debug.Log(_dropdown.value);
                    _dropdown.value = 0;
                    Debug.Log(_dropdown.value);
                    Debug.Log("English");
                }
            }
            catch (ArgumentOutOfRangeException e)
            {
                Debug.LogWarning("Language import error");
            }
        }
        else
        {
            if (LocalizationSettings.SelectedLocale == LocalizationSettings.AvailableLocales.Locales[polish])
            {
                _button.image.sprite = _plSprite;
            }
            else if (LocalizationSettings.SelectedLocale == LocalizationSettings.AvailableLocales.Locales[english])
            {
                _button.image.sprite = _gbSprite;
            }
        }
       
    }
    public void ChangeDropdownLanguage()
    {
        int english, polish;
        english = polish = -1;
        for (int i = 0; i < LocalizationSettings.AvailableLocales.Locales.Count; i++)
        {
            if (LocalizationSettings.AvailableLocales.Locales[i].ToString() == "Polish (Poland) (pl-PL)")
            {
                polish = i;
            }
            if (LocalizationSettings.AvailableLocales.Locales[i].ToString() == "English (United Kingdom) (en-GB)")
            {
                english = i;
            }
        }
        try
        {
            if (LocalizationSettings.SelectedLocale == LocalizationSettings.AvailableLocales.Locales[polish] && _dropdown.value==0)
            {
                LocalizationSettings.SelectedLocale = LocalizationSettings.AvailableLocales.Locales[english];
            }
            else if (LocalizationSettings.SelectedLocale == LocalizationSettings.AvailableLocales.Locales[english]&&_dropdown.value == 1)
            {
                LocalizationSettings.SelectedLocale = LocalizationSettings.AvailableLocales.Locales[polish];
            }
        }
        catch (ArgumentOutOfRangeException e)
        {
            Debug.LogWarning("Language import error");
        }


    }
    public void ChangeLanguage()
    {
        int english, polish;
        english = polish = -1;
        for (int i=0;i< LocalizationSettings.AvailableLocales.Locales.Count; i++)
        {
            if (LocalizationSettings.AvailableLocales.Locales[i].ToString() == "Polish (Poland) (pl-PL)")
            {
                polish = i;
            }
            if( LocalizationSettings.AvailableLocales.Locales[i].ToString() == "English (United Kingdom) (en-GB)")
            {
                english = i;
            }
        }
        try
        {
            if (LocalizationSettings.SelectedLocale == LocalizationSettings.AvailableLocales.Locales[polish])
            {
                LocalizationSettings.SelectedLocale = LocalizationSettings.AvailableLocales.Locales[english];
                _button.image.sprite = _gbSprite;

            }
            else if (LocalizationSettings.SelectedLocale == LocalizationSettings.AvailableLocales.Locales[english])
            {
                LocalizationSettings.SelectedLocale = LocalizationSettings.AvailableLocales.Locales[polish];
                _button.image.sprite = _plSprite;
            }
        }
        catch(IndexOutOfRangeException e)
        { 
            Debug.LogWarning("Language import error");
        }
       

    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
