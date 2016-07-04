from PyQt4 import QtGui, QtCore
import sys
import subprocess
import design
import os
import filecmp
import hashlib
from glob import glob


ffmpeg = 'ffmpeg'
config = os.path.dirname(os.path.abspath(sys.argv[0])) + '/config.txt'
override = 'n'
output = ''

class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        global ffmpeg
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        if os.path.isfile(config):
            with open(config, "r") as fo:
                ffmpeg = fo.readline()
        try:
            subprocess.call([ffmpeg, '-v', '0'])
        except OSError:
            print ('ffmpeg is not installed -'
             'please set ffmpeg path in settings!')
            msgBox = QtGui.QMessageBox()
            msgBox.setText('FFmpeg is not installed - '
            'Please select the ffmpeg executable')
            ret = msgBox.exec_()
            ffmpeg = QtGui.QFileDialog.getOpenFileName(self, "FFMPEG EXECUTABLE") 
            if not os.path.isfile(config):
                with open(config, "w") as fo:
                    fo.write(ffmpeg)

        global container
        container = '.mkv'  # default - find out a better way of doing this, like 'if not x'
        self.batch_button.setEnabled(False)
        self.radioButton.setChecked(True)
        self.radioButton_2.toggled.connect(self.enable_button)
        self.radioButton.toggled.connect(self.enable_inputButton)
        self.checkBox_2.setChecked(True)
        directory = self.btnBrowse.clicked.connect(self.browse_folder)
        directory = self.batch_button.clicked.connect(self.browse_batch)
        self.btnBrowse.clicked.connect(self.update_dir)
        self.pushButton.clicked.connect(self.encode)
        output = self.pushButton_3.clicked.connect(self.override_output)
        self.pushButton_3.clicked.connect(self.update_output)
        self.container_selection.activated[str].connect(self.on_combo_activated)

    def enable_button(self):
        self.batch_button.setEnabled(True)
        self.btnBrowse.setEnabled(False)

    def enable_inputButton(self):
        self.batch_button.setEnabled(False)
        self.btnBrowse.setEnabled(True)

    def browse_folder(self):
        global directory
        directory = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
         '',"Video files (*.mov *.mov *.mxf *.avi *.mkv *.mp4 *.wmv *.webm *.ogg *.ogm) ;; All Files(*)")
        return directory

    def browse_batch(self):
        global directory
        directory = QtGui.QFileDialog.getExistingDirectory(self, 'Open Directory')
        return directory

    def override_output(self):
        global output
        global override
        output = QtGui.QFileDialog.getExistingDirectory(self, "Pick a file")
        override = 'y'
        return output

    def on_combo_activated(self):
        global container
        container = self.container_selection.currentText()

    def encode(self):
        global output
        if os.path.isfile(directory):
            print os.path.isfile(directory)
            print "single file found"
            video_files = []
            video_files.append(directory)
            print video_files

        elif os.path.isdir(directory):
            os.chdir(directory)
            video_files =  glob('*.mov') + glob('*.mp4') + glob('*.mxf') + glob('*.mkv') + glob('*.avi')
            print video_files
        for video in video_files:
            # Change this so that output will default if an entry isn't in override_output
            if override == 'n':
                output = str(video) + container

            elif override == 'y':
                print override

            source_framemd5 = video + '.framemd5'
            cmd = [str(ffmpeg),
                            '-i', str(video),
                            '-c:v', 'ffv1',
                            '-g', '1',
                            '-level', '3',
                            '-c:a', 'copy',
                            '-map', '0',
                            '-dn',
                            '-report',
                            '-slicecrc', '1',
                            '-slices', '16']

            if override == 'n':
                out = ''
                out += str(video) + container
                cmd += [str(out)]
            elif override == 'y':
                out = ''
                out += output + '/' + str(os.path.basename(str(directory))) + container
                cmd += [str(out)]
            if not self.checkBox.isChecked():
                cmd += ['-f', 'framemd5', '-an', str(source_framemd5)]
            print cmd
            try:
                if directory:
                    subprocess.call(cmd)
            except NameError:
                    msgBox = QtGui.QMessageBox()
                    msgBox.setText('Please select an input before encoding')
                    ret = msgBox.exec_()

            if not self.checkBox.isChecked():

                fmd5 = [str(ffmpeg), '-i', str(out), '-f', 'framemd5', '-an']
                if override == 'n':
                    fmd5output = ''
                    fmd5output += str(output) + '.framemd5'
                    print fmd5output
                    fmd5 += [fmd5output]
                elif override == 'y':
                    fmd5output = ''
                    fmd5output += str(output) + '/' + str(os.path.basename(str(out))) + '.framemd5'
                    fmd5 += [fmd5output]
                print fmd5
                subprocess.call(fmd5)

            global output_parent_dir
            global normpath
            global relative_path
            global dirname
            global manifest_destination
            output_parent_dir    = os.path.dirname(str(out))
            normpath             = os.path.normpath(str(out))
            relative_path        = normpath.split(os.sep)[-1]
            dirname              = os.path.split(os.path.basename(str(out)))[1]
            manifest_destination           = '%s_manifest.md5' % dirname

            if self.checkBox_2.isChecked():
                m = hashlib.md5()
                with open(str(out), 'rb') as f:
                    while True:
                        buf = f.read(2**20)
                        if not buf:
                            break
                        m.update(buf)
                md5_output = m.hexdigest()
                with open(manifest_destination, "wb") as fo:
                    fo.write(md5_output + '  ' + normpath.split(os.sep)[-1])

            if filecmp.cmp(source_framemd5, fmd5output, shallow=False):
                    print ('YOUR FILES ARE LOSSLESS'
                    ' YOU SHOULD BE SO HAPPY!!!')
                    msgBox = QtGui.QMessageBox()
                    msgBox.setText('Your transcode was lossless')
                    ret = msgBox.exec_()
            else:
                    msgBox = QtGui.QMessageBox()
                    msgBox.setText('Your transcode was not lossless')
                    ret = msgBox.exec_()
            print 'Encode process completed'

    def update_dir(self):
        self.filename_text.setText(directory)

    def update_output(self):
        self.lineEdit_2.setText(output)

def main():

    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app

if __name__ == '__main__':
    main()  # run the main function
