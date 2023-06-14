import mgear.core.pyqt as gqt
QtGui, QtCore, QtWidgets, wrapInstance = gqt.qt_import()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(269, 218)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.intScale_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.intScale_checkBox.setObjectName("intScale_checkBox")
        self.verticalLayout_4.addWidget(self.intScale_checkBox)
        self.intRotation_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.intRotation_checkBox.setObjectName("intRotation_checkBox")
        self.verticalLayout_4.addWidget(self.intRotation_checkBox)
        self.intTranslation_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.intTranslation_checkBox.setObjectName("intTranslation_checkBox")
        self.verticalLayout_4.addWidget(self.intTranslation_checkBox)
        self.jointChainCnx_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.jointChainCnx_checkBox.setObjectName("jointChainCnx_checkBox")
        self.verticalLayout_4.addWidget(self.jointChainCnx_checkBox)
        self.metaCtl_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.metaCtl_checkBox.setObjectName("metaCtl_checkBox")
        self.verticalLayout_4.addWidget(self.metaCtl_checkBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(gqt.fakeTranslate("Form", "Form", None, -1))
        self.intScale_checkBox.setText(gqt.fakeTranslate("Form", "Interpolate Scale", None, -1))
        self.intRotation_checkBox.setText(gqt.fakeTranslate("Form", "Interpolate Rotation", None, -1))
        self.intTranslation_checkBox.setText(gqt.fakeTranslate("Form", "Interpolate Translation", None, -1))
        self.jointChainCnx_checkBox.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p>If checked will connect all the joints in chain, if uncheck will connect each joint to the parent component joint.</p></body></html>", None, -1))
        self.jointChainCnx_checkBox.setText(gqt.fakeTranslate("Form", "Joint Chain Connection", None, -1))
        self.metaCtl_checkBox.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p>If Checked, will create one control for each section</p></body></html>", None, -1))
        self.metaCtl_checkBox.setText(gqt.fakeTranslate("Form", "Meta Ctl", None, -1))
