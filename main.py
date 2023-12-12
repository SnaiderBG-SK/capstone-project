from PyQt5 import QtWidgets, QtCore, QtGui
from MainWindow import Ui_MainWindow
from gpt import ChatGPT
import sys 

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.chat = ChatGPT()
        self.ui.submitButton.clicked.connect(self.onSubmitButtonpressed)
        self.textBrowsers = [self.ui.task1TextBrowser, self.ui.task2TextBrowser, self.ui.task3TextBrowser]
        self.labels = [self.ui.task1Label, self.ui.task2Label, self.ui.task3Label]
        self.index = 0
    
    def onSubmitButtonpressed(self):
        response = self.chat.summarize_and_breakdown(self.ui.plainTextEdit.toPlainText())
        self.ui.plainTextEdit.setPlainText("")
        self.index = self.index % len(self.labels)
        breakdown_text = '\n'.join(response['breakdown']) 
        self.labels[self.index].setText(response['summary'])
        self.textBrowsers[self.index].setText(breakdown_text)
        self.index += 1

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main)
    # widget.addWidget(dbWin)
    widget.show()
    sys.exit(app.exec_())