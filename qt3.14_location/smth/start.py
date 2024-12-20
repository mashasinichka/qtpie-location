from PyQt5 import QtWidgets
import st

d = {}
d[0] = 'США'
d[1] = 'КНДР'
d[2] = 'КНР'
d[3] = 'РФ'
d[4] = 'ЮАР'

s = {}
s[0] = 'доллар'
s[1] = 'евро'
s[2] = 'рубль'
s[3] = 'стерлинг'
s[4] = 'фунт'

f = {}
f[0] = 'миллиметр'
f[1] = 'сантиметр'
f[2] = 'дециметр'
f[3] = 'метр'
f[4] = 'километр'

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = st.Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.currentIndexChanged.connect(self.box)
        self.ui.comboBox_3.currentIndexChanged.connect(self.rf)
        self.ui.comboBox_2.currentIndexChanged.connect(self.rf)

    def convert(self):
        c = 0
        a = float(self.ui.lineEdit.text())

        if self.ui.comboBox.currentIndex() == 0 and self.ui.comboBox_2.currentIndex() == 0:
            c = a

        if self.ui.comboBox.currentIndex() == 1 and self.ui.comboBox_2.currentIndex() == 0:
            c = a * 105

        if self.ui.comboBox.currentIndex() == 2 and self.ui.comboBox_2.currentIndex() == 0:
            c = a * 100

        self.ui.lineEdit_2.setText(str(c))
    def box(self):
        self.ui.label_6.setText(str(d[self.ui.comboBox.currentIndex()]))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("ЛИТВИН КОНДЦИЙ НАБРАЛ")
    window.show()
    sys.exit(app.exec_())

