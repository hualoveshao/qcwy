#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: jyroy
import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QListWidget,QStackedWidget
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
import pandas as pd
from PyQt5.QtCore import QSize, Qt
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

data = pd.read_csv("all_data.tsv",sep='\t')
last_data = pd.read_csv("last_all_data.tsv",sep='\t')

class Table(QWidget):
    def __init__(self,data,title):
        super(Table, self).__init__()
        self.title = title
        self.data = data
        self.initUI()

    def initUI(self):
        #设置标题与初始大小
        self.setWindowTitle(self.title)
        self.resize(600,800)

        ##水平布局
        layout=QHBoxLayout()
        #实例化表格视图（30*4）
        data_shape = self.data.shape
        tablewidget=QTableWidget(data_shape[0],data_shape[1])
        tablewidget.setHorizontalHeaderLabels(list(self.data.columns))
        layout.addWidget(tablewidget)
        data = self.data.values.tolist()
        for i in range(data_shape[0]):
            for j in range(data_shape[1]):
                itemContent='%s'% data[i][j]
                #为每个表格内添加数据
                tablewidget.setItem(i,j,QTableWidgetItem(itemContent))

        self.setLayout(layout)




#获取所有的显示图片列表
pic_index = 0
dirs = os.listdir("./picture")
pic_list = list(dirs)
class ListWidget(QListWidget):
    def clicked(self,item):
        if(item.text() == "分析图展示"):
            global pre_table,las_table,pic_index,main_wnd
            file_path = "file:///./picture/"+pic_list[pic_index]
            main_wnd.change_pic(file_path)
            pic_index+=1
            if(pic_index>=len(pic_list)):
                pic_index = 0
        elif(item.text() == "数据处理前"):
            #新开一个框展示处理前
            pre_table.show()

        else:
            #新开一个框展示处理后数据
            las_table.show()

class LeftTabWidget(QWidget):
    '''左侧选项栏'''
    def __init__(self):
        super(LeftTabWidget, self).__init__()
        self.setObjectName('物联网职位信息')
        
        self.setWindowTitle('物联网职位信息')
        with open('./set.qss', 'r') as f:   #导入QListWidget的qss样式
            self.list_style = f.read()

        self.main_layout = QHBoxLayout(self, spacing=0)     #窗口的整体布局
        self.main_layout.setContentsMargins(0,0,0,0)

        self.left_widget = ListWidget()     #左侧选项列表
        self.left_widget.setStyleSheet(self.list_style)
        self.main_layout.addWidget(self.left_widget)

        self.right_widget = QStackedWidget()
        self.main_layout.addWidget(self.right_widget)

        self._setup_ui()

    def _setup_ui(self):
        '''加载界面ui'''
        self.browser = QWebEngineView() 
        # self.left_widget.currentRowChanged.connect(self.right_widget.setCurrentIndex)   #list和右侧窗口的index对应绑定
        self.left_widget.itemClicked.connect(self.left_widget.clicked)

        self.left_widget.setFrameShape(QListWidget.NoFrame)    #去掉边框

        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  #隐藏滚动条
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str = ['分析图展示','数据处理前','数据处理后']
        url_list = ['job_num_wordcloud.html', 'edu_need.html', 'salary_bar.html', 'edu_salary_bar.html']

        for item in list_str:
            self.item = QListWidgetItem(item,self.left_widget)   #左侧选项的添加
            self.item.setSizeHint(QSize(30,60))
            self.item.setTextAlignment(Qt.AlignCenter)                  #居中显示
        self.browser.load(QUrl("file:///./picture/map_position.html"))
        self.right_widget.addWidget(self.browser)

    def change_pic(self,file_path):
        self.browser.load(QUrl(file_path))


app = QApplication(sys.argv)

main_wnd = LeftTabWidget()
main_wnd.show()
pre_table=Table(data,"数据处理前表格展示")
las_table=Table(last_data,"数据处理后表格展示")
app.exec()

