# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences_.ui'
#
# Created: Sat Jul 27 18:40:46 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 388)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(480, 300))
        Dialog.setMaximumSize(QtCore.QSize(480, 550))
        Dialog.setWindowTitle("Preferences")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../src/img/muffin_ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Preferences of </span><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Muffin Translator</span><span style=\" font-size:12pt; font-weight:600; font-style:italic; vertical-align:super;\">2</span></p></body></html>")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setMargin(5)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.toolBox = QtGui.QToolBox(Dialog)
        self.toolBox.setObjectName("toolBox")
        self.conf_editor = QtGui.QWidget()
        self.conf_editor.setGeometry(QtCore.QRect(0, 0, 462, 215))
        self.conf_editor.setObjectName("conf_editor")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.conf_editor)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtGui.QLabel(self.conf_editor)
        self.label_3.setText("Time of auto-save (mm:ss): ")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.timeEdit = QtGui.QTimeEdit(self.conf_editor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy)
        self.timeEdit.setTime(QtCore.QTime(0, 0, 30))
        self.timeEdit.setMaximumTime(QtCore.QTime(0, 59, 59))
        self.timeEdit.setMinimumTime(QtCore.QTime(0, 0, 5))
        self.timeEdit.setCurrentSection(QtGui.QDateTimeEdit.MinuteSection)
        self.timeEdit.setDisplayFormat("mm:ss")
        self.timeEdit.setCurrentSectionIndex(0)
        self.timeEdit.setObjectName("timeEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.timeEdit)
        self.label_4 = QtGui.QLabel(self.conf_editor)
        self.label_4.setText("Font: ")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.fontComboBox = QtGui.QFontComboBox(self.conf_editor)
        self.fontComboBox.setObjectName("fontComboBox")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.fontComboBox)
        self.label_5 = QtGui.QLabel(self.conf_editor)
        self.label_5.setText("Size: ")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.spinBox_2 = QtGui.QSpinBox(self.conf_editor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setSuffix("pt")
        self.spinBox_2.setMinimum(5)
        self.spinBox_2.setProperty("value", 12)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinBox_2)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.toolBox.addItem(self.conf_editor, "Editor configurations")
        self.conf_shotcuts = QtGui.QWidget()
        self.conf_shotcuts.setGeometry(QtCore.QRect(0, 0, 243, 344))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conf_shotcuts.sizePolicy().hasHeightForWidth())
        self.conf_shotcuts.setSizePolicy(sizePolicy)
        self.conf_shotcuts.setObjectName("conf_shotcuts")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.conf_shotcuts)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea = QtGui.QScrollArea(self.conf_shotcuts)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 106, 324))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setText("Ctrl+1: ")
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setText("Ctrl+2: ")
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setText("Ctrl+3: ")
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_11 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setText("Ctrl+4: ")
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_11)
        self.label_10 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setText("Ctrl+5: ")
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_10)
        self.label_13 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setText("Ctrl+6: ")
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_13)
        self.label_12 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setText("Ctrl+7: ")
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_12)
        self.label_15 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setText("Ctrl+8: ")
        self.label_15.setObjectName("label_15")
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_15)
        self.label_14 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setText("Ctrl+9: ")
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_14)
        self.label_16 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setText("Ctrl+0: ")
        self.label_16.setObjectName("label_16")
        self.formLayout_3.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_2 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setPlaceholderText("Write a text")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setPlaceholderText("for insert")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setPlaceholderText("with a shotcut.")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setPlaceholderText("Example:")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_9 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_9.setPlaceholderText("Pablito clavó un clavito...")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_9)
        self.lineEdit_8 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_8.setPlaceholderText("EruJ is da best RAE fan...")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_8)
        self.lineEdit_7 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_7.setPlaceholderText("Winbug a sh*t")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_7)
        self.lineEdit_6 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_6.setPlaceholderText("Mac is for f*gs")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEdit_6)
        self.lineEdit_11 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_11.setPlaceholderText("The penguins will overpower the world!")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.FieldRole, self.lineEdit_11)
        self.lineEdit_10 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_10.setPlaceholderText("etc... 〜(^∇^〜)")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_3.setWidget(9, QtGui.QFormLayout.FieldRole, self.lineEdit_10)
        self.verticalLayout_2.addLayout(self.formLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.toolBox.addItem(self.conf_shotcuts, "Custom Shotcuts")
        self.conf_mplayer = QtGui.QWidget()
        self.conf_mplayer.setGeometry(QtCore.QRect(0, 0, 462, 215))
        self.conf_mplayer.setObjectName("conf_mplayer")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.conf_mplayer)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lineEdit = QtGui.QLineEdit(self.conf_mplayer)
        self.lineEdit.setText("mplayer")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_7 = QtGui.QLabel(self.conf_mplayer)
        self.label_7.setText("Secs for F1 and F2: ")
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.spinBox = QtGui.QSpinBox(self.conf_mplayer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setSuffix(" sec")
        self.spinBox.setMinimum(1)
        self.spinBox.setProperty("value", 3)
        self.spinBox.setObjectName("spinBox")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinBox)
        self.label_2 = QtGui.QLabel(self.conf_mplayer)
        self.label_2.setText("Mplayer path: ")
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_17 = QtGui.QLabel(self.conf_mplayer)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_17)
        self.comboBox = QtGui.QComboBox(self.conf_mplayer)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.label_18 = QtGui.QLabel(self.conf_mplayer)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_18)
        self.comboBox_2 = QtGui.QComboBox(self.conf_mplayer)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBox_2)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.toolBox.addItem(self.conf_mplayer, "Player configurations")
        self.verticalLayout.addWidget(self.toolBox)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.label_17.setText(QtGui.QApplication.translate("Dialog", "Video output (!): ", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "gl", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "SDL", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Dialog", "xv", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Dialog", "directx", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("Dialog", "direct3d", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("Dialog", "quartz", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("Dialog", "caca", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Dialog", "Audio output (!): ", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("Dialog", "oss", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(1, QtGui.QApplication.translate("Dialog", "alsa", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(2, QtGui.QApplication.translate("Dialog", "pulse", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(3, QtGui.QApplication.translate("Dialog", "coreaudio", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(4, QtGui.QApplication.translate("Dialog", "OpenAL", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(5, QtGui.QApplication.translate("Dialog", "win32", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(6, QtGui.QApplication.translate("Dialog", "dsound", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(7, QtGui.QApplication.translate("Dialog", "SDL", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

