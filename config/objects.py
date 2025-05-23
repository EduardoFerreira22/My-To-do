from PySide6 import QtWidgets, QtCore, QtGui

def create_task_frame(parent, task_data):
    """
    Cria um frame para uma tarefa com base no modelo frm_model_color_task.
    
    Args:
        parent: Widget pai (geralmente scrollAreaWidgetContents).
        task_data: Dicionário com os dados da tarefa, ex: 
                   {"text": str, "category": str, "date": str, "completed": bool}.
    
    Returns:
        tuple: (frame_task, checkbox, title_label, category_label, date_label, button)
    """
    # Criar frame principal (equivalente a frm_model_color_task)
    frame_task = QtWidgets.QFrame(parent)
    frame_task.setMinimumSize(QtCore.QSize(0, 60))
    frame_task.setMaximumSize(QtCore.QSize(16777215, 60))
    frame_task.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    frame_task.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    
    # Layout vertical principal (verticalLayout_11)
    vertical_layout_11 = QtWidgets.QVBoxLayout(frame_task)
    vertical_layout_11.setContentsMargins(0, 0, 0, 4)
    
    # Frame interno (frame)
    frame = QtWidgets.QFrame(frame_task)
    frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    horizontal_layout_11 = QtWidgets.QHBoxLayout(frame)
    horizontal_layout_11.setContentsMargins(5, 3, 5, 3)
    
    # Frame para checkbox (frame_4)
    frame_4 = QtWidgets.QFrame(frame)
    frame_4.setMinimumSize(QtCore.QSize(40, 0))
    frame_4.setMaximumSize(QtCore.QSize(40, 16777215))
    frame_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
    frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    vertical_layout_16 = QtWidgets.QVBoxLayout(frame_4)
    vertical_layout_16.setSpacing(0)
    vertical_layout_16.setContentsMargins(0, 0, 0, 0)
    
    # Checkbox (checkBox_task_line)
    checkbox = QtWidgets.QCheckBox(frame_4)
    checkbox.setMinimumSize(QtCore.QSize(30, 0))
    checkbox.setMaximumSize(QtCore.QSize(30, 16777215))
    checkbox.setChecked(task_data.get("completed", False))
    vertical_layout_16.addWidget(checkbox, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
    horizontal_layout_11.addWidget(frame_4)
    
    # Frame para informações (frame_6)
    frame_6 = QtWidgets.QFrame(frame)
    frame_6.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
    frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    horizontal_layout_12 = QtWidgets.QHBoxLayout(frame_6)
    horizontal_layout_12.setContentsMargins(0, 0, 0, 0)
    
    # Frame para título e categoria (frame_13)
    frame_13 = QtWidgets.QFrame(frame_6)
    frame_13.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
    frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    vertical_layout_27 = QtWidgets.QVBoxLayout(frame_13)
    vertical_layout_27.setSpacing(4)
    vertical_layout_27.setContentsMargins(2, 0, 2, 0)
    
    # Label para título (lb_title_task)
    title_label = QtWidgets.QLabel(frame_13)
    title_label.setText(task_data.get("text", ""))
    vertical_layout_27.addWidget(title_label)
    
    # Label para categoria/prioridade (lb_categoria_prioridade_task)
    category_label = QtWidgets.QLabel(frame_13)
    category_label.setText(task_data.get("category", ""))
    vertical_layout_27.addWidget(category_label)
    
    horizontal_layout_12.addWidget(frame_13)
    
    # Frame para data (frame_14)
    frame_14 = QtWidgets.QFrame(frame_6)
    frame_14.setMinimumSize(QtCore.QSize(100, 0))
    frame_14.setMaximumSize(QtCore.QSize(100, 16777215))
    frame_14.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
    frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    vertical_layout_26 = QtWidgets.QVBoxLayout(frame_14)
    
    # Label para data (lb_data_task)
    date_label = QtWidgets.QLabel(frame_14)
    date_label.setText(task_data.get("date", ""))
    vertical_layout_26.addWidget(date_label)
    
    horizontal_layout_12.addWidget(frame_14)
    horizontal_layout_11.addWidget(frame_6)
    
    # Frame para botão (frame_7)
    frame_7 = QtWidgets.QFrame(frame)
    frame_7.setMinimumSize(QtCore.QSize(40, 0))
    frame_7.setMaximumSize(QtCore.QSize(40, 16777215))
    frame_7.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
    frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    vertical_layout_13 = QtWidgets.QVBoxLayout(frame_7)
    vertical_layout_13.setSpacing(0)
    vertical_layout_13.setContentsMargins(2, 0, 2, 0)
    
    # Botão (pushButton)
    button = QtWidgets.QPushButton(frame_7)
    button.setMinimumSize(QtCore.QSize(30, 30))
    button.setMaximumSize(QtCore.QSize(30, 30))
    icon = QtGui.QIcon()
    icon.addFile(":/imagens/share.png", QtCore.QSize(), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    button.setIcon(icon)
    button.setCheckable(True)
    button.setAutoExclusive(True)
    button.setAutoDefault(True)
    button.setFlat(True)
    vertical_layout_13.addWidget(button, 0, QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
    
    horizontal_layout_11.addWidget(frame_7)
    vertical_layout_11.addWidget(frame)
    
    return frame_task, checkbox, title_label, category_label, date_label, button