# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\PyQt\Project\my_dlib_face_detection_application\ShapeDetectorGui.ui'
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

class Ui_ShapePredictorDialog(object):
    def setupUi(self, ShapePredictorDialog):
        ShapePredictorDialog.setObjectName(_fromUtf8("ShapePredictorDialog"))
        ShapePredictorDialog.resize(1071, 676)
        self.verticalLayout_3 = QtGui.QVBoxLayout(ShapePredictorDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(ShapePredictorDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.train_tab = QtGui.QWidget()
        self.train_tab.setObjectName(_fromUtf8("train_tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.train_tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.train_tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.train_tab)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.train_tab)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_6 = QtGui.QPushButton(self.train_tab)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_2 = QtGui.QPushButton(self.train_tab)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtGui.QTextBrowser(self.train_tab)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.train_tab, _fromUtf8(""))
        self.test_tab = QtGui.QWidget()
        self.test_tab.setObjectName(_fromUtf8("test_tab"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.test_tab)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_4 = QtGui.QLabel(self.test_tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.test_tab)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_3 = QtGui.QPushButton(self.test_tab)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(self.test_tab)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_6.addWidget(self.line_2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.test_tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.graphicsView = QtGui.QGraphicsView(self.test_tab)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_4.addWidget(self.graphicsView)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButton_4 = QtGui.QPushButton(self.test_tab)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.line = QtGui.QFrame(self.test_tab)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_7.addWidget(self.line)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.label_3 = QtGui.QLabel(self.test_tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.graphicsView_2 = QtGui.QGraphicsView(self.test_tab)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.verticalLayout_5.addWidget(self.graphicsView_2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.pushButton_5 = QtGui.QPushButton(self.test_tab)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.test_tab, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)

        self.retranslateUi(ShapePredictorDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ShapePredictorDialog)

    def retranslateUi(self, ShapePredictorDialog):
        ShapePredictorDialog.setWindowTitle(_translate("ShapePredictorDialog", "人脸特征点检测器", None))
        self.label.setText(_translate("ShapePredictorDialog", "<html><head/><body><p>说明：</p><p>通过导入xml文件（使用工具imglab制作）来导入数据集 </p><p>关于如何制作数据集，详细请参考：</p><p><a href=\"http://blog.csdn.net/hongbin_xu/article/details/78511923\"><span style=\" text-decoration: underline; color:#0000ff;\">python dlib学习（八）：训练人脸特征点检测器</span></a></p></body></html>", None))
        self.pushButton.setText(_translate("ShapePredictorDialog", "导入训练数据集(XML)", None))
        self.pushButton_6.setText(_translate("ShapePredictorDialog", "训练参数设置", None))
        self.pushButton_2.setText(_translate("ShapePredictorDialog", "训练模型", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.train_tab), _translate("ShapePredictorDialog", "训练", None))
        self.label_4.setText(_translate("ShapePredictorDialog", "说明： \n"
"导入前面训练生成的模型文件，检测人脸的68个特征点。 \n"
"生成模型的默认名称为：\"predictor.dat\"", None))
        self.pushButton_3.setText(_translate("ShapePredictorDialog", "导入模型文件", None))
        self.label_2.setText(_translate("ShapePredictorDialog", "原图", None))
        self.pushButton_4.setText(_translate("ShapePredictorDialog", "打开图片", None))
        self.label_3.setText(_translate("ShapePredictorDialog", "结果", None))
        self.pushButton_5.setText(_translate("ShapePredictorDialog", "检测目标", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.test_tab), _translate("ShapePredictorDialog", "测试", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ShapePredictorDialog = QtGui.QDialog()
    ui = Ui_ShapePredictorDialog()
    ui.setupUi(ShapePredictorDialog)
    ShapePredictorDialog.show()
    sys.exit(app.exec_())
