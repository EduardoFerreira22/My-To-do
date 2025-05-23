from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QComboBox,
    QDateEdit, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

from ui.ui_main import Ui_MainWindow
from config.objects import *
import json
import os

class PrincipalWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(PrincipalWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("My To-Do")
        self.frm_model_color_task.setVisible(False)
        self.frm_principal_rigth_task.setVisible(False)
        # Lista para armazenar os widgets de tarefas
        self.task_widgets = []
        
        # Carregar tarefas e popular a lista
        self.tasks = self.load_data()
        self.frame_task_list()
        
        # Conectar botões (exemplo)
        self.btn_add_task.clicked.connect(self.add_task)
        self.btn_excluir_task.clicked.connect(self.remove_task)

    def frame_task_list(self):
            """Popula a lista de tarefas com frames dinâmicos."""
            # Limpar o layout atual
            for frame, _, _, _, _, _ in self.task_widgets:
                self.verticalLayout_list_tasks.removeWidget(frame)
                frame.deleteLater()
            self.task_widgets.clear()
            
            # Criar e adicionar frames para cada tarefa
            for task in self.tasks:
                frame, checkbox, title_label, category_label, date_label, button = create_task_frame(
                    self.scrollAreaWidgetContents, task
                )
                self.verticalLayout_list_tasks.addWidget(frame, 0, Qt.AlignmentFlag.AlignTop)
                self.task_widgets.append((frame, checkbox, title_label, category_label, date_label, button))
                # Conectar sinais (exemplo)
                button.clicked.connect(lambda checked, t=task: print(f"Botão clicado: {t['text']}"))
                checkbox.stateChanged.connect(self.save_data)
            
            # Adicionar um spacer para alinhar ao topo
            self.verticalLayout_list_tasks.addStretch()
    
    def add_task(self):
        """Adiciona uma tarefa fictícia (adaptar para sua lógica)."""
        task_data = {
            "text": "Nova Tarefa",
            "category": "Urgente",
            "date": QDate.currentDate().toString("yyyy-MM-dd"),
            "completed": False
        }
        self.tasks.append(task_data)
        self.frame_task_list()
        self.save_data()
    
    def remove_task(self):
        """Remove tarefas selecionadas."""
        selected_frames = [f for f, cb, _, _, _, _ in self.task_widgets if cb.isChecked()]
        if selected_frames:
            for frame in selected_frames:
                index = [f for f, _, _, _, _, _ in self.task_widgets].index(frame)
                self.tasks.pop(index)
                self.task_widgets[index][0].deleteLater()
                self.task_widgets.pop(index)
            self.frame_task_list()
            self.save_data()
    
    def save_data(self):
        """Salva as tarefas no arquivo JSON."""
        for i, (frame, checkbox, _, _, _, _) in enumerate(self.task_widgets):
            self.tasks[i]["completed"] = checkbox.isChecked()
        with open("tasks.json", "w") as f:
            json.dump({"tasks": self.tasks}, f, indent=4)
    
    def load_data(self):
        """Carrega as tarefas do arquivo JSON."""
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as f:
                data = json.load(f)
                return data.get("tasks", [])
        return []

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)  # Crie a instância de QApplication
    window = PrincipalWindow()
    window.show()
    sys.exit(app.exec())  # Execute o loop de eventos e finalize o programa corretamente