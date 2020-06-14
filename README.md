<h1 align="center">screenRec


[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-electricity.svg)](https://forthebadge.com)

</h1>

<h5 align="center">Yet another screen recorder.
<br>

<br>

## usage

Select the upper left corner and the lower right corner of the image to be captured.
Click to continue.

__s :__ save screenshot

**r :** start recording video

**q :** quit

<br>

## features
* **GUI** lets you select grab any part of the screen for recording/snapping


![screenshot of GUI](/Images/screenshotGUI.jpg)


* **Silent Capture** captures screenshots after specified amount of time without bringing up any interface


![screenshot of CLI](/Images/screenshotCLI.png)


<br>

## optional arguments
` -h, --help`

Shows help

` -sc, --silentcapture`

Just capture the screenshot without opening the interface in stealth mode 😎

` -vn VIDEONAME, --videoname VIDEONAME`<br>
` -in IMAGENAME, --imagename IMAGENAME`

Change the name of image/video to be saved

` -fhd, --fullhd`

Capture in full HD, 1920x1080. Default is 1366x768

` -s SLEEP, --sleep sleep`

Open the program after SLEEP seconds

Combine `-s SLEEP` and `-sc` to capture silently after specified time

<br>

## author

Karthikeshwar
