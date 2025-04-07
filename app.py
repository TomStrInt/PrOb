import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout, QLabel,
    QRadioButton, QCheckBox, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QSize
import unicodedata

def stylizuj_tekst(tekst):
    return f"<div style='border: 2px solid #ff8c00; color:black; padding:10px;'><b>{tekst}</b></div>"

def normalize_text(text):
    text = unicodedata.normalize("NFKD", text)
    text = "".join([c for c in text if not unicodedata.combining(c)])
    return " ".join(text.split()).lower()

class Quiz(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Harry Potter Quiz")
        self.resize(700, 800)

        # Tworzenie interfejsu
        self.create_quiz_layout()

        # Dodanie menu
        self.create_menu()

        # Dodanie toolbara
        self.create_toolbar()

        # Dodanie statusbara
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Gotowy do pracy!")

    def create_quiz_layout(self):
        """Tworzenie układu quizu"""
        scroll_area = QScrollArea()
        self.central_widget = QWidget()
        scroll_area.setWidget(self.central_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("background-color: #2c2f33;")
        self.setCentralWidget(scroll_area)

        self.main_layout = QVBoxLayout()

        # Pytanie 1
        q1_layout = QVBoxLayout()
        self.q1_label = QLabel(stylizuj_tekst("1. Jak nazywa się najlepszy przyjaciel Harry'ego Pottera?"))
        self.q1_radio1 = QRadioButton("Ron Weasley")
        self.q1_radio2 = QRadioButton("Draco Malfoy")
        self.q1_radio3 = QRadioButton("Neville Longbottom")
        self.q1_radios = [self.q1_radio1, self.q1_radio2, self.q1_radio3]

        q1_layout.addWidget(self.q1_label)
        for radio in self.q1_radios:
            q1_layout.addWidget(radio)
        self.main_layout.addLayout(q1_layout)

        # Pytanie 2
        q2_layout = QVBoxLayout()
        self.q2_label = QLabel(stylizuj_tekst("2. Kto był nauczycielem eliksirów w Hogwarcie?"))
        self.q2_checkbox1 = QCheckBox("Severus Snape")
        self.q2_checkbox2 = QCheckBox("Minerva McGonagall")
        self.q2_checkbox3 = QCheckBox("Rubeus Hagrid")
        self.q2_checkboxes = [self.q2_checkbox1, self.q2_checkbox2, self.q2_checkbox3]

        q2_layout.addWidget(self.q2_label)
        for checkbox in self.q2_checkboxes:
            q2_layout.addWidget(checkbox)
        self.main_layout.addLayout(q2_layout)

        # Pytanie 3
        q3_layout = QVBoxLayout()
        self.q3_label = QLabel(stylizuj_tekst("3. Jakiego patronusa ma Harry Potter?"))
        self.q3_correct_label = QLabel("")
        self.q3_correct_label.setStyleSheet("color: green; font-style: italic;")
        self.q3_input = QLineEdit()
        self.q3_input.setPlaceholderText("Wpisz odpowiedź...")

        q3_layout.addWidget(self.q3_label)
        q3_layout.addWidget(self.q3_correct_label)
        q3_layout.addWidget(self.q3_input)
        self.main_layout.addLayout(q3_layout)

        # Przycisk Sprawdź
        footer_layout = QHBoxLayout()
        self.check_button = QPushButton("Sprawdź")
        self.check_button.clicked.connect(self.sprawdzenie_odp)
        footer_layout.addWidget(self.check_button)
        self.main_layout.addLayout(footer_layout)

        self.central_widget.setLayout(self.main_layout)

    def create_menu(self):
        """Tworzenie menu"""
        new_action = QAction(QIcon("icons/new.png"), "Nowy Quiz", self)
        new_action.setShortcut("Ctrl+N")
        new_action.setStatusTip("Rozpocznij nowy quiz")
        new_action.triggered.connect(self.nowy_quiz)

        exit_action = QAction(QIcon("icons/exit.png"), "Wyjście", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Zamknij aplikację")
        exit_action.triggered.connect(self.close)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("Plik")
        file_menu.addAction(new_action)
        file_menu.addAction(exit_action)

    def create_toolbar(self):
        """Tworzenie toolbara"""
        toolbar = self.addToolBar("Opcje")
        toolbar.setIconSize(QSize(32, 32))

        new_action = QAction(QIcon("icons/new.png"), "Nowy Quiz", self)
        new_action.setStatusTip("Rozpocznij nowy quiz")
        new_action.triggered.connect(self.nowy_quiz)

        exit_action = QAction(QIcon("icons/exit.png"), "Wyjście", self)
        exit_action.setStatusTip("Zamknij aplikację")
        exit_action.triggered.connect(self.close)

        toolbar.addAction(new_action)
        toolbar.addSeparator()
        toolbar.addAction(exit_action)

    def nowy_quiz(self):
        """Przywraca oryginalny quiz"""
        self.menuBar().hide()
        self.toolBar().hide()
        self.statusbar.hide()

        # Wyczyszczenie głównego layoutu i ponowne załadowanie quizu
        self.central_widget.deleteLater()
        self.create_quiz_layout()

    def sprawdzenie_odp(self):
        """Sprawdzenie odpowiedzi użytkownika"""
        QMessageBox.information(self, "Wynik", "Quiz zakończony!")
