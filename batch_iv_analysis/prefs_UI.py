# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prefs.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_prefs(object):
    def setupUi(self, prefs):
        prefs.setObjectName("prefs")
        prefs.resize(412, 357)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(prefs.sizePolicy().hasHeightForWidth())
        prefs.setSizePolicy(sizePolicy)
        prefs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        prefs.setSizeGripEnabled(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(prefs)
        self.buttonBox.setGeometry(QtCore.QRect(30, 300, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.line = QtWidgets.QFrame(prefs)
        self.line.setGeometry(QtCore.QRect(233, 20, 20, 251))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(prefs)
        self.line_2.setGeometry(QtCore.QRect(120, 20, 251, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.I0_ub = QtWidgets.QLineEdit(prefs)
        self.I0_ub.setGeometry(QtCore.QRect(250, 40, 113, 32))
        self.I0_ub.setObjectName("I0_ub")
        self.label = QtWidgets.QLabel(prefs)
        self.label.setGeometry(QtCore.QRect(290, 10, 41, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(prefs)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 41, 20))
        self.label_2.setObjectName("label_2")
        self.I0_lb = QtWidgets.QLineEdit(prefs)
        self.I0_lb.setGeometry(QtCore.QRect(120, 40, 113, 32))
        self.I0_lb.setObjectName("I0_lb")
        self.line_3 = QtWidgets.QFrame(prefs)
        self.line_3.setGeometry(QtCore.QRect(20, 70, 351, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Iph_ub = QtWidgets.QLineEdit(prefs)
        self.Iph_ub.setGeometry(QtCore.QRect(250, 90, 113, 32))
        self.Iph_ub.setObjectName("Iph_ub")
        self.Iph_lb = QtWidgets.QLineEdit(prefs)
        self.Iph_lb.setGeometry(QtCore.QRect(120, 90, 113, 32))
        self.Iph_lb.setObjectName("Iph_lb")
        self.Rs_lb = QtWidgets.QLineEdit(prefs)
        self.Rs_lb.setGeometry(QtCore.QRect(120, 140, 113, 32))
        self.Rs_lb.setObjectName("Rs_lb")
        self.line_4 = QtWidgets.QFrame(prefs)
        self.line_4.setGeometry(QtCore.QRect(20, 120, 351, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.Rs_ub = QtWidgets.QLineEdit(prefs)
        self.Rs_ub.setGeometry(QtCore.QRect(250, 140, 113, 32))
        self.Rs_ub.setObjectName("Rs_ub")
        self.Rsh_lb = QtWidgets.QLineEdit(prefs)
        self.Rsh_lb.setGeometry(QtCore.QRect(120, 190, 113, 32))
        self.Rsh_lb.setObjectName("Rsh_lb")
        self.line_5 = QtWidgets.QFrame(prefs)
        self.line_5.setGeometry(QtCore.QRect(20, 170, 351, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.Rsh_ub = QtWidgets.QLineEdit(prefs)
        self.Rsh_ub.setGeometry(QtCore.QRect(250, 190, 113, 32))
        self.Rsh_ub.setObjectName("Rsh_ub")
        self.n_lb = QtWidgets.QLineEdit(prefs)
        self.n_lb.setGeometry(QtCore.QRect(120, 240, 113, 32))
        self.n_lb.setObjectName("n_lb")
        self.line_6 = QtWidgets.QFrame(prefs)
        self.line_6.setGeometry(QtCore.QRect(20, 220, 351, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.n_ub = QtWidgets.QLineEdit(prefs)
        self.n_ub.setGeometry(QtCore.QRect(250, 240, 113, 32))
        self.n_ub.setObjectName("n_ub")
        self.label_3 = QtWidgets.QLabel(prefs)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 61, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(prefs)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 61, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(prefs)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 71, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(prefs)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 81, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(prefs)
        self.label_7.setGeometry(QtCore.QRect(20, 250, 81, 20))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(prefs)
        self.buttonBox.accepted.connect(prefs.accept)
        self.buttonBox.rejected.connect(prefs.reject)
        QtCore.QMetaObject.connectSlotsByName(prefs)

    def retranslateUi(self, prefs):
        _translate = QtCore.QCoreApplication.translate
        prefs.setWindowTitle(_translate("prefs", "Set Parameter Bounds"))
        self.I0_ub.setText(_translate("prefs", "inf"))
        self.label.setText(_translate("prefs", "Upper"))
        self.label_2.setText(_translate("prefs", "Lower"))
        self.I0_lb.setText(_translate("prefs", "0"))
        self.Iph_ub.setText(_translate("prefs", "inf"))
        self.Iph_lb.setText(_translate("prefs", "0"))
        self.Rs_lb.setText(_translate("prefs", "0"))
        self.Rs_ub.setText(_translate("prefs", "inf"))
        self.Rsh_lb.setText(_translate("prefs", "0"))
        self.Rsh_ub.setText(_translate("prefs", "inf"))
        self.n_lb.setText(_translate("prefs", "0"))
        self.n_ub.setText(_translate("prefs", "inf"))
        self.label_3.setText(_translate("prefs", "I_0 [A]"))
        self.label_4.setText(_translate("prefs", "I_Ph [A]"))
        self.label_5.setText(_translate("prefs", "R_s [ohm]"))
        self.label_6.setText(_translate("prefs", "R_sh [ohm]"))
        self.label_7.setText(_translate("prefs", "n"))

