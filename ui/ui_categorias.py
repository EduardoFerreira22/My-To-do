# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'categoriasWWYmNY.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from icons import icons_rc

class Ui_CadastroCategorias(object):
    def setupUi(self, CadastroCategorias):
        if not CadastroCategorias.objectName():
            CadastroCategorias.setObjectName(u"CadastroCategorias")
        CadastroCategorias.resize(408, 64)
        self.verticalLayout = QVBoxLayout(CadastroCategorias)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(CadastroCategorias)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_window_categoria = QLineEdit(self.frame)
        self.txt_window_categoria.setObjectName(u"txt_window_categoria")
        self.txt_window_categoria.setMinimumSize(QSize(0, 30))
        self.txt_window_categoria.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.txt_window_categoria)

        self.frm_color_selected_categorias = QFrame(self.frame)
        self.frm_color_selected_categorias.setObjectName(u"frm_color_selected_categorias")
        self.frm_color_selected_categorias.setMinimumSize(QSize(20, 20))
        self.frm_color_selected_categorias.setMaximumSize(QSize(20, 20))
        self.frm_color_selected_categorias.setFrameShape(QFrame.Shape.Box)
        self.frm_color_selected_categorias.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.frm_color_selected_categorias)

        self.btn_selecionar_cor = QPushButton(self.frame)
        self.btn_selecionar_cor.setObjectName(u"btn_selecionar_cor")
        self.btn_selecionar_cor.setMinimumSize(QSize(35, 35))
        self.btn_selecionar_cor.setMaximumSize(QSize(35, 35))
        icon = QIcon()
        icon.addFile(u":/imagens/dropper.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_selecionar_cor.setIcon(icon)
        self.btn_selecionar_cor.setIconSize(QSize(25, 25))
        self.btn_selecionar_cor.setCheckable(True)
        self.btn_selecionar_cor.setAutoExclusive(True)
        self.btn_selecionar_cor.setAutoDefault(True)
        self.btn_selecionar_cor.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_selecionar_cor)

        self.btn_salvar_categoria = QPushButton(self.frame)
        self.btn_salvar_categoria.setObjectName(u"btn_salvar_categoria")
        self.btn_salvar_categoria.setMinimumSize(QSize(35, 35))
        self.btn_salvar_categoria.setMaximumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u":/imagens/floppy-disk.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_salvar_categoria.setIcon(icon1)
        self.btn_salvar_categoria.setIconSize(QSize(25, 25))
        self.btn_salvar_categoria.setCheckable(True)
        self.btn_salvar_categoria.setAutoExclusive(True)
        self.btn_salvar_categoria.setAutoDefault(True)
        self.btn_salvar_categoria.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_salvar_categoria)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(CadastroCategorias)

        QMetaObject.connectSlotsByName(CadastroCategorias)
    # setupUi

    def retranslateUi(self, CadastroCategorias):
        CadastroCategorias.setWindowTitle(QCoreApplication.translate("CadastroCategorias", u"Form", None))
#if QT_CONFIG(tooltip)
        self.btn_selecionar_cor.setToolTip(QCoreApplication.translate("CadastroCategorias", u"<html><head/><body><p><span style=\" font-weight:700; color:#00007f;\">Selecionar Cor</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_selecionar_cor.setText("")
#if QT_CONFIG(tooltip)
        self.btn_salvar_categoria.setToolTip(QCoreApplication.translate("CadastroCategorias", u"<html><head/><body><p><span style=\" font-weight:700; color:#00007f;\">Salvar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_salvar_categoria.setText("")
    # retranslateUi

