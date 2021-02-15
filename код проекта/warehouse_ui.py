# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Warehouse.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(597, 390)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 5)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(130, 25))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 4, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 4)
        self.pb_replenish = QtWidgets.QPushButton(Form)
        self.pb_replenish.setMinimumSize(QtCore.QSize(0, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../pictures/warehouse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_replenish.setIcon(icon)
        self.pb_replenish.setObjectName("pb_replenish")
        self.gridLayout.addWidget(self.pb_replenish, 2, 1, 1, 1)
        self.pb_add = QtWidgets.QPushButton(Form)
        self.pb_add.setMinimumSize(QtCore.QSize(0, 30))
        self.pb_add.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../pictures/Add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_add.setIcon(icon1)
        self.pb_add.setObjectName("pb_add")
        self.gridLayout.addWidget(self.pb_add, 2, 2, 1, 1)
        self.pb_edit = QtWidgets.QPushButton(Form)
        self.pb_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.pb_edit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../pictures/Edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_edit.setIcon(icon2)
        self.pb_edit.setObjectName("pb_edit")
        self.gridLayout.addWidget(self.pb_edit, 2, 3, 1, 1)
        self.pb_update = QtWidgets.QPushButton(Form)
        self.pb_update.setMinimumSize(QtCore.QSize(0, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../pictures/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_update.setIcon(icon3)
        self.pb_update.setObjectName("pb_update")
        self.gridLayout.addWidget(self.pb_update, 2, 4, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Подстрока для поиска:"))
        self.label_3.setText(_translate("Form", "Элементы склада:"))
        self.label_2.setText(_translate("Form", "Категория:"))
        self.pb_replenish.setText(_translate("Form", "Пополнить"))
        self.pb_add.setText(_translate("Form", "Добавить"))
        self.pb_edit.setText(_translate("Form", "Редактировать"))
        self.pb_update.setText(_translate("Form", "Обновить"))
