# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\PyQt\Project\my_dlib_face_detection_application\TrainObjectDetectorParametersGui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TrainObjectDetectorParametersDialog(object):
    def setupUi(self, TrainObjectDetectorParametersDialog):
        TrainObjectDetectorParametersDialog.setObjectName(_fromUtf8("TrainObjectDetectorParametersDialog"))
        TrainObjectDetectorParametersDialog.resize(864, 488)
        self.verticalLayout_10 = QtGui.QVBoxLayout(TrainObjectDetectorParametersDialog)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label = QtGui.QLabel(TrainObjectDetectorParametersDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_9.addWidget(self.label)
        self.line = QtGui.QFrame(TrainObjectDetectorParametersDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_9.addWidget(self.line)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_8 = QtGui.QLabel(TrainObjectDetectorParametersDialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(TrainObjectDetectorParametersDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(TrainObjectDetectorParametersDialog)
        self.doubleSpinBox.setMaximum(1000.0)
        self.doubleSpinBox.setSingleStep(0.5)
        self.doubleSpinBox.setProperty("value", 5.0)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_9.addLayout(self.verticalLayout)
        self.line_2 = QtGui.QFrame(TrainObjectDetectorParametersDialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_9.addWidget(self.line_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_9 = QtGui.QLabel(TrainObjectDetectorParametersDialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_4.addWidget(self.label_9)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtGui.QLabel(TrainObjectDetectorParametersDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(TrainObjectDetectorParametersDialog)
        self.doubleSpinBox_2.setSingleStep(0.01)
        self.doubleSpinBox_2.setProperty("value", 0.01)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_9.addLayout(self.verticalLayout_4)
        self.line_3 = QtGui.QFrame(TrainObjectDetectorParametersDialog)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_9.addWidget(self.line_3)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_10 = QtGui.QLabel(TrainObjectDetectorParametersDialog)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_5.addWidget(self.label_10)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_4 = QtGui.QLabel(TrainObjectDetectorParametersDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.spinBox = QtGui.QSpinBox(TrainObjectDetectorParametersDialog)
        self.spinBox.setProperty("value", 4)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_4.addWidget(self.spinBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.line_4 = QtGui.QFrame(TrainObjectDetectorParametersDialog)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_9.addWidget(self.line_4)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_11 = QtGui.QLabel(TrainObjectDetectorParametersDialog)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_6.addWidget(self.label_11)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.label_5 = QtGui.QLabel(TrainObjectDetectorParametersDialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        self.spinBox_2 = QtGui.QSpinBox(TrainObjectDetectorParametersDialog)
        self.spinBox_2.setMaximum(10000)
        self.spinBox_2.setSingleStep(100)
        self.spinBox_2.setProperty("value", 6400)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.horizontalLayout_6.addWidget(self.spinBox_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.line_5 = QtGui.QFrame(TrainObjectDetectorParametersDialog)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_9.addWidget(self.line_5)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_12 = QtGui.QLabel(TrainObjectDetectorParametersDialog)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_7.addWidget(self.label_12)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.label_6 = QtGui.QLabel(TrainObjectDetectorParametersDialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_7.addWidget(self.label_6)
        self.groupBox = QtGui.QGroupBox(TrainObjectDetectorParametersDialog)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7.addWidget(self.groupBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.line_6 = QtGui.QFrame(TrainObjectDetectorParametersDialog)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout_9.addWidget(self.line_6)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_13 = QtGui.QLabel(TrainObjectDetectorParametersDialog)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_8.addWidget(self.label_13)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.label_7 = QtGui.QLabel(TrainObjectDetectorParametersDialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_8.addWidget(self.label_7)
        self.groupBox_2 = QtGui.QGroupBox(TrainObjectDetectorParametersDialog)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_5.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout_5.addWidget(self.radioButton_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8.addWidget(self.groupBox_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.retranslateUi(TrainObjectDetectorParametersDialog)
        QtCore.QMetaObject.connectSlotsByName(TrainObjectDetectorParametersDialog)

    def retranslateUi(self, TrainObjectDetectorParametersDialog):
        TrainObjectDetectorParametersDialog.setWindowTitle(_translate("TrainObjectDetectorParametersDialog", "SVM参数设置", None))
        self.label.setText(_translate("TrainObjectDetectorParametersDialog", "SVM参数说明：", None))
        self.label_8.setText(_translate("TrainObjectDetectorParametersDialog", "C：是SVM的正则化参数。代表软间隔，C越大则模型能更好地拟合数据，但是可能导致过拟合；", None))
        self.label_2.setText(_translate("TrainObjectDetectorParametersDialog", "C", None))
        self.label_9.setText(_translate("TrainObjectDetectorParametersDialog", "Epsilon：迭代停止条件。这个值越小则能使得模型预测的结果更准确，但会花费更长的时间训练。", None))
        self.label_3.setText(_translate("TrainObjectDetectorParametersDialog", "Epsilon", None))
        self.label_10.setText(_translate("TrainObjectDetectorParametersDialog", "Threads：训练过程中执行多少个线程用于计算。取决于你的CPU有几核，使用的核数越多越快。", None))
        self.label_4.setText(_translate("TrainObjectDetectorParametersDialog", "Threads", None))
        self.label_11.setText(_translate("TrainObjectDetectorParametersDialog", "detection_window_size：检测时滑动窗口的大小。", None))
        self.label_5.setText(_translate("TrainObjectDetectorParametersDialog", "detection_window_size", None))
        self.label_12.setText(_translate("TrainObjectDetectorParametersDialog", "add_left_right_image_flips：如果设置为真，则认定物体是左右对称的。在训练过程中会自动生成图片的左右对称的图片，\n"
"训练数据集的大小会增加1倍。", None))
        self.label_6.setText(_translate("TrainObjectDetectorParametersDialog", "add_left_right_image_flips", None))
        self.radioButton.setText(_translate("TrainObjectDetectorParametersDialog", "True", None))
        self.radioButton_2.setText(_translate("TrainObjectDetectorParametersDialog", "False", None))
        self.label_13.setText(_translate("TrainObjectDetectorParametersDialog", "be_verbose：如果设置为真，则在训练过程中，将过程信息打印在终端上。", None))
        self.label_7.setText(_translate("TrainObjectDetectorParametersDialog", "be_verbose", None))
        self.radioButton_3.setText(_translate("TrainObjectDetectorParametersDialog", "True", None))
        self.radioButton_4.setText(_translate("TrainObjectDetectorParametersDialog", "False", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TrainObjectDetectorParametersDialog = QtGui.QDialog()
    ui = Ui_TrainObjectDetectorParametersDialog()
    ui.setupUi(TrainObjectDetectorParametersDialog)
    TrainObjectDetectorParametersDialog.show()
    sys.exit(app.exec_())

