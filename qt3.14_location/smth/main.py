from PyQt5 import QtCore, QtWidgets
import vr

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = vr.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.P)
        self.ui.pushButton_2.clicked.connect(self.clear)



    def P(self):
        a = float(self.ui.lineEdit_2.text())
        b = float(self.ui.lineEdit_4.text())
        s = a * b // 2
        self.ui.label_4.setText(f"P = {str(s)}")
    def clear(self):
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit.clear()
        self.ui.label.setText(f"s = ")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("ЛИТВИН КОНДЦИЙ НАБРАЛ")
    window.resize(690, 440)
    window.show()
    sys.exit(app.exec_())