import sys
from interface import *
from funcoes import gerador_chave, encriptar, desencriptar
from PyQt5.QtWidgets import QMainWindow, QApplication


class EncriptadorDescriptador(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_chave.clicked.connect(self.criar_chave)
        self.btn_encriptar.clicked.connect(self.encriptar)
        self.btn_decriptar.clicked.connect(self.descriptar)

    def verificar_chave_periodo(self):
        pass

    def criar_chave(self):
        chave = gerador_chave()
        text_chave = ''
        for c in chave:
            text_chave += str(c)
        self.input_chave.setText(text_chave)

    def encriptar(self):
        msg = self.input_msg.text()
        periodo = int(self.input_periodo.text())
        chave = []
        for c in self.input_chave.text():
            chave.append(c)

        msg_encriptada = encriptar(msg, chave, periodo)
        self.input_msg.setText(msg_encriptada)

    def descriptar(self):
        msg = self.input_msg.text()
        periodo = int(self.input_periodo.text())
        chave = []
        for c in self.input_chave.text():
            chave.append(c)
        msg_descriptada = desencriptar(msg, chave, periodo)
        self.input_msg.setText(msg_descriptada)


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    app = EncriptadorDescriptador()
    app.show()
    qt.exec_()
