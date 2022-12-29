from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from view.ui_app_main import Ui_MainWindow as UI_App

##REVIEW - 
## in this section Eclat App class inherats QMainWindo and UI_App
## to display UI_App as UI
class EclatApp(QtWidgets.QMainWindow, UI_App):
    #NOTE -  in constractor we pass the class as Perent in super
    ## and setting ui using setupUI() method
    def __init__(self, parent=None):
        super(EclatApp, self).__init__(parent)
        ## set ui to initlize ui
        self.setupUi(self)
        ## set events to add events to ui
        self.setEvents()


def main():
    #set and show EclatApp as QApplication
    app = QApplication(sys.argv)
    form = EclatApp()
    form.show()
    app.exec_()

    

##SECTION - this is main method , compiler will execute this code and not look at the rest of the program
if __name__ == '__main__':
    #run main function
    main()

