from tkinter import *
from tkinter import messagebox
import tkinter as tk
import pandas as pd
import tkinter.ttk as ttk

### 이름 아이디 비밀번호 전화번호, 주민번호, 자격증 토익점수

##################
###회원가입 UI
##################

User_CSV = "csv/User.csv"

class Register_UI ():

    def __init__(self,*args,**kwargs) :
        self.window = Tk()
        self.window.title("회원가입")
        self.window.geometry("450x600")
        self.window.resizable(width =FALSE,height=FALSE)


        

        #
        self.Name_label = Label(self.window,text="이름",font=("맑은고딕",11))
        self.Name_label.place(x=30,y=15)

        self.Name_Entry = Entry(self.window)
        self.Name_Entry.place(x=30,y=40,width=390,height=27)
        #
        self.Id_Re_label = Label(self.window,text="아이디",font=("맑은고딕",11))
        self.Id_Re_label.place(x=30,y=75)

        self.Id_Re_Entry = Entry(self.window)
        self.Id_Re_Entry.place(x=30,y=100,width=390,height=27)
        #
        self.Pw_Re_label = Label(self.window,text="비밀번호",font=("맑은고딕",11))
        self.Pw_Re_label.place(x=30,y=175)

        self.Pw_Re_Entry = Entry(self.window)
        self.Pw_Re_Entry.place(x=30,y=200,width=390,height=27)
        #
        self.Phone_label = Label(self.window,text="전화번호",font=("맑은고딕",11))
        self.Phone_label.place(x=30,y=235)

        ### 전화번호 엔트리 3개로 나눔 그리고 나중에 병합
        #self.Phone_Entry = Entry(self.window)
        #self.Phone_Entry.place(x=30,y=260,width=100,height=27)
        a = ["010","016","011"]
        self.Phone_combobox = ttk.Combobox(self.window,values=a,state="readonly")
        self.Phone_combobox.place(x=30,y=260,height=27,width=100)
        self.Phone_combobox.set("선택")
        self.Phone_Entry1 = Entry(self.window)
        self.Phone_Entry1.place(x=175,y=260,width=100,height=27)
        self.Phone_Entry2 = Entry(self.window)
        self.Phone_Entry2.place(x=320,y=260,width=100,height=27)
        #

        self.User_Number_label = Label(self.window,text="주민번호",font=("맑은고딕",11))
        self.User_Number_label.place(x=30,y=295)
        ### 주민번호 엔트리 2개로 나눔
        self.User_Number_Entry = Entry(self.window)
        self.User_Number_Entry.place(x=30,y=320,width=155,height=27)
        self.User_Number_Entry1 = Entry(self.window)
        self.User_Number_Entry1.place(x=265,y=320,width=155,height=27)
        #
        self.Spec_label = Label(self.window,text="자격증",font=("맑은고딕",11))
        self.Spec_label.place(x=30,y=355)

        self.Spec_Entry = Entry(self.window)
        self.Spec_Entry.place(x=30,y=380,width=390,height=27)
        #

        self.Toeic_text_label = Label(self.window,text="TOEIC 점수",font=("맑은고딕",11))
        self.Toeic_text_label.place(x=30,y=445)

        self.Toeic_Entry = Entry(self.window)
        self.Toeic_Entry.place(x=30,y=470,width=390,height=27)

        #ID 중복 확인 값
        self.Id_value = 0

        ##중복확인 버튼
        self.Id_check_button = Button(self.window,text="중복확인",bg="lightsteelblue",command=self.Id_Check)
        self.Id_check_button.place(x=340,y=140,width=80,height=30)

        ##자격증 찾기 버튼
        self.Spec_Search_button = Button(self.window,text="찾기",bg="lightsteelblue")
        self.Spec_Search_button.place(x=340,y=420,width=80,height=30)

        ##회원 가입 버튼
        self.Sign_Up_button = Button(self.window,text="회원가입",font=("맑은고딕",16,"bold"),\
            bg="cornflowerblue", fg="white",command=self.User_Edit_System)
        self.Sign_Up_button.place(x=30,y=518,width=390,height=60)

        self.window.mainloop()


    def User_Edit_System (self):
        

        self.df_User_CSV = pd.read_csv(User_CSV,encoding='CP949')
        #self.df_User_CSV = self.df_User_CSV.set_index(self.df_User_CSV['User_Phone'])
        
        

        self.name = self.Name_Entry.get()
        self.Id = self.Id_Re_Entry.get()
        self.Pw = self.Pw_Re_Entry.get()

        self.P = self.Phone_combobox.get()
        self.H = self.Phone_Entry1.get()
        self.O = self.Phone_Entry2.get()
        self.Phone = self.P + self.H + self.O

        self.N = self.User_Number_Entry.get()
        self.U = self.User_Number_Entry1.get()
        self.Number = self.N + self.U

        self.Spec = self.Spec_Entry.get()
        self.Toeic = self.Toeic_Entry.get()


        ##예외처리
        if self.Name_Entry.get() =="" :
            messagebox.showinfo("이름 에러","이름을 입력해주세요")
            return 0
        if len(self.Pw_Re_Entry.get())<8 :
            messagebox.showinfo("비밀번호 에러","비밀번호는 8자리 이상으로 입력해주세요")
            return 0
        if  not self.Phone.isdigit() :
            messagebox.showinfo("전화번호 에러","숫자만 입력해주세요")
            return 0
        if len(self.Phone_Entry1.get()) > 5 or len(self.Phone_Entry2.get()) > 5:
            messagebox.showinfo("전화번호 에러", "전화번호 자리에 숫자를 5개 이상 입력하셨습니다.")
            return 0
        if not len(self.User_Number_Entry.get()) == 6 :
            messagebox.showinfo("주민번호 에러","생년월일은 6자리로 입력해주세요")
            return 0
        if not len(self.User_Number_Entry1.get()) == 7 :
            messagebox.showinfo("주민번호 에러","주민번호 뒷자리는 7자리로 입력해주세요")
            return 0
        if int(self.Toeic_Entry.get()) > 990 or int(self.Toeic_Entry.get()) < 0 :
            messagebox.showinfo("토익점수 에러","0 ~ 990 범위안에서 입력해주세요")
            return 0 
        if  not self.Toeic_Entry.get().isdigit() :
            messagebox.showinfo("토익점수 에러","숫자만 입력해주세요")
            return 0

        if self.Id_value == 0 :
            messagebox.showinfo("중복에러","Id 중복확인을 먼저 해주세요")
            return 0
        
        
        

        df = pd.DataFrame.from_records([{'UserName' : self.name,'UserId':self.Id,'UserPw':self.Pw,'UserPhone':self.Phone,
        'UserNumber':self.Number,'UserSpec':self.Spec,'UserToeic':self.Toeic}])

        self.df_User_CSV = pd.concat([self.df_User_CSV, df])
        #self.df_User_CSV = self.df_User_CSV.set_index(self.df_User_CSV['User_Phone'])
        self.df_User_CSV.to_csv(User_CSV,index=False,encoding='cp949')
        messagebox.showinfo("회원 가입 완료 ","{} {} 이 등록되었습니다.".format(self.name,self.Phone))
        self.window.quit()
        self.window.destroy()
    

    ## id 중복확인 함수
    def Id_Check (self) :
        self.df_User_CSV = pd.read_csv(User_CSV,encoding='CP949')

        for i in self.df_User_CSV['UserId']:
            if i == self.Id_Re_Entry.get() :
                messagebox.showinfo("이름 중복","이름이 중복되었습니다")
                self.Id_value = 0
                return 0

        if self.Id_Re_Entry.get() not in self.df_User_CSV.loc[:,'UserId'] :
            self.Error_label1 = Label(self.window,text="사용가능한 ID 입니다",font=("맑은고딕",11),fg="green")
            self.Error_label1.place(x=150,y=140)
            self.Id_value = 1
            return 0
            
                

        

        

            


        
