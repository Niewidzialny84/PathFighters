using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Localization;
using TMPro;
using System;
using UnityEngine.SceneManagement;
public class InfoPopup : MonoBehaviour
{
    [SerializeField] Button _okButton;
    [SerializeField] Text _okButtonText;
    [SerializeField] TextMeshProUGUI _popupText;


    // Start is called before the first frame update
    public void Init(Transform canvas, string localized)
    {
        _okButtonText.text = "OK";
        _popupText.text = localized;
        transform.SetParent(canvas);
        transform.localScale = Vector3.one;
        GetComponent<RectTransform>().offsetMin = Vector2.zero;
        GetComponent<RectTransform>().offsetMax = Vector2.zero;
        _okButton.onClick.AddListener(() => { GameObject.Destroy(this.gameObject); });
    }
    public void Initialize(Transform canvas, string localized)
    {
        _okButtonText.text = "OK";
        _popupText.text = localized;
        transform.SetParent(canvas);
        transform.localScale = Vector3.one;
        transform.localScale = new Vector3(0.01f, 0.01f, 0.01f);
        GetComponent<RectTransform>().offsetMin = Vector2.zero;
        GetComponent<RectTransform>().offsetMax = Vector2.zero;
        _okButton.onClick.AddListener(() => { 
            SceneManager.LoadScene("Main Menu");
            GameObject.Destroy(this.gameObject); });
    }
    public void Ehhhh(Transform canvas, string localized)
    {
        _okButtonText.text = "OK";
        _popupText.text = localized;
        transform.SetParent(canvas);
        transform.localScale = Vector3.one;
        GetComponent<RectTransform>().offsetMin = Vector2.zero;
        GetComponent<RectTransform>().offsetMax = Vector2.zero;
        _okButton.onClick.AddListener(() => {
            SceneManager.LoadScene("Main Menu");
            GameObject.Destroy(this.gameObject);
        });
    }


}
