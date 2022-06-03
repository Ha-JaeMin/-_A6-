from tkinter import *
import os

# 관리자 메인 화면


class ManagerMainUI():
    def JobAdd():
        os.system("python Job_Add_UI.py")

    def JobEdit():
        os.system("python Job_Edit_UI.py")

    def JobDelete():
        os.system("python Job_Delete_UI.py")

    def UserSearch():
        os.system("python searchrec.py")

    def UserDelete():
        os.system("python addrecord.py")

    win = Tk()
    win.title("관리자 메인 화면")
    win.geometry("1200x600+200+100")  # 너비, 높이, 왼쪽 끝에서 거리, 윗쪽 끝에서 거리
    win.resizable(0, 0)

    JobAddButton = Button(win, text="직업 등록", fg="black",
                          relief="raise", font=("맑은고딕", 13), width=20, height=3, bg="#DAE3F3", command=JobAdd)
    JobAddButton.pack(pady=10)
    JobEditButton = Button(win, text="직업 수정", fg="black",
                           relief="raise", font=("맑은고딕", 13), width=20, height=3, bg="#DAE3F3", command=JobEdit)
    JobEditButton.pack(pady=10)
    JobDeleteButton = Button(win, text="직업 삭제", fg="black",
                             relief="raise", font=("맑은고딕", 13), width=20, height=3, bg="#DAE3F3", command=JobDelete)
    JobDeleteButton.pack(pady=10)
    UserSearchButton = Button(win, text="회원 검색", fg="black",
                              relief="raise", font=("맑은고딕", 13), width=20, height=3, bg="#DAE3F3", command=UserSearch)
    UserSearchButton.pack(pady=10)
    UserDeleteButton = Button(win, text="회원 삭제", fg="black",
                              relief="raise", font=("맑은고딕", 13), width=20, height=3, bg="#DAE3F3", command=UserDelete)
    UserDeleteButton.pack(pady=10)

    win.mainloop()
