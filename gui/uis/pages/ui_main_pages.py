# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesHSpAaG.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 615)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt ;")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.og_pic = QLabel(self.page_1)
        self.og_pic.setObjectName(u"og_pic")
        self.og_pic.setMaximumSize(QSize(480, 270))
        self.og_pic.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.og_pic)

        self.select_dir = QPushButton(self.page_1)
        self.select_dir.setObjectName(u"select_dir")
        self.select_dir.setMaximumSize(QSize(480, 32))
        self.select_dir.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_6.addWidget(self.select_dir)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.fix_single = QPushButton(self.page_1)
        self.fix_single.setObjectName(u"fix_single")
        self.fix_single.setMaximumSize(QSize(140, 87))

        self.horizontalLayout.addWidget(self.fix_single)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.page_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(480, 270))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.page_1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.comboBox = QComboBox(self.page_1)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.page_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.page_1_layout.addLayout(self.verticalLayout_3)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.empty_page_label = QLabel(self.page_3)
        self.empty_page_label.setObjectName(u"empty_page_label")
        font = QFont()
        font.setPointSize(16)
        self.empty_page_label.setFont(font)
        self.empty_page_label.setStyleSheet(u"t-size:14pt; background:;")
        self.empty_page_label.setAlignment(Qt.AlignCenter)

        self.page_3_layout.addWidget(self.empty_page_label)

        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.pages.addWidget(self.page_4)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.og_pic.setText(QCoreApplication.translate("MainPages", u"\u539f\u59cb\u753b\u9762\uff08\u56fe\u50cf/\u89c6\u9891\uff09", None))
        self.select_dir.setText(QCoreApplication.translate("MainPages", u"\u9009\u62e9\u6587\u4ef6", None))
        self.fix_single.setText(QCoreApplication.translate("MainPages", u"\u9884\u89c8\u4fee\u590d/\u5355\u5e27\u4fee\u590d", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"\u4fee\u590d\u753b\u9762\uff08\u56fe\u50cf/\u89c6\u9891\uff09", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainPages", u"\u6b63\u5f0f\u4fee\u590d", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainPages", u"MP4", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainPages", u"MOV", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainPages", u"MXF", None))

        self.label_3.setText(QCoreApplication.translate("MainPages", u"\u8fdb\u5ea6\u6761", None))
        self.empty_page_label.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
    # retranslateUi

