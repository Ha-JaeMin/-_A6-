from tkinter import *
from tkinter.ttk import *
from SpecSearchSystem import*
import pandas as pd


class SpecSearchUI (Tk) :
    def __init__(self):
        Tk.__init__(self)
        #self.window = Tk()
        self.action= SpecSearchSystem()
        self.title("스펙 검색 조회")
        self.geometry("800x400")
        self.resizable(False, False)
        # 왼쪽 검색창
        left_frame = Frame(self,width = 200)
        left_frame.pack(side='left')
        # 검색창(Entry, Button) 프레임
        Search_frame = Frame(left_frame)

        self.SearchEntry = Entry(Search_frame, width=20)  # 검색창
        self.SearchEntry.grid(row=1, column=1)
        self.SearchButton = Button(Search_frame, width=5, text="찾기"
                                   ,command= lambda : self.action.SearchClick(self.SearchEntry.get(),self.SearchTable))  # 검색버튼
        self.SearchButton.grid(row=1, column=2)

        Search_frame.pack(padx=50, pady=10)

        # 검색결과 테이블
        # 테이블과 스크롤바를 넣을 프레임 생성
        result_frame = Frame(left_frame)

        # 테이블 생성
        self.SearchTable = Treeview(result_frame, selectmode='browse')
        self.SearchTable['columns'] = ('one')
        self.SearchTable['show'] = 'headings'
        self.SearchTable.pack(side='left')

        # 스크롤바 생성
        self.scrollbar = Scrollbar(result_frame, command=self.SearchTable.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.SearchTable.configure(yscrollcommand=self.scrollbar.set)

        # 테이블 속성 설정
        self.SearchTable.column("one", width=200, )
        self.SearchTable.heading("one", text="직업", anchor="center")

        result_frame.pack(padx=50)  # 검색 결과 테이블 프레임 부착

        #선택버튼
        self.ChoiceButton = Button(left_frame, text = '선택',width = 30
                                   ,command=lambda:self.choice(self.SearchTable.focus(),'류준호'))
        self.ChoiceButton.pack(pady=40)

        #오른쪽 프레임
        self.right_frame = Frame(self)
        self.right_frame.pack(side='right',expand=True)
        self.frame = SpecSearchUI_right(parent=self.right_frame, controller=self)   #오른쪽 화면 객체
        self.right_frame.pack_forget()


    def choice(self,job_name,user_name):  #선택버튼시 호출되는 이벤트
        self.frame.modify(job_name,user_name)
        self.right_frame.pack(side='right',expand=True)


app = SpecSearchUI()
app.mainloop()