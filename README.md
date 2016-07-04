# ffv1-gui
# Features:
Frontend GUI that performs the following actions: <br>

1. Transcode either a single file, or all files in a folder to FFV1 level 3 with the option of MKV/MOV/AVI containers.
2. Generate frame level checksums for the source and ffv1 transcode (framemd5).
3. Lossless verification by comparing the frame level checksums of the source and output.
4. Generate a whole file .md5 manifest for the FFV1 output.
5. Generate verbose ffmpeg log files for the transcode and framemd5 generation.

![GUI](https://raw.githubusercontent.com/kieranjol/ffv1-gui/master/screen.png)
# Installation

1. If ffmpeg is not already installed, download a ffmpeg build from here: <br>
 WINDOWS: https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-latest-win64-static.zip <br>
 MAC: http://www.ffmpegmac.net/
2. WINDOWS: Unzip/Extract ffmpeg.exe (it may just be called 'ffmpeg' depending on your windows settings) from that zip file and place it somewhere on your computer. ffmpeg will be in the /bin subfolder. <br>
  MAC: Unzip/extract ffmpeg from the zip file.
3. Download the latest ffv1-gui release from here:
   <br>WINDOWS: https://github.com/kieranjol/ffv1-gui/releases/download/v0.3.1-beta/ffv1gui_windows_binary_v0.3.1_beta.exe <br> MAC: https://github.com/kieranjol/ffv1-gui/releases/download/v0.3.1-beta/ffv1gui_macosx_binary_v0.3.1_beta
4. If ffmpeg in not installed, a warning will pop up, followed by a prompt to select where ffmpeg is located.
5. Make sure you select the ffmpeg executable when prompted. It is located wherever you stored it in step 3
6. Now that FFV1-GUI knows where ffmpeg is installed, select a file to transcode.
7. By default, FFV1-GUI creates a sidecar mkv file, but if you'd like to choose a different output directory, please select 'Select Output Directory'
8. A terminal window will pop up when transcoding, and when complete, you should find a new file next to your source file with the extension '.mkv'
<br>

#Details:

1. GUI is generated using py-qt.
2. Binaries created with pyinstaller
3. The FFV1 files have the following features: Intra Frame, Version 3, embedded framecrc checksums.

Future plans: Compile to exe/app and transcode from ffv1 -> prores/h264<br>

Code initially adapted from this great article (comments remain for now) https://nikolak.com/pyqt-qt-designer-getting-started/ <br>

many thanks to @euanc for help/inspiration: https://github.com/euanc/DiskFormatID
b
