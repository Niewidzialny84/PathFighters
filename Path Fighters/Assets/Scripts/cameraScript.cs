using UnityEngine;
using System.Collections.Generic;

public class cameraScript : MonoBehaviour
{
    private int screenSizeX = 0;
    private int screenSizeY = 0;

    private void rescaleCamera()
    {

        if (Screen.width == screenSizeX && Screen.height == screenSizeY) return;

        float targetaspect = 16.0f / 9.0f;
        float windowaspect = (float)Screen.width / (float)Screen.height;
        float scaleheight = windowaspect / targetaspect;
        Camera camera = GetComponent<Camera>();

        if (scaleheight < 1.0f)
        {
            Rect rect = camera.rect;

            rect.width = 1.0f;
            rect.height = scaleheight;
            rect.x = 0;
            rect.y = (1.0f - scaleheight) / 2.0f;

            camera.rect = rect;
        }
        else
        {
            float scalewidth = 1.0f / scaleheight;

            Rect rect = camera.rect;

            rect.width = scalewidth;
            rect.height = 1.0f;
            rect.x = (1.0f - scalewidth) / 2.0f;
            rect.y = 0;

            camera.rect = rect;
        }

        screenSizeX = Screen.width;
        screenSizeY = Screen.height;
    }

    // Use this for initialization
    void Start()
    {
        rescaleCamera();
    }

    // Update is called once per frame
    void Update()
    {
        rescaleCamera();
    }
}
