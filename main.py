from PyQt4 import QtGui, QtCore  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication
import subprocess
import design  # This file holds our MainWindow and all design related things

# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        #global directory

        directory = self.btnBrowse.clicked.connect(self.browse_folder)
        #directory = QtCore.QString(directory)
        self.btnBrowse.clicked.connect(self.update_dir)  # When the button is pressed
        
        self.pushButton.clicked.connect(self.encode)                                                    # Execute browse_folder function
        
    def browse_folder(self):
        #self.textBrowser.clear() # In case there are any existing elements in the list
        global directory
        directory = QtGui.QFileDialog.getOpenFileName(self,
                                                           "Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory
        
        return directory
    def encode(self):
        try:
              if directory: 
                    subprocess.call(['ffmpeg','-i', directory, '-c:v', 'ffv1', '-f', 'null','-']) # for all files, if any, in the directory    

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
