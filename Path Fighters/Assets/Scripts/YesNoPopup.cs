using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Localization;
using TMPro;
using System;

public class YesNoPopup : MonoBehaviour
{
   
    [SerializeField] Button _leftButton;
    [SerializeField] Button _rightButton;
    [SerializeField] Text _popupName;
    [SerializeField] Text _leftButtonName;
    [SerializeField] Text _rightButtonName;
    [SerializeField] TextMeshProUGUI _firstInput;

    // Start is called before the first frame update
    public void Init(Transform canvas, string title, string leftButton, string rightButton, string text, Action action)
    {
        _popupName.text = title;
        _leftButtonName.text = leftButton;
        _rightButtonName.text = rightButton;
        _firstInput.text = text;
        transform.SetParent(canvas);
        transform.localScale = Vector3.one;
        GetComponent<RectTransform>().offsetMin = Vector2.zero;
        GetComponent<RectTransform>().offsetMax = Vector2.zero;
        _leftButton.onClick.AddListener(() => {
            GameObject.Destroy(this.gameObject);
        });
        _rightButton.onClick.AddListener(() => {
            action();
            GameObject.Destroy(this.gameObject);
        });
    }


}
