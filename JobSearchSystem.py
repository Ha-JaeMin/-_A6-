from JobDB import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class JobSearchSystem():
    def __init__(self):
        self.jobDB = JobDB()
        self.df_Job = self.jobDB.get_df()
    def SearchClick(self,str,treeView):
        # 테이블 초기화
        for item in treeView.get_children():
            treeView.delete(item)
        df_contains = self.df_Job[self.df_Job['jobName'].str.contains(str)]
        for select_name in df_contains['jobName']:
            name= df_contains['jobName'].loc[select_name]
            treeView.insert('','end',text='',value=name,iid=name)

    def CheckClick(self,index_key,window,DepartmentText,informationText,SpecText,LinkText,nameLabel,moneyText,PossibilityText,employText):
        self.jobDB.set_index_key(index_key)
        name = self.jobDB.get_name()
        information = self.jobDB.get_information()
        Certifi = self.jobDB.get_Certifi()
        Department = self.jobDB.get_Department()
        Wage = self.jobDB.get_Wage()
        Prospect = self.jobDB.get_Prospect()
        Equality = self.jobDB.get_Equality()
        View = self.jobDB.get_View()
        Sex = self.jobDB.get_Sex()
        Link = self.jobDB.get_Link()

        self.fig = Figure(figsize=(7,4), dpi=70)  #그리프 그릴 창 생성
        self.fig2 = Figure(figsize=(5,4), dpi=80)  #그리프 그릴 창 생성
        possibility = ["보상","고용안정","발전가능성","근무여건","전문성","고용평등"]
        sexname = ["남자","여자"]
        nameLabel.config(text=name)
        informationText.configure(text=information)
        SpecText.configure(text=Certifi)
        DepartmentText.configure(text=Department)
        LinkText.delete('1.0','end')
        Wage = str(round(Wage))
        moneyText.configure(text="평균 "+Wage+"만원")
        PossibilityText.configure(text=Prospect)
        employText.configure(text=Equality)
        LinkText.insert('1.0',Link)
        list_int = View.split(',')
        list_int = list(map(int,list_int))

        self.fig.add_subplot(1,1,1).barh(possibility,list_int,color=["black","red","blue","green","yellow","gray"])#창에 그래프 하나 추가
        canvas = FigureCanvasTkAgg(self.fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().place(x=440,y=440)
        list_float = Sex.split(",")
        self.fig2.add_subplot(1,1,1).pie(list_float,labels=sexname,autopct="%.1f",colors=["red","blue"])#창에 그래프 하나 추가
        canvas2 = FigureCanvasTkAgg(self.fig2,master=window)
        canvas2.draw()
        canvas2.get_tk_widget().place(x=960,y=100)
