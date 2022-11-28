from GUI.ui_Add_list import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow, QFileDialog

from time import strptime

from Proverka import proverka_dir
from Write_file import write_file

class SecondWindow(QMainWindow):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_clear_path.setEnabled(False)
        self.ui.pushButton_clear_name.setEnabled(False)
        self.ui.pushButton_clear_date.setEnabled(False)
        self.ui.pushButton_add_in_list.setEnabled(False)
        self.ui.pushButton_add_in_dict.setEnabled(False)
        self.ui.pushButton_load_data.setEnabled(False)
        self.ui.line_name.setEnabled(False)

        self.ui.pushButton_load_data.clicked.connect(self.load_data_in_date)
        self.ui.pushButton_path_dir.clicked.connect(self.path_folder)
        self.ui.pushButton_FAQ_path.clicked.connect(self.show_FAQ_path)
        self.ui.pushButton_FAQ_name.clicked.connect(self.show_FAQ_name)
        self.ui.pushButton_FAQ_date.clicked.connect(self.show_FAQ_date)
        self.ui.pushButton_exit.clicked.connect(QApplication.instance().quit)

        self.ui.line_path.textChanged.connect(lambda text: self.ui.pushButton_clear_path.setEnabled(bool(text)))
        self.ui.line_name.textChanged.connect(lambda text: self.ui.pushButton_clear_name.setEnabled(bool(text)))
        self.ui.line_date.textChanged.connect(lambda text: self.ui.pushButton_clear_date.setEnabled(bool(text)))
        self.ui.line_date.textChanged.connect(lambda text: self.ui.pushButton_load_data.setEnabled(bool(text)))

        self.dict_birth = {}
        self.file_name = "List_of_happy_birthdays"

    def save_spisok_in_file(self):
        path_dir = self.ui.line_path.text().strip()

        path_dir = proverka_dir(path_dir)

        write_file(self.dict_birth, self.file_name, path_dir)
        self.msg("Information", f"Файл сохранён!\nЗапомните местоположение: {path_dir}{self.file_name}.json")


    def add_in_list(self):
        flag_date = self.date_pulling()
        name = self.ui.line_name.text()

        if name == "":
            self.msg("Error", "Поле должно быть заполнено!")
            flag_name = False
        else:
            flag_name = True

        if flag_date and flag_name:
            list_birth = self.dict_birth.get(self.date, [])
            list_birth.append(name)
            self.dict_birth[self.date] = list_birth
            self.addItems_in_list(list_birth)
            self.ui.line_name.setText("")

    def addItems_in_list(self, items):
        self.ui.listWidget.addItems(items)

    def load_data_in_date(self):
        flag = self.date_pulling()

        if flag:
            list_birth = self.dict_birth.get(self.date, [])
            self.ui.label_info_names_in_date.setText(f"Количество записей: {str(len(list_birth))}")
            self.addItems_in_list(list_birth)

    def date_pulling(self):
        self.date = self.ui.line_date.text()
        
        if self.date == "":
            self.msg("Error", "Поле должно быть заполнено!")
        else:
            try:
                valid_date = strptime(self.date, '%d.%m')
                flag = True
                self.ui.line_name.setEnabled(True)
                return flag

            except:
                self.msg("Error", "Не верный формат даты!")
                flag = False
                self.ui.line_name.setEnabled(False)
                return flag
                
    def path_folder(self):
        path = QFileDialog.getExistingDirectory(self, "Select a folder")
        path = path.replace("/", "\\")
        self.ui.line_path.setText(path)

    def show_FAQ_name(self):
        self.msg("Information", "После ввода имени, вы можете:\n'Добавить к списку' - добавление имени к списку ко всем;\n'Сохранить список' - список добавленых имён сохняется на выбранную дату и записывается в файл.")

    def show_FAQ_date(self):
        self.msg("Information", "Нужно ввести день и месяц рождения.")

    def show_FAQ_path(self):
        self.msg("Information", "Для сохранения файла, нажмите \"...\", чтобы указать папку, где сохранить файл.\nЕсли оставить пустым, то файл появится возле программы.")

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