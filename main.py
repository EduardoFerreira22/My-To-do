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
from connections.connect import DBConnect
from config.objects import *
import json
import os

path_db = "Data/dados.db"
db = DBConnect(path=path_db)

class PrincipalWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(PrincipalWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("My To-Do")
        self.inicializadores()
        self.setup_buttons()
        self.tables_cresate()
        
        # Lista para armazenar os widgets de tarefas
        self.task_widgets = []
        
        # Carregar tarefas e popular a lista
        self.tasks = self.load_data()
        self.frame_task_list()
        
        # Conectar botões (exemplo)

        self.btn_excluir_task.clicked.connect(self.remove_task)
    def inicializadores(self):
        self.lb_titulo_superior_categoria.setVisible(False)
        self.line.setVisible(False)
        self.lb_data_titulo_superior.setVisible(False)
        self.frm_model_color_task.setVisible(False)
        self.frm_principal_rigth_task.setVisible(False)
        self.comboBox_status_task.setVisible(False)
        self.btn_atualizar_task.setVisible(False)
        self.date_selecionar_data_task.setDate(QDate.currentDate())
    

    def setup_buttons(self):
        data = self.data_create_task()
        self.btn_add_task.clicked.connect(self.add_task_frm)
        self.btn_salvar_new_task.clicked.connect(lambda: print(data))

    def add_task_frm(self):
        self.frm_principal_rigth_task.setVisible(True)

    def tables_cresate(self):
        try:
            db.create_tables()
        except:
            pass

    def data_create_task(self):
        # Váriaveis para Armazenar os dados da nova task
        descricao = self.txt_descricao_task.toPlainText()
        prioridade = self.cbx_select_prioridades.currentText()
        categoria = self.cbx_select_categoria.currentText()
        lembrar_data = self.date_selecionar_data_task.date().toString("dd-MM-yyyy")
        repetir_texto = self.cbx_repetir_task.currentText()
        observacoes = self.txt_observacoes_task.toPlainText()
        # Mapeamento de texto para número de dias
        mapa_repetir = {
            "Diáriamente": 1,
            "Semanalmente": 6,
            "Mensalmente": 30,
            "Anualmente": 360
        }
        repetir = mapa_repetir.get(repetir_texto, 0)# padrão: 0 = sem repetições
        #Dicionário que armazena o valor das variáveis par ser reutilizados em outras áreas do código.
        task_data = {
            "descricao": descricao,
            "prioridade": prioridade,
            "categoria": categoria,
            "data": lembrar_data,
            "repetir": repetir,
            "observacoes": observacoes
        }
        
        return task_data #Retorna o dicionário com os dados capturados.

    

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