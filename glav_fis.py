from PyQt5 import QtWidgets
import ks1, ks2, ks4

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = ks1.Ui_VT()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_glavnoe)
        self.ui.pushButton_2.clicked.connect(self.close_password)



    def open_glavnoe(self):
        if self.ui.lineEdit.text() == "Admin" and self.ui.lineEdit_2.text() == "Admin":
            pt.show()
            window.close()
        elif self.ui.lineEdit.text() == "":
            self.ui.label.setText("Введите логин")
        elif self.ui.lineEdit_2.text() == "":
            self.ui.label.setText("Введите пароль")
        else:
            Vt.show()
            window.close()
            
    
    def close_password(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()

    
class gs(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = ks2.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.back)

    def back(self):
        window.show()
        Vt.close()

class Window3(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = ks4.Ui_Form()
        self.ui.setupUi(self)
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    Vt = gs()
    pt = Window3()
    window.show()
    sys.exit(app.exec_())