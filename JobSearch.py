from tkinter import *
from tkinter import messagebox
from JobUI import *

class JobSearch(JobUI):
    def __init__(self):
        JobUI.__init__(self)
        self.Search = Entry(self.window,width=55)
        self.Search.place(x=10,y=30)
        self.SearchButton = Button(self.window,text="검색",command=self.Searchbtn)
        self.SearchButton.place(x=375,y=30)
    def Searchbtn(self):
        index_key = self.Search.get()
        self.action.SearchClick(index_key,self.Table)
        self.Search.delete("0","end")