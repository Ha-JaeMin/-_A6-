import tkinter as tk
from tkinter import Button, Label, PhotoImage, font  as tkfont
from PIL import Image
from PIL import Image,ImageTk
from matplotlib import container

from Job_Search import JobSearch, JobSearchSystem # python 3

IMG_WIDTH = 70
IMG_HEIGHT = 70
class Start_Main(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        chageFrame= tk.Frame(self,width=50,bg="gray80")
        chageFrame.pack(side="left",fill="y")
        self.btn_ch1 = Button(chageFrame,padx=20,pady=20,command=lambda: self.show_frame("StartPage"),relief="flat",bg="gray80")
        img = Image.open("Image/Home.jpg")
        resize_img = img.resize((IMG_WIDTH,IMG_HEIGHT))
        img_tk = ImageTk.PhotoImage(resize_img,master=chageFrame)
        self.btn_ch1.configure(image=img_tk, width=IMG_WIDTH, height=IMG_HEIGHT)
        self.btn_ch1.image = img_tk
        self.btn_ch1.pack(sid="top")
        self.btn_ch2 = Button(chageFrame,padx=20,pady=20,command=lambda: self.show_frame("OtherPage"),relief="flat",bg="gray80")
        img = Image.open("Image/User.jpg")
        resize_img = img.resize((IMG_WIDTH,IMG_HEIGHT))
        img_tk = ImageTk.PhotoImage(resize_img,master=chageFrame)
        self.btn_ch2.configure(image=img_tk, width=IMG_WIDTH, height=IMG_HEIGHT)
        self.btn_ch2.image = img_tk
        self.btn_ch2.pack(sid="top")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, OtherPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Job_SearchButton = Button(self,text="직업 검색",width=30,pady=10,font=("맑은고딕",12),background="SlateGray1",anchor="center",command=self.Job_Search)
        Job_SearchButton.place(x=25,y=50)
        Job_ListButton = Button(self,text="직업목록조회",width=30,pady=10,font=("맑은고딕",12),background="SlateGray1",anchor="center")
        Job_ListButton.place(x=25,y=150)
        User_suggestion = Button(self,text="회원맞춤직업추천",width=30,pady=10,font=("맑은고딕",12),background="SlateGray1",anchor="center")
        User_suggestion.place(x=25,y=250)
        Spec_SearchButton = Button(self,text="SPEC 검색",width=30,pady=10,font=("맑은고딕",12),background="SlateGray1",anchor="center")
        Spec_SearchButton.place(x=25,y=350)
    def Job_Search(self):
        Job_Search = JobSearchSystem()


class OtherPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        TitleLabel = Label(self,text="프로필",font=("맑은고딕",16,"bold"),anchor="center")
        TitleLabel.place(x=30,y=30)
        NameTitle = Label(self,text="이름 : ",font=("맑은고딕",12),anchor="center")
        NameTitle.place(x=30,y=100)
        Name = Label(self,text="조준호",font=("맑은고딕",12),anchor="center")
        Name.place(x=80,y=100)
        IdTitle = Label(self,text ="아이디 : ",font=("맑은고딕",12),anchor="center")
        IdTitle.place(x=30,y=130)
        Id = Label(self,text="hiwhwnsgh",font=("맑은고딕",12),anchor="center")
        Id.place(x=100,y=130)
        ToeicTitle = Label(self,text="TOEIC : ",font=("맑은고딕",12),anchor="center")
        ToeicTitle.place(x=30,y=160)
        Toeic = Label(self,text="890점",font=("맑은고딕",12),anchor="center")
        Toeic.place(x=100,y=160)
        SpecTitel = Label(self,text="자격증",font=("맑은고딕",12),anchor="center")
        SpecTitel.place(x=30,y=190)
        Spec = Label(self,text="없음",font=("맑은고딕",12),anchor="e")
        Spec.place(x=30,y=210)
        EditButton = Button(self,text="편집",font=("맑은고딕",11),width=10,background="gray85",relief="flat")
        EditButton.place(x=230,y=95)
app = Start_Main()
app.geometry("430x550")
app.mainloop()