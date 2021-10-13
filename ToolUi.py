# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ToolUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tool(object):
    def setupUi(self, Tool):
        Tool.setObjectName("Tool")
        Tool.resize(752, 568)
        Tool.setMinimumSize(QtCore.QSize(752, 444))
        Tool.setMaximumSize(QtCore.QSize(752, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(206, 233, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 145, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        Tool.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("HarmonyOS Sans Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        Tool.setFont(font)
        Tool.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Tool.setMouseTracking(False)
        Tool.setTabletTracking(False)
        Tool.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Tool.setAcceptDrops(False)
        Tool.setAccessibleDescription("")
        Tool.setAutoFillBackground(True)
        Tool.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(Tool)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Roman_Frame = QtWidgets.QFrame(self.centralwidget)
        self.Roman_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Roman_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Roman_Frame.setObjectName("Roman_Frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Roman_Frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ZhiHeNum = QtWidgets.QFrame(self.Roman_Frame)
        self.ZhiHeNum.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ZhiHeNum.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ZhiHeNum.setObjectName("ZhiHeNum")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ZhiHeNum)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.UiZhiShuZhiHe = QtWidgets.QLabel(self.ZhiHeNum)
        self.UiZhiShuZhiHe.setObjectName("UiZhiShuZhiHe")
        self.horizontalLayout.addWidget(self.UiZhiShuZhiHe)
        self.UiZhiShuNum = QtWidgets.QLineEdit(self.ZhiHeNum)
        self.UiZhiShuNum.setMinimumSize(QtCore.QSize(0, 36))
        self.UiZhiShuNum.setObjectName("UiZhiShuNum")
        self.horizontalLayout.addWidget(self.UiZhiShuNum)
        self.UiZhiShuStart = QtWidgets.QPushButton(self.ZhiHeNum)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.UiZhiShuStart.setFont(font)
        self.UiZhiShuStart.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.UiZhiShuStart.setObjectName("UiZhiShuStart")
        self.horizontalLayout.addWidget(self.UiZhiShuStart)
        self.UiZhiShuFinally = QtWidgets.QLabel(self.ZhiHeNum)
        self.UiZhiShuFinally.setObjectName("UiZhiShuFinally")
        self.horizontalLayout.addWidget(self.UiZhiShuFinally)
        self.verticalLayout_3.addWidget(self.ZhiHeNum)
        self.Roman = QtWidgets.QFrame(self.Roman_Frame)
        self.Roman.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Roman.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Roman.setObjectName("Roman")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Roman)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.UiRomanRoman = QtWidgets.QLabel(self.Roman)
        self.UiRomanRoman.setObjectName("UiRomanRoman")
        self.horizontalLayout_2.addWidget(self.UiRomanRoman)
        self.UiRomanRomanNum = QtWidgets.QLineEdit(self.Roman)
        self.UiRomanRomanNum.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setFamily("HarmonyOS Sans Condensed Medium")
        self.UiRomanRomanNum.setFont(font)
        self.UiRomanRomanNum.setText("")
        self.UiRomanRomanNum.setObjectName("UiRomanRomanNum")
        self.horizontalLayout_2.addWidget(self.UiRomanRomanNum)
        self.NumToRoman = QtWidgets.QPushButton(self.Roman)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.NumToRoman.setFont(font)
        self.NumToRoman.setAutoFillBackground(False)
        self.NumToRoman.setObjectName("NumToRoman")
        self.horizontalLayout_2.addWidget(self.NumToRoman)
        self.RumanToNum = QtWidgets.QPushButton(self.Roman)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RumanToNum.setFont(font)
        self.RumanToNum.setObjectName("RumanToNum")
        self.horizontalLayout_2.addWidget(self.RumanToNum)
        self.UiRomanNum = QtWidgets.QLineEdit(self.Roman)
        self.UiRomanNum.setMinimumSize(QtCore.QSize(0, 36))
        self.UiRomanNum.setObjectName("UiRomanNum")
        self.horizontalLayout_2.addWidget(self.UiRomanNum)
        self.verticalLayout_3.addWidget(self.Roman)
        self.PassWord = QtWidgets.QFrame(self.Roman_Frame)
        self.PassWord.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PassWord.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PassWord.setObjectName("PassWord")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.PassWord)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.UiPassWordLabel = QtWidgets.QLabel(self.PassWord)
        self.UiPassWordLabel.setObjectName("UiPassWordLabel")
        self.horizontalLayout_6.addWidget(self.UiPassWordLabel)
        self.UiPassWordOriginal = QtWidgets.QLineEdit(self.PassWord)
        self.UiPassWordOriginal.setMinimumSize(QtCore.QSize(0, 36))
        self.UiPassWordOriginal.setObjectName("UiPassWordOriginal")
        self.horizontalLayout_6.addWidget(self.UiPassWordOriginal)
        self.UiPassWordDe = QtWidgets.QPushButton(self.PassWord)
        self.UiPassWordDe.setObjectName("UiPassWordDe")
        self.horizontalLayout_6.addWidget(self.UiPassWordDe)
        self.UiPassWordEn = QtWidgets.QPushButton(self.PassWord)
        self.UiPassWordEn.setObjectName("UiPassWordEn")
        self.horizontalLayout_6.addWidget(self.UiPassWordEn)
        self.UiPassWordPassWord = QtWidgets.QLineEdit(self.PassWord)
        self.UiPassWordPassWord.setEnabled(True)
        self.UiPassWordPassWord.setMinimumSize(QtCore.QSize(0, 36))
        self.UiPassWordPassWord.setTabletTracking(False)
        self.UiPassWordPassWord.setMaxLength(32767)
        self.UiPassWordPassWord.setObjectName("UiPassWordPassWord")
        self.horizontalLayout_6.addWidget(self.UiPassWordPassWord)
        self.verticalLayout_3.addWidget(self.PassWord)
        self.Morse_Frame = QtWidgets.QFrame(self.Roman_Frame)
        self.Morse_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Morse_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Morse_Frame.setObjectName("Morse_Frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Morse_Frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.UiMorseMorseLabel = QtWidgets.QLabel(self.Morse_Frame)
        self.UiMorseMorseLabel.setObjectName("UiMorseMorseLabel")
        self.horizontalLayout_5.addWidget(self.UiMorseMorseLabel)
        self.UiMorsePassWord = QtWidgets.QLineEdit(self.Morse_Frame)
        self.UiMorsePassWord.setMinimumSize(QtCore.QSize(0, 36))
        self.UiMorsePassWord.setText("")
        self.UiMorsePassWord.setObjectName("UiMorsePassWord")
        self.horizontalLayout_5.addWidget(self.UiMorsePassWord)
        self.morse = QtWidgets.QPushButton(self.Morse_Frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.morse.setFont(font)
        self.morse.setObjectName("morse")
        self.horizontalLayout_5.addWidget(self.morse)
        self.plaintext = QtWidgets.QPushButton(self.Morse_Frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.plaintext.setFont(font)
        self.plaintext.setObjectName("plaintext")
        self.horizontalLayout_5.addWidget(self.plaintext)
        self.UiMorselineEdit = QtWidgets.QLineEdit(self.Morse_Frame)
        self.UiMorselineEdit.setMinimumSize(QtCore.QSize(0, 36))
        self.UiMorselineEdit.setMaximumSize(QtCore.QSize(72, 16777215))
        self.UiMorselineEdit.setObjectName("UiMorselineEdit")
        self.horizontalLayout_5.addWidget(self.UiMorselineEdit)
        self.UiMorseOriginal = QtWidgets.QLineEdit(self.Morse_Frame)
        self.UiMorseOriginal.setMinimumSize(QtCore.QSize(0, 36))
        self.UiMorseOriginal.setReadOnly(False)
        self.UiMorseOriginal.setObjectName("UiMorseOriginal")
        self.horizontalLayout_5.addWidget(self.UiMorseOriginal)
        self.verticalLayout_3.addWidget(self.Morse_Frame)
        self.Fence = QtWidgets.QFrame(self.Roman_Frame)
        self.Fence.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Fence.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Fence.setObjectName("Fence")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Fence)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.UiFenceFenceLabel = QtWidgets.QLabel(self.Fence)
        self.UiFenceFenceLabel.setObjectName("UiFenceFenceLabel")
        self.horizontalLayout_3.addWidget(self.UiFenceFenceLabel)
        self.UiFenceOriginal = QtWidgets.QLineEdit(self.Fence)
        self.UiFenceOriginal.setMinimumSize(QtCore.QSize(0, 36))
        self.UiFenceOriginal.setObjectName("UiFenceOriginal")
        self.horizontalLayout_3.addWidget(self.UiFenceOriginal)
        self.Decrypt = QtWidgets.QPushButton(self.Fence)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Decrypt.setFont(font)
        self.Decrypt.setObjectName("Decrypt")
        self.horizontalLayout_3.addWidget(self.Decrypt)
        self.Encrypt = QtWidgets.QPushButton(self.Fence)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Encrypt.setFont(font)
        self.Encrypt.setObjectName("Encrypt")
        self.horizontalLayout_3.addWidget(self.Encrypt)
        self.UiFenceFenceKey = QtWidgets.QLineEdit(self.Fence)
        self.UiFenceFenceKey.setMinimumSize(QtCore.QSize(0, 36))
        self.UiFenceFenceKey.setMaximumSize(QtCore.QSize(72, 16777215))
        self.UiFenceFenceKey.setText("")
        self.UiFenceFenceKey.setObjectName("UiFenceFenceKey")
        self.horizontalLayout_3.addWidget(self.UiFenceFenceKey)
        self.UiFenceFencePassWord = QtWidgets.QLineEdit(self.Fence)
        self.UiFenceFencePassWord.setMinimumSize(QtCore.QSize(0, 36))
        self.UiFenceFencePassWord.setObjectName("UiFenceFencePassWord")
        self.horizontalLayout_3.addWidget(self.UiFenceFencePassWord)
        self.verticalLayout_3.addWidget(self.Fence)
        self.Caesar = QtWidgets.QFrame(self.Roman_Frame)
        self.Caesar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Caesar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Caesar.setObjectName("Caesar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Caesar)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.UiCaesarCaesarLabel = QtWidgets.QLabel(self.Caesar)
        self.UiCaesarCaesarLabel.setObjectName("UiCaesarCaesarLabel")
        self.horizontalLayout_4.addWidget(self.UiCaesarCaesarLabel)
        self.UiCaesarOriginal = QtWidgets.QLineEdit(self.Caesar)
        self.UiCaesarOriginal.setMinimumSize(QtCore.QSize(0, 36))
        self.UiCaesarOriginal.setObjectName("UiCaesarOriginal")
        self.horizontalLayout_4.addWidget(self.UiCaesarOriginal)
        self.decrypt = QtWidgets.QPushButton(self.Caesar)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.decrypt.setFont(font)
        self.decrypt.setObjectName("decrypt")
        self.horizontalLayout_4.addWidget(self.decrypt)
        self.encrypt = QtWidgets.QPushButton(self.Caesar)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.encrypt.setFont(font)
        self.encrypt.setObjectName("encrypt")
        self.horizontalLayout_4.addWidget(self.encrypt)
        self.UiCaesarPassWord = QtWidgets.QLineEdit(self.Caesar)
        self.UiCaesarPassWord.setMinimumSize(QtCore.QSize(0, 36))
        self.UiCaesarPassWord.setObjectName("UiCaesarPassWord")
        self.horizontalLayout_4.addWidget(self.UiCaesarPassWord)
        self.verticalLayout_3.addWidget(self.Caesar)
        self.Vigenere = QtWidgets.QFrame(self.Roman_Frame)
        self.Vigenere.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Vigenere.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Vigenere.setObjectName("Vigenere")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Vigenere)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.UiVigenerelabel = QtWidgets.QLabel(self.Vigenere)
        self.UiVigenerelabel.setObjectName("UiVigenerelabel")
        self.horizontalLayout_7.addWidget(self.UiVigenerelabel)
        self.UiVigenereOriginal = QtWidgets.QLineEdit(self.Vigenere)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UiVigenereOriginal.sizePolicy().hasHeightForWidth())
        self.UiVigenereOriginal.setSizePolicy(sizePolicy)
        self.UiVigenereOriginal.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.UiVigenereOriginal.setFont(font)
        self.UiVigenereOriginal.setObjectName("UiVigenereOriginal")
        self.horizontalLayout_7.addWidget(self.UiVigenereOriginal)
        self.UiVigenereDecrypt = QtWidgets.QPushButton(self.Vigenere)
        self.UiVigenereDecrypt.setObjectName("UiVigenereDecrypt")
        self.horizontalLayout_7.addWidget(self.UiVigenereDecrypt)
        self.UiVigenereEncrypt = QtWidgets.QPushButton(self.Vigenere)
        self.UiVigenereEncrypt.setObjectName("UiVigenereEncrypt")
        self.horizontalLayout_7.addWidget(self.UiVigenereEncrypt)
        self.UiVigenereKey = QtWidgets.QLineEdit(self.Vigenere)
        self.UiVigenereKey.setMinimumSize(QtCore.QSize(85, 36))
        self.UiVigenereKey.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.UiVigenereKey.setFont(font)
        self.UiVigenereKey.setObjectName("UiVigenereKey")
        self.horizontalLayout_7.addWidget(self.UiVigenereKey)
        self.UiVigenerePassWord = QtWidgets.QLineEdit(self.Vigenere)
        self.UiVigenerePassWord.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.UiVigenerePassWord.setFont(font)
        self.UiVigenerePassWord.setObjectName("UiVigenerePassWord")
        self.horizontalLayout_7.addWidget(self.UiVigenerePassWord)
        self.verticalLayout_3.addWidget(self.Vigenere)
        self.gridLayout.addWidget(self.Roman_Frame, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        Tool.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(Tool)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 752, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        Tool.setMenuBar(self.menuBar)
        self.actionOpenInCmd = QtWidgets.QAction(Tool)
        self.actionOpenInCmd.setObjectName("actionOpenInCmd")
        self.actionRead = QtWidgets.QAction(Tool)
        self.actionRead.setObjectName("actionRead")
        self.actionExit = QtWidgets.QAction(Tool)
        self.actionExit.setMenuRole(QtWidgets.QAction.ApplicationSpecificRole)
        self.actionExit.setShortcutVisibleInContextMenu(True)
        self.actionExit.setObjectName("actionExit")
        self.menu_2.addAction(self.actionExit)
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(Tool)
        self.actionExit.triggered.connect(Tool.close)
        QtCore.QMetaObject.connectSlotsByName(Tool)

    def retranslateUi(self, Tool):
        _translate = QtCore.QCoreApplication.translate
        Tool.setWindowTitle(_translate("Tool", "工具箱"))
        self.UiZhiShuZhiHe.setText(_translate("Tool", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">质合数判断</span></p></body></html>"))
        self.UiZhiShuNum.setPlaceholderText(_translate("Tool", "在这里输入要判断的整数"))
        self.UiZhiShuStart.setText(_translate("Tool", "判断"))
        self.UiZhiShuFinally.setText(_translate("Tool", "<html><head/><body><p><span style=\" font-weight:600;\">结果</span></p></body></html>"))
        self.UiRomanRoman.setText(_translate("Tool", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">罗马数字</span></p></body></html>"))
        self.UiRomanRomanNum.setPlaceholderText(_translate("Tool", "在这里输入罗马数字"))
        self.NumToRoman.setText(_translate("Tool", "←"))
        self.RumanToNum.setText(_translate("Tool", "→"))
        self.UiRomanNum.setPlaceholderText(_translate("Tool", "在这里输入阿拉伯数字"))
        self.UiPassWordLabel.setText(_translate("Tool", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">加密</span></p></body></html>"))
        self.UiPassWordOriginal.setPlaceholderText(_translate("Tool", "在这里输入原文"))
        self.UiPassWordDe.setText(_translate("Tool", "←"))
        self.UiPassWordEn.setText(_translate("Tool", "→"))
        self.UiPassWordPassWord.setPlaceholderText(_translate("Tool", "在这里输入密文"))
        self.UiMorseMorseLabel.setText(_translate("Tool", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">摩斯密码</span></p></body></html>"))
        self.UiMorsePassWord.setPlaceholderText(_translate("Tool", "在这里输入摩斯密码"))
        self.morse.setText(_translate("Tool", "←"))
        self.plaintext.setText(_translate("Tool", "→"))
        self.UiMorselineEdit.setPlaceholderText(_translate("Tool", "分隔符"))
        self.UiMorseOriginal.setPlaceholderText(_translate("Tool", "在这里输入明文"))
        self.UiFenceFenceLabel.setText(_translate("Tool", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">栅栏密码</span></p></body></html>"))
        self.UiFenceOriginal.setPlaceholderText(_translate("Tool", "在这里输入原文"))
        self.Decrypt.setText(_translate("Tool", "←"))
        self.Encrypt.setText(_translate("Tool", "→"))
        self.UiFenceFenceKey.setPlaceholderText(_translate("Tool", "密钥"))
        self.UiFenceFencePassWord.setPlaceholderText(_translate("Tool", "在这里输入密文"))
        self.UiCaesarCaesarLabel.setText(_translate("Tool", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">凯撒密码</span></p></body></html>"))
        self.UiCaesarOriginal.setPlaceholderText(_translate("Tool", "在这里输入原文"))
        self.decrypt.setText(_translate("Tool", "←"))
        self.encrypt.setText(_translate("Tool", "→"))
        self.UiCaesarPassWord.setPlaceholderText(_translate("Tool", "在这里输入密文"))
        self.UiVigenerelabel.setText(_translate("Tool", "<html><head/><body><p><span style=\" font-weight:600;\">Vigenere密码</span></p></body></html>"))
        self.UiVigenereOriginal.setPlaceholderText(_translate("Tool", "在这里输入原文"))
        self.UiVigenereDecrypt.setText(_translate("Tool", "←"))
        self.UiVigenereEncrypt.setText(_translate("Tool", "→"))
        self.UiVigenereKey.setPlaceholderText(_translate("Tool", "密钥"))
        self.UiVigenerePassWord.setPlaceholderText(_translate("Tool", "在这里输入密文"))
        self.menu_2.setTitle(_translate("Tool", "窗口"))
        self.actionOpenInCmd.setText(_translate("Tool", "在文本交互界面打开"))
        self.actionRead.setText(_translate("Tool", "查看"))
        self.actionRead.setToolTip(_translate("Tool", "查看日志"))
        self.actionRead.setShortcut(_translate("Tool", "Ctrl+L"))
        self.actionExit.setText(_translate("Tool", "退出"))
        self.actionExit.setToolTip(_translate("Tool", "退出"))