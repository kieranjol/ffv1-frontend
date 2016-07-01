from PyQt4 import QtGui, QtCore 
import sys
import subprocess
import design
import os
import filecmp
import hashlib

ffmpeg = 'ffmpeg'
config =  os.path.dirname(os.path.abspath(sys.argv[0])) + '/config.txt'

output = ''     
 
class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        global ffmpeg
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        if os.path.isfile(config):
            with open(config,"r") as fo:
                ffmpeg = fo.readline()
        try:
            subprocess.call([ffmpeg, '-v','0'])
        except OSError:
            print 'ffmpeg is not installed - please set ffmpeg path in settings!'
            msgBox = QtGui.QMessageBox()
            msgBox.setText('FFmpeg is not installed - Please select the ffmpeg executable')
            ret = msgBox.exec_() 
            
            ffmpeg = QtGui.QFileDialog.getOpenFileName(self, "FFMPEG EXECUTABLE") 
            if not os.path.isfile(config):
                 with open(config,"w") as fo: 
                     fo.write(ffmpeg)

        global container
        container = '.mkv' # default - find out a better way of doing this, like 'if not x'
        directory = self.btnBrowse.clicked.connect(self.browse_folder)
        #directory = QtCore.QString(directory)
        self.btnBrowse.clicked.connect(self.update_dir)
        self.pushButton.clicked.connect(self.encode)                                                    
        self.pushButton_3.clicked.connect(self.override_output) 
        self.pushButton_3.clicked.connect(self.update_output)
        self.container_selection.activated[str].connect(self.on_combo_activated)
        
    def browse_folder(self):
        global directory
        filters = "videos (*.mov *.mxf *.avi *.mkv *.mp4 *.wmv)"
        directory = QtGui.QFileDialog.getOpenFileName(self, "Pick a file", filters)
        return directory
    
    def override_output(self):
        #self.textBrowser.clear() # In case there are any existing elements in the list
        global output
        output = QtGui.QFileDialog.getExistingDirectory(self, "Pick a file")
        output  += '/' + str(os.path.basename(str(directory))) 
        
    def on_combo_activated(self):
        global container
        container = self.container_selection.currentText()
        
    def encode(self):
        global output
        print output
        # Change this so that output will default if an entry isn't in override_output
        if output == '':
            output = str(directory) + container
        else:
            output+= container
        source_framemd5 = directory + '.framemd5'
        output_framemd5 = output + '.framemd5'
        cmd = [str(ffmpeg),
                        '-i', str(directory), 
                        '-c:v', 'ffv1',
                        '-g','1',              # Use intra-frame only aka ALL-I aka GOP=1
                        '-level','3',          # Use Version 3 of FFv1
                        '-c:a','copy',         # Copy and paste audio bitsream with no transcoding
                        '-map','0',
                        '-dn',
                        '-report',
                        '-slicecrc', '1',
                        '-slices', '16',str(output)]
        if not self.checkBox.isChecked():
            cmd += ['-f','framemd5','-an',str(source_framemd5)]
        print cmd
        try:
              if directory: 
                    subprocess.call(cmd) 
        except NameError:
                msgBox = QtGui.QMessageBox()
                msgBox.setText('Please select an input before encoding')
                ret = msgBox.exec_() 

        if not self.checkBox.isChecked():
            fmd5 = [str(ffmpeg),'-i', str(output), '-f','framemd5', '-an',str(output_framemd5)]
            subprocess.call(fmd5)  
            
        global output_parent_dir
        global normpath 
        global relative_path
        global dirname
        global manifest_destination 
        output_parent_dir    = os.path.dirname(str(output))
        normpath             = os.path.normpath(str(output)) 
        relative_path        = normpath.split(os.sep)[-1]
        dirname              = os.path.split(os.path.basename(str(output)))[1]
        manifest_destination           = output_parent_dir + '/%s_manifest.md5' % dirname
        if self.checkBox_2.isChecked():
            m = hashlib.md5()
            with open(str(output),'rb') as f: 
               while True:
                    buf = f.read(2**20)
                    if not buf:
                        break
                    m.update( buf )
            md5_output = m.hexdigest()
            with open(manifest_destination,"wb") as fo:
                fo.write(md5_output + '  ' + normpath.split(os.sep)[-1] )
        
        if filecmp.cmp(source_framemd5, output_framemd5, shallow=False): 
                print "YOUR FILES ARE LOSSLESS YOU SHOULD BE SO HAPPY!!!"
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
    
if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
