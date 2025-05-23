# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainRoijqW.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCalendarWidget, QCheckBox,
    QComboBox, QDateEdit, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)
from icons import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1240, 867)
        MainWindow.setStyleSheet(u"#btn_close_frmRigth {\n"
"	border:none;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"\n"
"}\n"
"#btn_close_frmRigth QPushButton:hover {\n"
"	border:none;\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	background-color: rgba(226, 226, 226, 0.20);\n"
"	border: 1px solid rgba(109, 109, 109, 0.30);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frm_principal_left = QFrame(self.centralwidget)
        self.frm_principal_left.setObjectName(u"frm_principal_left")
        self.frm_principal_left.setMinimumSize(QSize(300, 0))
        self.frm_principal_left.setMaximumSize(QSize(300, 16777215))
        self.frm_principal_left.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_principal_left.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frm_principal_left)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frm_principal_left)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 250))
        self.frame_5.setMaximumSize(QSize(16777215, 250))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.calendarWidget = QCalendarWidget(self.frame_5)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.calendarWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.calendarWidget.setFirstDayOfWeek(Qt.DayOfWeek.Monday)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)

        self.verticalLayout_3.addWidget(self.calendarWidget)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frm_principal_prioridades = QFrame(self.frm_principal_left)
        self.frm_principal_prioridades.setObjectName(u"frm_principal_prioridades")
        self.frm_principal_prioridades.setMinimumSize(QSize(0, 0))
        self.frm_principal_prioridades.setMaximumSize(QSize(16777215, 16777215))
        self.frm_principal_prioridades.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_principal_prioridades.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frm_principal_prioridades)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frm_titulo_prioridades = QFrame(self.frm_principal_prioridades)
        self.frm_titulo_prioridades.setObjectName(u"frm_titulo_prioridades")
        self.frm_titulo_prioridades.setMinimumSize(QSize(0, 40))
        self.frm_titulo_prioridades.setMaximumSize(QSize(16777215, 40))
        self.frm_titulo_prioridades.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_titulo_prioridades.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frm_titulo_prioridades)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 0, 5, 0)
        self.lb_titulo_prioridades = QLabel(self.frm_titulo_prioridades)
        self.lb_titulo_prioridades.setObjectName(u"lb_titulo_prioridades")

        self.horizontalLayout_8.addWidget(self.lb_titulo_prioridades)


        self.verticalLayout_17.addWidget(self.frm_titulo_prioridades, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_list_prioridades = QVBoxLayout()
        self.verticalLayout_list_prioridades.setObjectName(u"verticalLayout_list_prioridades")

        self.verticalLayout_17.addLayout(self.verticalLayout_list_prioridades)


        self.verticalLayout_2.addWidget(self.frm_principal_prioridades)

        self.frm_principal_categorias = QFrame(self.frm_principal_left)
        self.frm_principal_categorias.setObjectName(u"frm_principal_categorias")
        self.frm_principal_categorias.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_principal_categorias.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frm_principal_categorias)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frm_titulo_categorias = QFrame(self.frm_principal_categorias)
        self.frm_titulo_categorias.setObjectName(u"frm_titulo_categorias")
        self.frm_titulo_categorias.setMinimumSize(QSize(0, 40))
        self.frm_titulo_categorias.setMaximumSize(QSize(16777215, 40))
        self.frm_titulo_categorias.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_titulo_categorias.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frm_titulo_categorias)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.lb_titulo_categorias = QLabel(self.frm_titulo_categorias)
        self.lb_titulo_categorias.setObjectName(u"lb_titulo_categorias")

        self.horizontalLayout_6.addWidget(self.lb_titulo_categorias)

        self.btn_addNew_categoria = QPushButton(self.frm_titulo_categorias)
        self.btn_addNew_categoria.setObjectName(u"btn_addNew_categoria")
        self.btn_addNew_categoria.setMinimumSize(QSize(35, 35))
        self.btn_addNew_categoria.setMaximumSize(QSize(35, 35))
        icon = QIcon()
        icon.addFile(u":/imagens/bookmark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_addNew_categoria.setIcon(icon)
        self.btn_addNew_categoria.setIconSize(QSize(20, 20))
        self.btn_addNew_categoria.setCheckable(True)
        self.btn_addNew_categoria.setChecked(False)
        self.btn_addNew_categoria.setAutoExclusive(True)
        self.btn_addNew_categoria.setAutoDefault(True)
        self.btn_addNew_categoria.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btn_addNew_categoria)


        self.verticalLayout_14.addWidget(self.frm_titulo_categorias, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_list_categorias = QVBoxLayout()
        self.verticalLayout_list_categorias.setObjectName(u"verticalLayout_list_categorias")

        self.verticalLayout_14.addLayout(self.verticalLayout_list_categorias)


        self.verticalLayout_2.addWidget(self.frm_principal_categorias)

        self.frm_button_info_left = QFrame(self.frm_principal_left)
        self.frm_button_info_left.setObjectName(u"frm_button_info_left")
        self.frm_button_info_left.setFrameShape(QFrame.Shape.NoFrame)
        self.frm_button_info_left.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.frm_button_info_left)


        self.horizontalLayout.addWidget(self.frm_principal_left)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 80))
        self.frame_12.setMaximumSize(QSize(16777215, 80))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lb_titulo_superior_categoria = QLabel(self.frame_12)
        self.lb_titulo_superior_categoria.setObjectName(u"lb_titulo_superior_categoria")

        self.verticalLayout_15.addWidget(self.lb_titulo_superior_categoria)

        self.line = QFrame(self.frame_12)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_15.addWidget(self.line)

        self.lb_data_titulo_superior = QLabel(self.frame_12)
        self.lb_data_titulo_superior.setObjectName(u"lb_data_titulo_superior")

        self.verticalLayout_15.addWidget(self.lb_data_titulo_superior)


        self.horizontalLayout_7.addLayout(self.verticalLayout_15)

        self.btn_add_task = QPushButton(self.frame_12)
        self.btn_add_task.setObjectName(u"btn_add_task")
        self.btn_add_task.setMinimumSize(QSize(40, 40))
        self.btn_add_task.setMaximumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u":/imagens/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_add_task.setIcon(icon1)
        self.btn_add_task.setIconSize(QSize(20, 20))
        self.btn_add_task.setCheckable(True)
        self.btn_add_task.setChecked(False)
        self.btn_add_task.setAutoExclusive(True)
        self.btn_add_task.setAutoDefault(True)
        self.btn_add_task.setFlat(True)

        self.horizontalLayout_7.addWidget(self.btn_add_task, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_10.addWidget(self.frame_12)

        self.scrollArea = QScrollArea(self.frame_8)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 594, 695))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_list_tasks = QVBoxLayout()
        self.verticalLayout_list_tasks.setSpacing(2)
        self.verticalLayout_list_tasks.setObjectName(u"verticalLayout_list_tasks")
        self.frm_model_color_task = QFrame(self.scrollAreaWidgetContents)
        self.frm_model_color_task.setObjectName(u"frm_model_color_task")
        self.frm_model_color_task.setMinimumSize(QSize(0, 60))
        self.frm_model_color_task.setMaximumSize(QSize(16777215, 60))
        self.frm_model_color_task.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_model_color_task.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frm_model_color_task)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 4)
        self.frame = QFrame(self.frm_model_color_task)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 3, 5, 3)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(30, 0))
        self.frame_4.setMaximumSize(QSize(30, 16777215))
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_4)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.checkBox_task_line = QCheckBox(self.frame_4)
        self.checkBox_task_line.setObjectName(u"checkBox_task_line")

        self.verticalLayout_16.addWidget(self.checkBox_task_line, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_11.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_13)
        self.verticalLayout_27.setSpacing(4)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(2, 0, 2, 0)
        self.lb_title_task = QLabel(self.frame_13)
        self.lb_title_task.setObjectName(u"lb_title_task")

        self.verticalLayout_27.addWidget(self.lb_title_task)

        self.lb_categoria_prioridade_task = QLabel(self.frame_13)
        self.lb_categoria_prioridade_task.setObjectName(u"lb_categoria_prioridade_task")

        self.verticalLayout_27.addWidget(self.lb_categoria_prioridade_task)


        self.horizontalLayout_12.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(100, 0))
        self.frame_14.setMaximumSize(QSize(100, 16777215))
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_14)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.lb_data_task = QLabel(self.frame_14)
        self.lb_data_task.setObjectName(u"lb_data_task")

        self.verticalLayout_26.addWidget(self.lb_data_task)


        self.horizontalLayout_12.addWidget(self.frame_14)


        self.horizontalLayout_11.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(40, 0))
        self.frame_7.setMaximumSize(QSize(40, 16777215))
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_7)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(2, 0, 2, 0)
        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/imagens/share.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setFlat(True)

        self.verticalLayout_13.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_11.addWidget(self.frame_7)


        self.verticalLayout_11.addWidget(self.frame)


        self.verticalLayout_list_tasks.addWidget(self.frm_model_color_task, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_12.addLayout(self.verticalLayout_list_tasks)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)


        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frm_principal_rigth_task = QFrame(self.frame_3)
        self.frm_principal_rigth_task.setObjectName(u"frm_principal_rigth_task")
        self.frm_principal_rigth_task.setMinimumSize(QSize(300, 0))
        self.frm_principal_rigth_task.setMaximumSize(QSize(300, 16777215))
        self.frm_principal_rigth_task.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_principal_rigth_task.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frm_principal_rigth_task)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 5, -1, -1)
        self.frame_17 = QFrame(self.frm_principal_rigth_task)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 30))
        self.frame_17.setMaximumSize(QSize(16777215, 30))
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(4, 0, 4, 0)
        self.lb_titulo_data_frmRigth = QLabel(self.frame_17)
        self.lb_titulo_data_frmRigth.setObjectName(u"lb_titulo_data_frmRigth")

        self.horizontalLayout_13.addWidget(self.lb_titulo_data_frmRigth, 0, Qt.AlignmentFlag.AlignRight)

        self.btn_close_frmRigth = QPushButton(self.frame_17)
        self.btn_close_frmRigth.setObjectName(u"btn_close_frmRigth")
        self.btn_close_frmRigth.setMinimumSize(QSize(30, 30))
        self.btn_close_frmRigth.setMaximumSize(QSize(30, 30))
        self.btn_close_frmRigth.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/imagens/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_close_frmRigth.setIcon(icon3)

        self.horizontalLayout_13.addWidget(self.btn_close_frmRigth, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_4.addWidget(self.frame_17)

        self.frame_9 = QFrame(self.frm_principal_rigth_task)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_9)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_feito = QCheckBox(self.frame_9)
        self.checkBox_feito.setObjectName(u"checkBox_feito")
        self.checkBox_feito.setMinimumSize(QSize(0, 35))
        self.checkBox_feito.setMaximumSize(QSize(16777215, 35))
        self.checkBox_feito.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_feito.setIconSize(QSize(16, 16))
        self.checkBox_feito.setCheckable(True)
        self.checkBox_feito.setChecked(False)
        self.checkBox_feito.setTristate(False)

        self.horizontalLayout_5.addWidget(self.checkBox_feito)

        self.comboBox_status_task = QComboBox(self.frame_9)
        self.comboBox_status_task.addItem("")
        self.comboBox_status_task.addItem("")
        self.comboBox_status_task.addItem("")
        self.comboBox_status_task.setObjectName(u"comboBox_status_task")
        self.comboBox_status_task.setMinimumSize(QSize(150, 30))
        self.comboBox_status_task.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_5.addWidget(self.comboBox_status_task)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame_9)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignmentFlag.AlignBottom)

        self.txt_descricao_task = QTextEdit(self.frame_9)
        self.txt_descricao_task.setObjectName(u"txt_descricao_task")
        self.txt_descricao_task.setMinimumSize(QSize(0, 50))
        self.txt_descricao_task.setMaximumSize(QSize(16777215, 50))
        self.txt_descricao_task.setTabChangesFocus(True)
        self.txt_descricao_task.setOverwriteMode(True)

        self.verticalLayout_5.addWidget(self.txt_descricao_task, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_8.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignBottom)

        self.cbx_select_prioridades = QComboBox(self.frame_9)
        self.cbx_select_prioridades.setObjectName(u"cbx_select_prioridades")
        self.cbx_select_prioridades.setMinimumSize(QSize(0, 30))
        self.cbx_select_prioridades.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_8.addWidget(self.cbx_select_prioridades, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignBottom)

        self.cbx_select_categoria = QComboBox(self.frame_9)
        self.cbx_select_categoria.setObjectName(u"cbx_select_categoria")
        self.cbx_select_categoria.setMinimumSize(QSize(0, 30))
        self.cbx_select_categoria.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_7.addWidget(self.cbx_select_categoria, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)


        self.verticalLayout_25.addLayout(self.verticalLayout_9)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frm_principal_rigth_task)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.frame_10)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 264, 184))
        self.verticalLayout_24 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.btn_adicionar_meu_dia = QPushButton(self.layoutWidget)
        self.btn_adicionar_meu_dia.setObjectName(u"btn_adicionar_meu_dia")
        self.btn_adicionar_meu_dia.setMinimumSize(QSize(260, 35))
        self.btn_adicionar_meu_dia.setMaximumSize(QSize(260, 35))
        self.btn_adicionar_meu_dia.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/imagens/sunny-day.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_adicionar_meu_dia.setIcon(icon4)
        self.btn_adicionar_meu_dia.setIconSize(QSize(25, 25))
        self.btn_adicionar_meu_dia.setCheckable(True)
        self.btn_adicionar_meu_dia.setAutoExclusive(True)
        self.btn_adicionar_meu_dia.setAutoDefault(True)
        self.btn_adicionar_meu_dia.setFlat(True)

        self.verticalLayout_20.addWidget(self.btn_adicionar_meu_dia)

        self.btn_lembrar_me = QPushButton(self.layoutWidget)
        self.btn_lembrar_me.setObjectName(u"btn_lembrar_me")
        self.btn_lembrar_me.setMinimumSize(QSize(260, 35))
        self.btn_lembrar_me.setMaximumSize(QSize(260, 35))
        self.btn_lembrar_me.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_lembrar_me.setMouseTracking(False)
        icon5 = QIcon()
        icon5.addFile(u":/imagens/alarm-clock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_lembrar_me.setIcon(icon5)
        self.btn_lembrar_me.setIconSize(QSize(25, 25))
        self.btn_lembrar_me.setCheckable(True)
        self.btn_lembrar_me.setAutoExclusive(True)
        self.btn_lembrar_me.setAutoDefault(True)
        self.btn_lembrar_me.setFlat(True)

        self.verticalLayout_20.addWidget(self.btn_lembrar_me)


        self.verticalLayout_24.addLayout(self.verticalLayout_20)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_18.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignBottom)

        self.date_selecionar_data_task = QDateEdit(self.layoutWidget)
        self.date_selecionar_data_task.setObjectName(u"date_selecionar_data_task")
        self.date_selecionar_data_task.setMinimumSize(QSize(0, 30))
        self.date_selecionar_data_task.setMaximumSize(QSize(150, 30))
        self.date_selecionar_data_task.setAutoFillBackground(False)
        self.date_selecionar_data_task.setInputMethodHints(Qt.InputMethodHint.ImhPreferNumbers)
        self.date_selecionar_data_task.setWrapping(False)
        self.date_selecionar_data_task.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date_selecionar_data_task.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.date_selecionar_data_task.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue)
        self.date_selecionar_data_task.setProperty(u"showGroupSeparator", False)
        self.date_selecionar_data_task.setDateTime(QDateTime(QDate(1999, 12, 30), QTime(21, 0, 0)))
        self.date_selecionar_data_task.setCalendarPopup(True)
        self.date_selecionar_data_task.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.verticalLayout_18.addWidget(self.date_selecionar_data_task)


        self.verticalLayout_24.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_19.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignBottom)

        self.cbx_repetir_task = QComboBox(self.layoutWidget)
        self.cbx_repetir_task.addItem("")
        self.cbx_repetir_task.addItem("")
        self.cbx_repetir_task.addItem("")
        self.cbx_repetir_task.addItem("")
        self.cbx_repetir_task.addItem("")
        self.cbx_repetir_task.setObjectName(u"cbx_repetir_task")
        self.cbx_repetir_task.setMinimumSize(QSize(0, 30))
        self.cbx_repetir_task.setMaximumSize(QSize(150, 30))

        self.verticalLayout_19.addWidget(self.cbx_repetir_task)


        self.verticalLayout_24.addLayout(self.verticalLayout_19)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frm_principal_rigth_task)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 250))
        self.frame_11.setMaximumSize(QSize(16777215, 250))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_11)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_21.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignBottom)

        self.txt_observacoes_task = QTextEdit(self.frame_11)
        self.txt_observacoes_task.setObjectName(u"txt_observacoes_task")

        self.verticalLayout_21.addWidget(self.txt_observacoes_task)


        self.verticalLayout_22.addLayout(self.verticalLayout_21)

        self.frame_18 = QFrame(self.frame_11)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 40))
        self.frame_18.setMaximumSize(QSize(16777215, 40))
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_salvar_new_task = QPushButton(self.frame_18)
        self.btn_salvar_new_task.setObjectName(u"btn_salvar_new_task")
        self.btn_salvar_new_task.setMinimumSize(QSize(0, 35))
        self.btn_salvar_new_task.setMaximumSize(QSize(16777215, 35))
        self.btn_salvar_new_task.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/imagens/floppy-disk.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_salvar_new_task.setIcon(icon6)
        self.btn_salvar_new_task.setIconSize(QSize(20, 20))
        self.btn_salvar_new_task.setCheckable(True)
        self.btn_salvar_new_task.setChecked(False)
        self.btn_salvar_new_task.setAutoRepeat(False)
        self.btn_salvar_new_task.setAutoExclusive(True)
        self.btn_salvar_new_task.setAutoDefault(True)
        self.btn_salvar_new_task.setFlat(True)

        self.horizontalLayout_9.addWidget(self.btn_salvar_new_task)

        self.btn_atualizar_task = QPushButton(self.frame_18)
        self.btn_atualizar_task.setObjectName(u"btn_atualizar_task")
        self.btn_atualizar_task.setMinimumSize(QSize(0, 35))
        self.btn_atualizar_task.setMaximumSize(QSize(16777215, 35))
        self.btn_atualizar_task.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_atualizar_task.setIcon(icon6)
        self.btn_atualizar_task.setIconSize(QSize(20, 20))
        self.btn_atualizar_task.setCheckable(True)
        self.btn_atualizar_task.setChecked(False)
        self.btn_atualizar_task.setAutoRepeat(False)
        self.btn_atualizar_task.setAutoExclusive(True)
        self.btn_atualizar_task.setAutoDefault(True)
        self.btn_atualizar_task.setFlat(True)

        self.horizontalLayout_9.addWidget(self.btn_atualizar_task)

        self.btn_excluir_task = QPushButton(self.frame_18)
        self.btn_excluir_task.setObjectName(u"btn_excluir_task")
        self.btn_excluir_task.setMinimumSize(QSize(0, 35))
        self.btn_excluir_task.setMaximumSize(QSize(16777215, 35))
        self.btn_excluir_task.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/imagens/trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_excluir_task.setIcon(icon7)
        self.btn_excluir_task.setIconSize(QSize(20, 20))
        self.btn_excluir_task.setCheckable(True)
        self.btn_excluir_task.setChecked(False)
        self.btn_excluir_task.setAutoRepeat(False)
        self.btn_excluir_task.setAutoExclusive(True)
        self.btn_excluir_task.setAutoDefault(True)
        self.btn_excluir_task.setFlat(True)

        self.horizontalLayout_9.addWidget(self.btn_excluir_task)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)


        self.verticalLayout_22.addWidget(self.frame_18)


        self.verticalLayout_4.addWidget(self.frame_11)


        self.horizontalLayout_2.addWidget(self.frm_principal_rigth_task)


        self.verticalLayout.addWidget(self.frame_3)

        self.frm_info_system = QFrame(self.frame_2)
        self.frm_info_system.setObjectName(u"frm_info_system")
        self.frm_info_system.setMinimumSize(QSize(0, 40))
        self.frm_info_system.setMaximumSize(QSize(16777215, 40))
        self.frm_info_system.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_info_system.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frm_info_system)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_adicionar_meu_dia.setDefault(False)
        self.btn_lembrar_me.setDefault(False)
        self.btn_salvar_new_task.setDefault(False)
        self.btn_atualizar_task.setDefault(False)
        self.btn_excluir_task.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_titulo_prioridades.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Prioridade</span></p></body></html>", None))
        self.lb_titulo_categorias.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Categorias</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_addNew_categoria.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#00007f;\">Nova Categoria</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_addNew_categoria.setText("")
        self.lb_titulo_superior_categoria.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Urgente</span></p></body></html>", None))
        self.lb_data_titulo_superior.setText(QCoreApplication.translate("MainWindow", u"20/05/2025", None))
#if QT_CONFIG(tooltip)
        self.btn_add_task.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#00007f;\">Nova Tarefa</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add_task.setText("")
        self.checkBox_task_line.setText("")
        self.lb_title_task.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lb_categoria_prioridade_task.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lb_data_task.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText("")
        self.lb_titulo_data_frmRigth.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Criado em Ter, 20 de Maio</span></p></body></html>", None))
        self.btn_close_frmRigth.setText("")
        self.checkBox_feito.setText("")
        self.comboBox_status_task.setItemText(0, "")
        self.comboBox_status_task.setItemText(1, QCoreApplication.translate("MainWindow", u"Conclu\u00eddo", None))
        self.comboBox_status_task.setItemText(2, QCoreApplication.translate("MainWindow", u"Descartado", None))

        self.comboBox_status_task.setCurrentText("")
        self.comboBox_status_task.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Prioridade", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.btn_adicionar_meu_dia.setText(QCoreApplication.translate("MainWindow", u"Adicionar ao meu Dia", None))
        self.btn_lembrar_me.setText(QCoreApplication.translate("MainWindow", u"  Lembrar-me", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Selecionar data", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Repetir", None))
        self.cbx_repetir_task.setItemText(0, QCoreApplication.translate("MainWindow", u"N\u00e3o ir\u00e1 se repetir", None))
        self.cbx_repetir_task.setItemText(1, QCoreApplication.translate("MainWindow", u"Di\u00e1riamente", None))
        self.cbx_repetir_task.setItemText(2, QCoreApplication.translate("MainWindow", u"Semanalmente", None))
        self.cbx_repetir_task.setItemText(3, QCoreApplication.translate("MainWindow", u"Mensalmente", None))
        self.cbx_repetir_task.setItemText(4, QCoreApplication.translate("MainWindow", u"Anualmente", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Adicionar anota\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.btn_salvar_new_task.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#00007f;\">Nova tarefa</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_salvar_new_task.setText("")
#if QT_CONFIG(tooltip)
        self.btn_atualizar_task.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#00007f;\">Salvar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_atualizar_task.setText("")
#if QT_CONFIG(tooltip)
        self.btn_excluir_task.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#00007f;\">Excluir tarefa</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_excluir_task.setText("")
    # retranslateUi

