from PyQt5 import QtCore, QtGui, QtWidgets
#encoderass
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(995, 690)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 430, 971, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 360, 971, 61))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 971, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 6, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 1, 8, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 7, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 1, 6, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 1, 7, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 8, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 4, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 1, 9, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 9, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.cikti)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "OLUSTUR"))
        self.label_3.setText(_translate("Dialog", ""))
        self.label_7.setText(_translate("Dialog", ""))
        self.label_19.setText(_translate("Dialog", ""))
        self.label_4.setText(_translate("Dialog", ""))
        self.label_5.setText(_translate("Dialog", ""))
        self.label_8.setText(_translate("Dialog", ""))
        self.label_17.setText(_translate("Dialog", ""))
        self.label_18.setText(_translate("Dialog", ""))
        self.label_6.setText(_translate("Dialog", ""))
        self.label_9.setText(_translate("Dialog", ""))
        self.label_13.setText(_translate("Dialog", ""))
        self.label_15.setText(_translate("Dialog", ""))
        self.label_16.setText(_translate("Dialog", ""))
        self.label_11.setText(_translate("Dialog", ""))
        self.label_1.setText(_translate("Dialog", ""))
        self.label_2.setText(_translate("Dialog", ""))
        self.label_20.setText(_translate("Dialog", ""))
        self.label_14.setText(_translate("Dialog", ""))
        self.label_10.setText(_translate("Dialog", ""))
        self.label_12.setText(_translate("Dialog", ""))


    def cikti(self):
        mtn = self.lineEdit.text()
        boyut = len(mtn)
        cikti = ""

        self.label_1.setText(cikti)
        self.label_2.setText(cikti)
        self.label_3.setText(cikti)
        self.label_4.setText(cikti)
        self.label_5.setText(cikti)
        self.label_6.setText(cikti)
        self.label_7.setText(cikti)
        self.label_8.setText(cikti)
        self.label_9.setText(cikti)
        self.label_10.setText(cikti)
        self.label_11.setText(cikti)
        self.label_12.setText(cikti)
        self.label_13.setText(cikti)
        self.label_14.setText(cikti)
        self.label_15.setText(cikti)
        self.label_16.setText(cikti)
        self.label_17.setText(cikti)
        self.label_18.setText(cikti)
        self.label_19.setText(cikti)
        self.label_20.setText(cikti)

        for k in range(boyut):

            cikti = ""
            byt = 10

            if 'a' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if i == 0 or j == 0 or j == byt - 1 or i == byt/2:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'b' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if i == 0 or i == (byt-1)/2 or i == byt-1 or j == 0 or j == byt-1:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'c' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if i == 0 or j == 0 or i == byt-1:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'd' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if j == 0 or i == byt - 1 or j == byt - 1 or i == 0:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'e' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if i == 0 or i == byt/2 or i == byt - 1 or j == 0:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'f' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if i == 0 or i == byt/2 or j == 0:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'g' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if i == 0 or (i == byt/2) and (j > (byt-1)/2) or i == byt-1 or j == 0 or (i > (byt-1)/2) and (j == byt-1):
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'h' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if i == byt/2 or j == 0 or j == byt - 1:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'i' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if j == byt/2:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'j' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if i == byt - 1 or j == 0 and i > byt/2 or j == byt - 1:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'k' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if j == 2 or (byt - 1)/2 < i and i == j+1 or (byt - 1)/2 >= i and i == byt -1 - j-1:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'l' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if j == 0 or i == byt - 1:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'm' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if j == 0 or j == byt - 1 or j < byt/2 and i == j or j >= byt/2 and i == byt-1-j:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'n' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if j == 0 or j == byt - 1 or i == j:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'o' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if i == 0 or j == byt - 1 or i == byt -1 or j == 0:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'p' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if j == 0 or j == byt-1 and i < (byt - 1)/2 or i == 0 or i == (byt - 1)/2:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'r' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if j == 0 or j == byt - 1 and i < (byt - 1)/2 or i == 0 or i == byt/2 or i > (byt - 1)/2 and i == j:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 's' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if i == byt - 1 or i == 0 or j == 0 and i < (byt - 1)/2 or i == byt/2 or j == byt-1 and i > (byt - 1)/2:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 't' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if i == 0 or j == byt/2:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'u' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if j == 0 or j == byt - 1 or i == byt - 1:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'v' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt * 2):
                        if j < byt and i == j or j > byt and i == 2 * byt - j - 1:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'y' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if i >= (byt-1)/2 and j == byt/2 or i < (byt-1)/2 and ((j<(byt-1)/2 and i == j) or (j >= (byt-1)/2 and i==byt-1-j)):
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'z' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if i == 0 or i == byt-1 or i == byt - 1 - j:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'x' == mtn[k]:

                for i in range(byt):
                    cikti += "\n"
                    for j in range(byt):
                        if i == j or i == byt - 1 - j:
                            cikti += "x"
                        else:
                            cikti += "  "

            elif 'q' == mtn[k]:

                for i in range(byt * (6//5)):
                    cikti += "\n"
                    for j in range(byt * (6//5)):
                        if j==0 and i<byt or j==byt-1 and i<byt or i==0 and j<byt or i==byt-1 and j<byt or i>byt/2 and j>byt/2 and i==j:
                            cikti += "x"
                        else:
                            cikti += "  "

            else:
                pass

            if k == 0:
                self.label_1.setText(cikti)
            elif k == 1:
                self.label_2.setText(cikti)
            elif k == 2:
                self.label_3.setText(cikti)
            elif k == 3:
                self.label_4.setText(cikti)
            elif k == 4:
                self.label_5.setText(cikti)
            elif k == 5:
                self.label_6.setText(cikti)
            elif k == 6:
                self.label_7.setText(cikti)
            elif k == 7:
                self.label_8.setText(cikti)
            elif k == 8:
                self.label_9.setText(cikti)
            elif k == 9:
                self.label_10.setText(cikti)
            elif k == 10:
                self.label_11.setText(cikti)
            elif k == 11:
                self.label_12.setText(cikti)
            elif k == 12:
                self.label_13.setText(cikti)
            elif k == 13:
                self.label_14.setText(cikti)
            elif k == 14:
                self.label_15.setText(cikti)
            elif k == 15:
                self.label_16.setText(cikti)
            elif k == 16:
                self.label_17.setText(cikti)
            elif k == 17:
                self.label_18.setText(cikti)
            elif k == 18:
                self.label_19.setText(cikti)
            elif k == 19:
                self.label_20.setText(cikti)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

