# ffv1-gui
![GUI](https://raw.githubusercontent.com/kieranjol/ffv1-gui/master/screen.png)
# Installation
1. Download the windows file from here: https://github.com/kieranjol/ffv1-gui/releases/download/0.1/main.exe
2. If ffmpeg is not already installed, download a windows ffmpeg build from here: https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-latest-win64-static.zip
3. Unzip/Extract ffmpeg.exe from that zip file and place it somewhere on your computer.
4. If ffmpeg in not installed, a warning will pop up, followed by a prompt to select where ffmpeg.exe is located.
5. Make sure you select ffmpeg.exe when prompted. It is located wherever you stored it in step 3
6. Now that FFV1-GUI knows where ffmpeg is installed, select a file to transcode.
7. By default, FFV1-GUI creates a sidecar mkv file, but if you'd like to choose a different output directory, please select 'Select Output Directory'
8. A terminal window will pop up when transcoding, and when complete, you should find a new file next to your source file with the extension '.mkv'
<br>
Framemd5/md5/container selection/batch currently not working.


Future plans: Compile to exe/app and transcode from ffv1 -> prores/h264<br>



Code initially adapted from this great article (comments remain for now) https://nikolak.com/pyqt-qt-designer-getting-started/ <br>

many thanks to @euanc for help/inspiration: https://github.com/euanc/DiskFormatID
