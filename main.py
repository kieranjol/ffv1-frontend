from PyQt4 import QtGui, QtCore 
import sys
import subprocess
import design
import os


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        try:
            subprocess.call(['ffmpeg', '-v','0'])
        except OSError:
            print 'ffmpeg is not installed!'
            msgBox = QtGui.QMessageBox()
            msgBox.setText('FFmpeg is not installed!')
            ret = msgBox.exec_()   
        global container
        container = '.mkv' # default - find out a better way of doing this, like 'if not x'
        
        print container, '111111111111111111111'
        directory = self.btnBrowse.clicked.connect(self.browse_folder)
        #directory = QtCore.QString(directory)
        self.btnBrowse.clicked.connect(self.update_dir)
        self.pushButton.clicked.connect(self.encode)                                                    
        
        self.container_selection.activated[str].connect(self.on_combo_activated)
    def browse_folder(self):
        #self.textBrowser.clear() # In case there are any existing elements in the list
        global directory
        directory = QtGui.QFileDialog.getOpenFileName(self,
                                                           "Pick a file")
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory
        
        return directory
    
    def on_combo_activated(self):
        global container
        container = self.container_selection.currentText()
        print container    
    def encode(self):
       
            
            
            
        print container, 5343
        try:
              if directory: 
                    subprocess.call(['ffmpeg','-i', str(directory), '-c:v', 'ffv1', '-f', 'null','-']) # for all files, if any, in the directory    

        except NameError:
                msgBox = QtGui.QMessageBox()
                msgBox.setText('Please select an input before encoding')
                ret = msgBox.exec_()    
    def update_dir(self):

        self.filename_text.setText(directory)# add file to the listWidget
def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app
    

if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
