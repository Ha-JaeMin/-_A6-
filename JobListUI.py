from tkinter import *
from tkinter.ttk import*
from JobDB import*
from JobListSystem import*


class JobListUI (Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("직업 목록 조회")
        self.geometry("800x500")
        self.resizable(False,False)

        #직업 DB 생성
        jobDB = JobDB()
        self.df_Job = jobDB.get_df()

        self.label = Label(self,text='직억 목록 조회',font=("맑은고딕",12),anchor="center",relief="flat")
        self.label.pack(pady=10)
        #테이블과 스크롤바를 넣을 프레임 생성
        frame = Frame(self)

        #테이블 생성
        self.JobListTable = Treeview(frame, selectmode = 'browse',height=15)
        self.JobListTable['columns'] = ('one','two','three')
        self.JobListTable['show'] = 'headings'
        self.JobListTable.pack(side='left')

        #스크롤바 생성
        self.scrollbar = Scrollbar(frame,command=self.JobListTable.yview)
        self.scrollbar.pack(side='right',fill='y')
        self.JobListTable.configure(yscrollcommand=self.scrollbar.set)

        #테이블 속성 설정
        self.JobListTable.column("one",width=150,)
        self.JobListTable.heading("one",text = "직업이름",anchor="center")

        self.JobListTable.column("two",width=300,)
        self.JobListTable.heading("two",text = "관련학과",anchor="center")

        self.JobListTable.column("three",width=100,)
        self.JobListTable.heading("three",text = "전망",anchor="center")

        frame.pack(pady=10)

        self.action = JobListSystem()
        self.action.list_call(self.JobListTable)



app = JobListUI()
app.mainloop()
