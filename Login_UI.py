from tkinter import *
from tkinter import messagebox
from Register_UI import Register_UI
from UserMainUI import Start_Main
import pandas as pd
import msvcrt

## 아아
User_CSV = "csv/User.csv"

############################
### 로그인 화면
############################

class Login_Start():

    def __init__(self):
        self.window =Tk()
        self.checkbutton = Button(self.window)
        self.window.title("로그인")
        self.window.geometry("550x550")
        self.window.resizable(width =FALSE,height=FALSE)

        self.label1 = Label(self.window,text="직업",font=("맑은고딕",30,"bold"))
        self.label1.place(x=80,y=70)

        self.label2 = Label(self.window,text="관리 프로그램",font=("맑은고딕",30,"bold"))
        self.label2.place(x=80,y=120)

        self.Id_text_label = Label(self.window,text="아이디",font=("맑은고딕",11))
        self.Id_text_label.place(x=80,y=210)

        self.Id_Entry = Entry(self.window)
        self.Id_Entry.place(x=80,y=238,width=390,height=30)

        self.Pw_text_label = Label(self.window,text="비밀번호",font=("맑은고딕",11))
        self.Pw_text_label.place(x=80,y=277)

        self.Pw_Entry = Entry(self.window,show='*')
        self.Pw_Entry.place(x=80,y=305,width=390,height=30) ###

        self.Login_button = Button(self.window,text="로 그 인",bg="cornflowerblue",font=("맑은고딕",18,"bold"),\
            fg="white",command=self.login)## 로그인 버튼
        self.Login_button.place(x=80,y=360,width=390,height=60)

        self.sign_up_button = Button(self.window,text="회원가입",bg="grey",font=("맑은고딕",13)\
            ,command= Register_UI) ## 회원가입 버튼 
        self.sign_up_button.place(x=145,y=450,width=260,height=50)

   
        self.window.mainloop()

    ### 로그인 버튼 기능
    def login(self):
        self.df_User_CSV = pd.read_csv(User_CSV,encoding='CP949')
        ### for in 을 써서 userid의 열의 갯수를 b에 카운트하고 b 값과 유저 데이터프레임 행 개수가 같으면 
        ### Id가 일치하지 않는것
        
        b = 0
        
        ### 아이디 불일치 예외처리    
        for i in self.df_User_CSV['UserId'] :
            if i == self.Id_Entry.get() :
                a = 0
            else :
                b+=1
        
        if len(self.df_User_CSV) == b :
            messagebox.showinfo("로그인 에러","아이디가 일치하지 않습니다.")
            return 0

                
        ## 비밀번호 일치하면 UserMainUI 실행 비밀번호 틀리면 예외처리
        self.get_info = self.df_User_CSV.loc[self.df_User_CSV['UserId']==self.Id_Entry.get()]


        for i in self.get_info['UserPw'] :
            if i == self.Pw_Entry.get() :
                self.window.quit()
                self.window.destroy()
                aaa = Start_Main(self.get_info)
                aaa.geometry("430x550")
                aaa.resizable(width=False,height=False)

                aaa.mainloop()    

                
                
            else:
                messagebox.showinfo("로그인 에러","아이디나 비밀번호가 일치하지 않습니다.")
                return 0





abc = Login_Start()