# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_base.ui'
#
# Created: Tue Jul 23 22:42:52 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from muffin_utils import dir_
from MuffinVideo import QPlayerView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(str(dir_()) + "/img/muffin_ico.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_section = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(
            self.top_section.sizePolicy().hasHeightForWidth())
        self.top_section.setSizePolicy(sizePolicy)
        self.top_section.setObjectName("top_section")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.top_section)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.video_section = QtGui.QWidget(self.top_section)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.video_section.sizePolicy().hasHeightForWidth())
        self.video_section.setSizePolicy(sizePolicy)
        self.video_section.setObjectName("video_section")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.video_section)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        #los necesito aquí para mandarlos al MuffinVideo.
        self.volume_dial = QtGui.QDial(self.video_section)
        self.slider_video_control = QtGui.QSlider(self.video_section)
        
        
        #self.videoWidget = QtGui.QWidget(self.video_section)
        self.videoWidget = QPlayerView(self.video_section, self.volume_dial, 
                                       self.slider_video_control)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.videoWidget.sizePolicy().hasHeightForWidth())
        self.videoWidget.setSizePolicy(sizePolicy)
        self.videoWidget.setObjectName("videoWidget")
        self.verticalLayout_3.addWidget(self.videoWidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.slider_video_control.sizePolicy().hasHeightForWidth())
        self.slider_video_control.setSizePolicy(sizePolicy)
        self.slider_video_control.setOrientation(QtCore.Qt.Horizontal)
        self.slider_video_control.setObjectName("slider_video_control")
        self.verticalLayout_3.addWidget(self.slider_video_control)
        self.layout_video_control = QtGui.QHBoxLayout()
        self.layout_video_control.setObjectName("layout_video_control")
        spacerItem = QtGui.QSpacerItem(40, 20,
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.layout_video_control.addItem(spacerItem)
        self.button_play = QtGui.QPushButton(self.video_section)
        self.button_play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(str(dir_()) + "/img/play.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_play.setIcon(icon1)
        self.button_play.setObjectName("button_play")
        self.layout_video_control.addWidget(self.button_play)
        self.button_stop = QtGui.QPushButton(self.video_section)
        self.button_stop.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(str(dir_()) + "/img/stop.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_stop.setIcon(icon2)
        self.button_stop.setShortcut("")
        self.button_stop.setObjectName("button_stop")
        self.layout_video_control.addWidget(self.button_stop)
        self.button_bwd = QtGui.QPushButton(self.video_section)
        self.button_bwd.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(str(dir_()) + "/img/atras.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_bwd.setIcon(icon3)
        self.button_bwd.setObjectName("button_bwd")
        self.layout_video_control.addWidget(self.button_bwd)
        self.button_fwd = QtGui.QPushButton(self.video_section)
        self.button_fwd.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(str(dir_()) + "/img/adelante.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_fwd.setIcon(icon4)
        self.button_fwd.setObjectName("button_fwd")
        self.layout_video_control.addWidget(self.button_fwd)
        spacerItem1 = QtGui.QSpacerItem(40, 20,
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.layout_video_control.addItem(spacerItem1)
        self.volume_dial.setMaximumSize(QtCore.QSize(90, 35))
        self.volume_dial.setSingleStep(3)
        self.volume_dial.setObjectName("volume_dial")
        self.layout_video_control.addWidget(self.volume_dial)
        spacerItem2 = QtGui.QSpacerItem(40, 20,
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.layout_video_control.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.layout_video_control)
        self.horizontalLayout_3.addWidget(self.video_section)
        self.tabWidget_dict = QtGui.QTabWidget(self.top_section)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabWidget_dict.sizePolicy().hasHeightForWidth())
        self.tabWidget_dict.setSizePolicy(sizePolicy)
        self.tabWidget_dict.setTabPosition(QtGui.QTabWidget.East)
        self.tabWidget_dict.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_dict.setObjectName("tabWidget_dict")
        self.home_tab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.home_tab.sizePolicy().hasHeightForWidth())
        self.home_tab.setSizePolicy(sizePolicy)
        self.home_tab.setObjectName("home_tab")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.home_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtGui.QLabel(self.home_tab)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.tabWidget_dict.addTab(self.home_tab, "Home")
        self.wr_tab = QtGui.QWidget()
        self.wr_tab.setObjectName("wr_tab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.wr_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.wr_scrollArea = QtGui.QScrollArea(self.wr_tab)
        self.wr_scrollArea.setWidgetResizable(True)
        self.wr_scrollArea.setObjectName("wr_scrollArea")
        self.wr_scrollAreaWidgetContents = QtGui.QWidget()
        self.wr_scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, 284, 254))
        self.wr_scrollAreaWidgetContents.setObjectName(
            "wr_scrollAreaWidgetContents")
        self.verticalLayout_6 = QtGui.QVBoxLayout(
            self.wr_scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtGui.QLabel(
            self.wr_scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.wr_scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_6.addWidget(self.lineEdit)
        self.wr_consult = QtGui.QCommandLinkButton(self.wr_scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.wr_consult.sizePolicy().hasHeightForWidth())
        self.wr_consult.setSizePolicy(sizePolicy)
        self.wr_consult.setCursor(QtCore.Qt.PointingHandCursor)
        self.wr_consult.setObjectName("wr_consult")
        self.verticalLayout_6.addWidget(self.wr_consult)
        self.groupBox = QtGui.QGroupBox(self.wr_scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(
            QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setMargin(5)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.wr_scrollArea.setWidget(self.wr_scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.wr_scrollArea)
        self.tabWidget_dict.addTab(self.wr_tab, "Eng-Spa")
        self.horizontalLayout_3.addWidget(self.tabWidget_dict)
        self.verticalLayout.addWidget(self.top_section)
        self.wtf_a_line = QtGui.QFrame(self.centralwidget)
        self.wtf_a_line.setFrameShape(QtGui.QFrame.HLine)
        self.wtf_a_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.wtf_a_line.setObjectName("wtf_a_line")
        self.verticalLayout.addWidget(self.wtf_a_line)
        self.tabWidget_documents = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(
            self.tabWidget_documents.sizePolicy().hasHeightForWidth())
        self.tabWidget_documents.setSizePolicy(sizePolicy)
        self.tabWidget_documents.setStatusTip("")
        self.tabWidget_documents.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget_documents.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget_documents.setDocumentMode(True)
        self.tabWidget_documents.setTabsClosable(False)
        self.tabWidget_documents.setMovable(True)
        self.tabWidget_documents.setObjectName("tabWidget_documents")
        self.tab_doc = QtGui.QWidget()
        self.tab_doc.setObjectName("tab_doc")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_doc)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text_control = QtGui.QHBoxLayout()
        self.text_control.setObjectName("text_control")
        spacerItem3 = QtGui.QSpacerItem(40, 20,
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.text_control.addItem(spacerItem3)
        self.b_button = QtGui.QPushButton(self.tab_doc)
        self.b_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(
            "../src/img/format-text-bold.png"), QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.b_button.setIcon(icon5)
        self.b_button.setIconSize(QtCore.QSize(20, 20))
        self.b_button.setObjectName("b_button")
        self.text_control.addWidget(self.b_button)
        self.i_button = QtGui.QPushButton(self.tab_doc)
        self.i_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(str(dir_()) + "/img/format-text-italic.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.i_button.setIcon(icon6)
        self.i_button.setIconSize(QtCore.QSize(20, 20))
        self.i_button.setObjectName("i_button")
        self.text_control.addWidget(self.i_button)
        self.u_button = QtGui.QPushButton(self.tab_doc)
        self.u_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(str(dir_()) + "/img/format-text-underline.png"),
        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.u_button.setIcon(icon7)
        self.u_button.setIconSize(QtCore.QSize(20, 20))
        self.u_button.setObjectName("u_button")
        self.text_control.addWidget(self.u_button)
        self.comment_button = QtGui.QPushButton(self.tab_doc)
        self.comment_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(str(dir_()) + "/img/format-text-comment.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comment_button.setIcon(icon8)
        self.comment_button.setIconSize(QtCore.QSize(40, 20))
        self.comment_button.setObjectName("comment_button")
        self.text_control.addWidget(self.comment_button)
        self.line = QtGui.QFrame(self.tab_doc)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.text_control.addWidget(self.line)
        self.save_button = QtGui.QPushButton(self.tab_doc)
        self.save_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(str(dir_()) + "/img/document-save.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon9)
        self.save_button.setIconSize(QtCore.QSize(20, 20))
        #self.save_button.setShortcut("Ctrl+S")
        self.save_button.setObjectName("save_button")
        self.text_control.addWidget(self.save_button)
        spacerItem4 = QtGui.QSpacerItem(40, 20,
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.text_control.addItem(spacerItem4)
        self.close_doc_button = QtGui.QPushButton(self.tab_doc)
        self.close_doc_button.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(str(dir_()) + "/img/gtk-no.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_doc_button.setIcon(icon10)
        self.close_doc_button.setIconSize(QtCore.QSize(20, 20))
        self.close_doc_button.setObjectName("close_doc_button")
        self.text_control.addWidget(self.close_doc_button)
        self.verticalLayout_2.addLayout(self.text_control)
        self.plainText_document = QtGui.QPlainTextEdit(self.tab_doc)
        self.plainText_document.setToolTip("")
        self.plainText_document.setStatusTip("")
        self.plainText_document.setFrameShadow(QtGui.QFrame.Raised)
        self.plainText_document.setObjectName("plainText_document")
        self.verticalLayout_2.addWidget(self.plainText_document)
        self.tabWidget_documents.addTab(self.tab_doc, "Tab 1")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_documents.addTab(self.tab_2, "Tab 2")
        self.verticalLayout.addWidget(self.tabWidget_documents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuVideo_options = QtGui.QMenu(self.menubar)
        self.menuVideo_options.setObjectName("menuVideo_options")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_video = QtGui.QAction(MainWindow)
        self.actionOpen_video.setObjectName("actionOpen_video")
        self.actionOpen_document = QtGui.QAction(MainWindow)
        self.actionOpen_document.setObjectName("actionOpen_document")
        self.actionSave_document = QtGui.QAction(MainWindow)
        self.actionSave_document.setObjectName("actionSave_document")
        self.actionSave_all_documents = QtGui.QAction(MainWindow)
        self.actionSave_all_documents.setObjectName("actionSave_all_documents")
        self.actionSave_document_as = QtGui.QAction(MainWindow)
        self.actionSave_document_as.setObjectName("actionSave_document_as")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionLoadASS = QtGui.QAction(MainWindow)
        self.actionLoadASS.setObjectName("actionLoadASS")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionShow_time_of_video = QtGui.QAction(MainWindow)
        self.actionShow_time_of_video.setCheckable(True)
        self.actionShow_time_of_video.setObjectName("actionShow_time_of_video")
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionReport_a_bug = QtGui.QAction(MainWindow)
        self.actionReport_a_bug.setObjectName("actionReport_a_bug")
        self.actionNew_document = QtGui.QAction(MainWindow)
        self.actionNew_document.setObjectName("actionNew_document")
        self.menuFile.addAction(self.actionNew_document)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_document)
        self.menuFile.addAction(self.actionOpen_video)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_document)
        self.menuFile.addAction(self.actionSave_document_as)
        self.menuFile.addAction(self.actionSave_all_documents)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuVideo_options.addAction(self.actionLoadASS)
        self.menuVideo_options.addAction(self.actionShow_time_of_video)
        self.menuVideo_options.addSeparator()
        self.menuVideo_options.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionReport_a_bug)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuVideo_options.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        #Shotcuts, traducciones, etc...
        self.shotcuts(MainWindow)
        self.retranslateUi(MainWindow)
        self.tabWidget_dict.setCurrentIndex(0)
        self.tabWidget_documents.setCurrentIndex(0)
        
        #Conexiones y todo eso
        self.actionQuit.activated.connect(MainWindow.close)
        self.actionOpen_video.activated.connect(self.videoWidget.load_video)
        self.button_play.clicked.connect(self.videoWidget.pause_clicked)
        self.button_stop.pressed.connect(self.videoWidget.stop_clicked)
        self.button_fwd.clicked.connect(self.videoWidget.onAdvanceVideo)
        self.button_bwd.clicked.connect(self.videoWidget.onBackVideo)
        self.volume_dial.dialReleased.connect(self.videoWidget.set_vol_clicked)
        self.slider_video_control.sliderMoved.connect(self.videoWidget.set_pos)
        
        
    def shotcuts(self,MainWindow):
        self.button_play.setShortcut("Esc")
        self.button_bwd.setShortcut("F1")
        self.button_fwd.setShortcut("F2")
        self.b_button.setShortcut("Ctrl+B")
        self.i_button.setShortcut("Ctrl+I")
        self.u_button.setShortcut("Ctrl+U")
        self.comment_button.setShortcut("Ctrl+K")
        self.close_doc_button.setShortcut("Ctrl+W")
        self.actionOpen_document.setShortcut("Ctrl+F")
        self.actionOpen_video.setShortcut("Ctrl+Shift+F")
        self.actionSave_document.setShortcut("Ctrl+S")
        self.actionSave_document_as.setShortcut("Ctrl+Shift+S")
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionPreferences.setShortcut("Ctrl+P")
        self.actionNew_document.setShortcut("Ctrl+N")
        
    
    
    def retranslateUi(self, MainWindow):
        '''Aquí está la mayoría del texto'''
        MainWindow.setWindowTitle("Muffin Translator 2 - " +
            " develop version へ(>_<へ) ")
        self.button_play.setStatusTip("Play/Pause button, you can use Esc key.")
        self.button_stop.setStatusTip("This button stop completely the video.")
        self.button_bwd.setStatusTip(
            "Back a little the video, you can use F1 key.")
        self.button_fwd.setStatusTip(
            "Forward a little the video, you can use F2 key.")
        self.wr_consult.setText("Consult powerd by Wordreference")
        self.label_3.setText("TextLabel")#este es el de las traducciones
        self.b_button.setToolTip("Bold")
        self.b_button.setStatusTip(
            "Put «{\\b1} ····· {\\b0}» in a select text. You can use Ctrl+B.")
        self.i_button.setToolTip("Italic")
        self.i_button.setStatusTip(
            "Put «{\\i1} ····· {\\i0}» in a select text. You can use Ctrl+I.")
        self.u_button.setToolTip("Underline")
        self.u_button.setStatusTip(
            "Put «{\\u1} ····· {\\u0}» in a select text. You can use Ctrl+U.")
        self.comment_button.setToolTip("Comment")
        self.comment_button.setStatusTip(
            "Put the selected text in comment, «{ ····· }». You can use Ctrl+K.")
        self.save_button.setToolTip("Save this document")
        self.save_button.setStatusTip("Save the document in any place...")
        self.close_doc_button.setToolTip("Close")
        self.close_doc_button.setStatusTip(
            "Close this tab. You can use Ctrl+W.")
        self.slider_video_control.setStatusTip("このは明白ですよ。。。")
        self.button_play.setToolTip("Play/Pause")
        self.button_stop.setToolTip("Stop")
        self.button_bwd.setToolTip("Back")
        self.button_fwd.setToolTip("Forward")
        self.volume_dial.setToolTip("Volume")
        self.volume_dial.setStatusTip("Sets the volume.")
        __welcom_text = "<html><head/><body><p><span style=\" font-size:18pt;\">"+ \
                        "{0}</span></p><p><span style=\" font-size:18pt;" + \
                        "font-weight:600;\">Muffin Translator</span>" + \
                        "<span style=\" font-size:18pt; font-weight:600;" + \
                        "vertical-align:super;\">2</span></p></body></html>"
        self.label.setText(str(__welcom_text).format('Welcome to'))
        self.label_2.setText("English-Spanish :")
        self.groupBox.setTitle("Result:")
        self.menuFile.setTitle("File")
        self.menuVideo_options.setTitle("Options")
        self.menuHelp.setTitle("Help")
        self.actionOpen_document.setText("Open document")
        self.actionOpen_video.setText("Open video")
        self.actionSave_document.setText("Save document")
        self.actionSave_all_documents.setText("Save all documents")
        self.actionSave_document_as.setText("Save document as...")
        self.actionQuit.setText("Quit")
        self.actionLoadASS.setText("Load subs from video (MKV)")
        self.actionAbout.setText("About...")
        self.actionShow_time_of_video.setText("Show time of video")
        self.actionPreferences.setText("Preferences")
        self.actionReport_a_bug.setText("Report a bug")
        self.actionNew_document.setText("New document")


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
