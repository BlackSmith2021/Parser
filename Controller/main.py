from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QBasicTimer
import sys  # sys нужен для передачи argv в QApplication
from Model.informerYaInf import Pars_inf
from view.window_pars import Ui_MainWindow


pars = Pars_inf()

class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, start):
        super().__init__()
        self.start = start
        self.setupUi(self)  # для инициализации дизайна
        self.timer = QBasicTimer()
        self.timer.start(1000, self)

    def starts(self):
        self.label_date.setText(pars.getInf_day())
        self.label_wind.setText(pars.getInf_wind())
        self.label_level.setText(pars.getInf_level())
        self.lcdNumber.display(pars.getInf_temperature())
        self.lcdNumber_2.display(pars.getInf_time())

    def timerEvent(self, e):
        print(pars.getInf_time())
        self.label_date.setText(pars.getInf_day())
        self.label_wind.setText(pars.getInf_wind())
        self.label_level.setText(pars.getInf_level())
        self.lcdNumber.display(pars.getInf_temperature())
        self.lcdNumber_2.display(pars.getInf_time())

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp(pars)  # Создаём объект класса ExampleApp
    window.starts()
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
