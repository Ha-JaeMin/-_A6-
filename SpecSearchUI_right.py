from tkinter import *
from tkinter.ttk import *
import pandas as pd
from UserDB import*
from JobDB import*


class SpecSearchUI_right(Frame) :
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller = controller
        self.parent= parent

        # 검색창(Entry, Button) 프레임
        job_name_frame = Frame(self.parent)

        self.JobImageLabel = Label(job_name_frame, width=5)  # 검색버튼
        self.JobImageLabel.pack(side='left')
        self.JobNameLabel = Label(job_name_frame, text = '',anchor="center",width=20)  # 검색창
        self.JobNameLabel.pack(side='left')

        job_name_frame.pack()

        self.s = Style(self).configure('self.Treeview', rowheight=80)

        # 테이블 생성
        self.SearchTable = Treeview(self.parent, selectmode='browse',height=3,style ='self.Treeview')
        self.SearchTable['columns'] = ('one','two','three')
        self.SearchTable['show'] = 'headings'

        self.SearchTable.pack(padx=20)

        # 테이블 속성 설정
        self.SearchTable.column("one", width=50,anchor='center' )
        self.SearchTable.heading("one", text="자격증", anchor="center")

        self.SearchTable.column("two", width=180, )
        self.SearchTable.heading("two", text="회원 SPEC", anchor="center")

        self.SearchTable.column("three", width=180, )
        self.SearchTable.heading("three", text="직업", anchor="center")
        # 테이블 값 입력
        job_list = [('필수','',''),
                    ('관련','',''),
                    ('TOEIC','',''),
                    ]

        for i in range(len(job_list)):
            self.SearchTable.insert('', 'end', values=job_list[i])

        #확인버튼
        self.Confirm_Button = Button(self.parent, text = '확인',width = 30,command= lambda : self.forget())
        self.Confirm_Button.pack(pady=40)

    def forget(self):
        self.parent.pack_forget()

    def modify(self,job_name,user_name):
        #직업DB 객체 생성
        self.jobDB = JobDB()
        self.jobDB.set_index_key(job_name)

        #회원DB 객체 생성
        self.userDB = UserDB()
        self.userDB.set_index_key(user_name)

        #선택한 직업의 이름으로 레이블 변경
        self.JobNameLabel.configure(text=job_name)

        #기존 데이터 제거
        for item in self.SearchTable.get_children():
            self.SearchTable.delete(item)

        # 테이블 값 입력
        job_list = [('자격증',('\n').join(self.userDB.get_Certifi().split(', ')), ('\n').join(self.jobDB.get_Certifi().split(', '))),
                    ('TOEIC',self.userDB.get_Toeic(), self.jobDB.get_Toeic()),
                    ]
        for i in range(len(job_list)):
            self.SearchTable.insert('', 'end', values=job_list[i])

