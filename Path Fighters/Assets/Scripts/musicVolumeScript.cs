using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Audio;

public class musicVolumeScript : MonoBehaviour
{
    [SerializeField] private AudioMixer audioMixer;

    public void VolumeSlider(float volume)
    {
        audioMixer.SetFloat("masterVolume", Mathf.Log10(volume) * 20);
    }
}
