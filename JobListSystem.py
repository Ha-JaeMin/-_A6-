from tkinter import *
from tkinter.ttk import*
from JobDB import*

class JobListSystem (Tk):
    def __init__(self):
        #직업 DB 생성
        jobDB = JobDB()
        self.df_Job = jobDB.get_df()

    def list_call(self,treeView):
        # 테이블 값 입력 (직업이름, 관련학과, 전망)
        for index,row in self.df_Job.iterrows():
            treeView.insert('','end',text='',value=(row['jobName'],row['jobDepartment'],row['jobProspect']))


