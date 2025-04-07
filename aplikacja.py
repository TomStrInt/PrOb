import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMenu, QMenuBar, QToolBar, QLabel, QMessageBox
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QSize

class Quiz(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Harry Potter Quiz")
        self.resize(700, 800)

        # Statusbar
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Gotowy do pracy!")

        # Menu
        self.create_menu()

        # Toolbar
        self.create_toolbar()

    def create_menu(self):
        # Tworzenie QAction z ikonami, statusTip i skrótami klawiszowymi
        new_action = QAction(QIcon("icons/new.png"), "Nowy Quiz", self)
        new_action.setShortcut("Ctrl+N")
        new_action.setStatusTip("Rozpocznij nowy quiz")
        new_action.triggered.connect(self.new_quiz)

        exit_action = QAction(QIcon("icons/exit.png"), "Wyjście", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Zamknij aplikację")
        exit_action.triggered.connect(self.close)

        about_action = QAction(QIcon("icons/about.png"), "O programie", self)
        about_action.setStatusTip("Informacje o programie")
        about_action.triggered.connect(self.show_about)

        help_action = QAction(QIcon("icons/help.png"), "Pomoc", self)
        help_action.setShortcut("Ctrl+H")
        help_action.setStatusTip("Wyświetl pomoc")
        help_action.triggered.connect(self.show_help)

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("Plik")
        file_menu.addAction(new_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        help_menu = menu_bar.addMenu("Pomoc")
        help_menu.addAction(help_action)
        help_menu.addAction(about_action)

    def create_toolbar(self):
        # Toolbar
        toolbar = QToolBar("Główne opcje", self)
        toolbar.setIconSize(QSize(32, 32))
        self.addToolBar(Qt.LeftToolBarArea, toolbar)

        # Dodanie obiektów QAction do toolbara
        new_action = QAction(QIcon("icons/new.png"), "Nowy Quiz", self)
        new_action.setStatusTip("Rozpocznij nowy quiz")
        new_action.triggered.connect(self.new_quiz)

        exit_action = QAction(QIcon("icons/exit.png"), "Wyjście", self)
        exit_action.setStatusTip("Zamknij aplikację")
        exit_action.triggered.connect(self.close)

        toolbar.addAction(new_action)
        toolbar.addSeparator()
        toolbar.addAction(exit_action)

    def new_quiz(self):
        self.statusbar.showMessage("Nowy quiz rozpoczęty!")

    def show_about(self):
        QMessageBox.information(self, "O programie", "Harry Potter Quiz v1.0")

    def show_help(self):
        QMessageBox.information(self, "Pomoc", "To jest quiz dotyczący serii Harry Potter.")

# Uruchomienie aplikacji
app = QApplication(sys.argv)
quiz = Quiz()
quiz.show()
sys.exit(app.exec())
