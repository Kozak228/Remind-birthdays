from GUI.ui_Remind_main import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow, QFileDialog
from PyQt6.QtCore import QDate

from Proverka import proverka_file, proverka_dir
from Read_file import read_file

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_clear.setEnabled(False)

        self.ui.pushButton_exit.clicked.connect(QApplication.instance().quit)
        self.ui.calendarWidget.clicked[QDate].connect(self.show_date)
        self.ui.pushButton_FAQ_path.clicked.connect(self.show_FAQ_path)
        self.ui.pushButton_reload.clicked.connect(self.reload_exist)
        self.ui.pushButton_path_file.clicked.connect(self.path_folder)
        self.ui.line_path.textChanged.connect(lambda text: self.ui.pushButton_clear.setEnabled(bool(text)))

        self.file_name = "List_of_happy_birthdays"

        self.reload_exist()

        date = self.ui.calendarWidget.selectedDate().toString('dd.MM.yyyy')
        self.ui.label_info.setText(f"{date} отмечает День Рождение")

    def reload_exist(self):
        self.path_pulling()
        self.exists_file(self.file_name, self.path_file)
        self.read_with_file(self.file_name, self.path_file)

    def path_folder(self):
        path = QFileDialog.getExistingDirectory(self, "Select a folder")
        path = path.replace("/", "\\")
        self.ui.line_path.setText(path)

    def exists_file(self, file_name, file_path):
        if proverka_file(file_name, file_path):
            self.ui.label_exists_file.setText("Файл найден!")
            self.ui.label_exists_file.setStyleSheet("color: #00008B;")
        else:
            self.ui.label_exists_file.setText("Файл не найден!")
            self.ui.label_exists_file.setStyleSheet("color: #8B0000;")

    def read_with_file(self, file_name, file_path):
        try:
            self.dict_happy_birth = read_file(file_name, file_path)
        except:
            pass

    def path_pulling(self):
        self.path_file = self.ui.line_path.text().strip()
        self.path_file = proverka_dir(self.path_file)

    def show_date(self, date_witg):
        date = date_witg.toString("dd.MM")

        Name = {'15.10':"Худак Элеонора", '11.09':["Арутюнов Александр", "Bdf рппппав"], '13.04':"[Семёнов Влад]", 
        '09.01':"[Сухарков Гиви]", '08.03':"[Масановский Максим]", '14.12':"[Колесник Егор]", 
        '10.10':"[Палагута Оля]", '04.11':"[Паньков Даня]", '10.01':"[Панченко Евгений]"}

        self.ui.label_info.setText(f"{date_witg.toString('dd.MM.yyyy')} отмечает День Рождение")
        self.ui.listWidget.addItems(Name.get(date, []))

    def show_FAQ_path(self):
        self.msg("Information", "Если файл создан, но не находится с радом программой.\nНажмите \"...\", чтобы указать папку, где лежить файл")

    def msg(self, reson, message):
        msg = QMessageBox()
        if reson == "Error": 
            msg.setWindowTitle(reson)
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()

        if reson == "Information":
            msg.setWindowTitle(reson)
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()