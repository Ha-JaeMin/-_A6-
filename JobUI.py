from asyncio.windows_events import NULL
from cProfile import label
from calendar import c
from faulthandler import disable
from operator import index
from tkinter import messagebox
from cv2 import line
import pandas as pd
import numpy as np
import platform
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import ttk
from JobSearchSystem import *
from pyparsing import null_debug_action

DIR_CSV_JOB = "Job.csv"

class JobUI():
    def __init__(self):
        self.window = Tk()
        self.action = JobSearchSystem()
        self.checkButton = Button(self.window)
        self.window.title("직업조회프로그램")
        self.window.geometry("1400x800")
        self.window.resizable(width=False,height=False)
        # TreeView 기본 설정
        columns = ["직업이름"]
        width = [400]
        self.Table =ttk.Treeview(self.window,columns=columns,displaycolumns=columns)
        self.Table.place(x=10,y=60)
        for i in range(len(columns)):
            self.Table.column(columns[i],width=width[i],anchor="center")
            self.Table.heading(columns[i],text=columns[i],anchor="center")
        self.Table["show"]= "headings"
        self.checkButton.config(width=56,text="선택",command=self.Checkbtn)
        self.checkButton.place(x=10,y=300)

        self.nameLabel = Label(self.window,font=("맑은고딕",20,"bold"))
        self.nameLabel.place(x=440,y=30)


        self.information = Label(self.window,text="직업정보",font=("맑은고딕",10,"bold"))

        self.informationText = Label(self.window,width=70,relief="flat",height=8,font=("맑은고딕",10),wraplength=520,anchor='nw')
        self.informationText.place(x=440,y=90)
        
        self.Department = Label(self.window,text="관련학과",font=("맑은고딕",10,"bold"))

        self.DepartmentText = Label(self.window,width=38,height=3,anchor='nw',wraplength=250)
        self.DepartmentText.place(x=440,y=220)

        self.Spec = Label(self.window,text="관련자격증",font=("맑은고딕",10,"bold"))

        self.SpecText = Label(self.window,width=29,height=3,wraplength=200,anchor='nw')
        self.SpecText.place(x=730,y=220)

        self.money = Label(self.window,text="임금",font=("맑은고딕",10,"bold"))
        self.moneyText= Label(self.window)
        self.moneyText.place(x=440,y=320)

        self.Possibility = Label(self.window,text="발전가능성",font=("맑은고딕",10,"bold"))
        self.PossibilityText = Label(self.window)
        self.PossibilityText.place(x=620,y=320)

        self.employ = Label(self.window,text="고용가능성",font=("맑은고딕",10,"bold"))
        self.employText = Label(self.window)
        self.employText.place(x=800,y=320)

        self.view = Label(self.window,text="직업 전망",font=("맑은고딕",10,"bold"))

        self.sexLabel = Label(self.window,text="남녀 분포도",font=("맑은고딕",10,"bold"))

        self.Link = Label(self.window,text="관련 링크",font=("맑은고딕",10,"bold"))
        self.LinkText = Text(self.window,font=("맑은고딕",10),width=57,height=2)

        
        

        if platform.system() == 'Windows':
            plt.rc('font', family='Malgun Gothic')
        elif platform.system() == 'Darwin': # Mac
            plt.rc('font', family='AppleGothic')
        else: #linux
            plt.rc('font', family='NanumGothic')

        # 그래프에 마이너스 표시가 되도록 변경
        plt.rcParams['axes.unicode_minus'] = False
        
    def place_widget(self):
        self.information.place(x=440,y=70)
        self.Department.place(x=440,y=200)
        self.Spec.place(x=730,y=200)
        self.money.place(x=440,y=300)
        self.Possibility.place(x=620,y=300)
        self.employ.place(x=800,y=300)
        self.view.place(x=440,y=400)
        self.sexLabel.place(x=960,y=70)
        self.Link.place(x=960,y=440)
        self.LinkText.place(x=960,y=460)
        
    def Checkbtn(self):
        index_key = self.Table.focus()
        if index_key == '':
            messagebox.showerror("알림","직업을 선택해주세요")
        else:
            self.place_widget()
            self.action.CheckClick(index_key,self.window,self.DepartmentText,self.informationText,self.SpecText,self.LinkText,self.nameLabel,self.moneyText,self.PossibilityText,self.employText)

        
    
    def mainloop(self):
        self.window.mainloop()
    
