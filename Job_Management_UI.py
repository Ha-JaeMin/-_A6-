from tkinter import *
import csv
from tkinter import ttk
from tkinter import messagebox


class JobManagementUI():
    def __init__(self, title, label, buttonName):
        win = Tk()
        win.title(title)
        win.geometry("600x500+400+100")
        win.resizable(0, 0)
        name = StringVar()
        information = StringVar()
        department = StringVar()
        certifi = StringVar()
        toeic = StringVar()
        wage = StringVar()
        prosp = StringVar()
        sex = StringVar()

        Label(win, text=label,
              font=("맑은고딕", 16)).place(x=30, y=2)
        Label(win, text="직업 이름",
              font=("맑은고딕", 12)).place(x=30, y=50)
        Label(win, text="직업 정보",
              font=("맑은고딕", 12)).place(x=30, y=90)
        Label(win, text="직업 관련 학과",
              font=("맑은고딕", 12)).place(x=30, y=130)
        Label(win, text="직업 자격증",
              font=("맑은고딕", 12)).place(x=30, y=170)
        Label(win, text="직업 토익 점수",
              font=("맑은고딕", 12)).place(x=30, y=210)
        Label(win, text="직업 임금",
              font=("맑은고딕", 12)).place(x=30, y=250)
        Label(win, text="직업 전망",
              font=("맑은고딕", 12)).place(x=30, y=290)
        Label(win, text="직업 남성 비율",
              font=("맑은고딕", 12)).place(x=30, y=330)

        if title == "직업 삭제 화면":
            JobNameEntry = Entry(win, textvariable=name,
                                 width=50, state="disable")
            JobNameEntry.place(x=160, y=50)

            JobInformationEntry = Entry(
                win, textvariable=information, width=50, state="disable")
            JobInformationEntry.place(x=160, y=90)

            JobDepartmentEntry = Entry(
                win, textvariable=department, width=50, state="disable")
            JobDepartmentEntry.place(x=160, y=130)

            JobCertifiEntry = Entry(
                win, textvariable=certifi, width=50, state="disable")
            JobCertifiEntry.place(x=160, y=170)

            JobToeicEntry = Entry(win, textvariable=toeic,
                                  width=50, state="disable")
            JobToeicEntry.place(x=160, y=210)

            JobWageEntry = Entry(win, textvariable=wage,
                                 width=50, state="disable")
            JobWageEntry.place(x=160, y=250)

            JobProspEntry = Entry(win, textvariable=prosp,
                                  width=50, state="disable")
            JobProspEntry.place(x=160, y=290)

            JobMaleEntry = Entry(win, textvariable=sex,
                                 width=50, state="disable")
            JobMaleEntry.place(x=160, y=330)
        else:
            JobNameEntry = Entry(win, textvariable=name, width=50)
            JobNameEntry.place(x=160, y=50)

            JobInformationEntry = Entry(
                win, textvariable=information, width=50)
            JobInformationEntry.place(x=160, y=90)

            JobDepartmentEntry = Entry(win, textvariable=department, width=50)
            JobDepartmentEntry.place(x=160, y=130)

            JobCertifiEntry = Entry(win, textvariable=certifi, width=50)
            JobCertifiEntry.place(x=160, y=170)

            JobToeicEntry = Entry(win, textvariable=toeic, width=50)
            JobToeicEntry.place(x=160, y=210)

            JobWageEntry = Entry(win, textvariable=wage, width=50)
            JobWageEntry.place(x=160, y=250)

            JobProspEntry = Entry(win, textvariable=prosp, width=50)
            JobProspEntry.place(x=160, y=290)

            JobMaleEntry = Entry(win, textvariable=sex, width=50)
            JobMaleEntry.place(x=160, y=330)


# 직업 이름을 읽어와서 저장
        JobNameList = []
        file = open("JobDB.csv")
        read = csv.reader(file, delimiter=",")
        for row in read:
            JobNameList.append(row[0])
        print(JobNameList)
        file.close()

# 직업등록 중복체크
        b = 0

        def JobCheck():
            a = 1
            global b
            for name in JobNameList:
                if name == JobNameEntry.get():
                    a = 0
                    b = 0
            if JobNameEntry.get() == "":
                b = 1
            elif a == 1:
                b = 2

            if a == 0:
                messagebox.showinfo(buttonName, "이미 존재하는 직업입니다.")
                a = 1
            elif b == 1:
                messagebox.showinfo(buttonName, "직업 이름을 적으세요.")
                b = 0
            elif b == 2:
                messagebox.showinfo(buttonName, "등록 가능합니다.")
                print(b)

# 직업등록
        def JobAddDB():
            try:
                if (JobInformationEntry.get() == "" or JobDepartmentEntry.get() == "" or JobCertifiEntry.get() == ""
                        or JobToeicEntry.get() == "" or JobWageEntry.get() == "" or JobProspEntry.get() == "" or JobMaleEntry.get() == ""):
                    messagebox.showinfo(buttonName, "빈 칸이 있습니다.")
                else:
                    global b
                    print(b)
                    CheckBox = messagebox.askquestion(
                        buttonName, "직업을 등록하시겠습니까?")
                    if CheckBox == 'yes':
                        if b == 2:
                            file = open("JobDB.csv", "a")
                            csv_writer = csv.writer(
                                file, delimiter=",", lineterminator="\n")
                            csv_writer.writerow([JobNameEntry.get(), JobInformationEntry.get(), JobDepartmentEntry.get(),
                                                JobCertifiEntry.get(), JobToeicEntry.get(), JobWageEntry.get(), JobProspEntry.get(), JobMaleEntry.get(), 0])
                            messagebox.showinfo(buttonName, "등록이 완료 되었습니다.")
                            b = 0
                            name.set("")
                            information.set("")
                            department.set("")
                            certifi.set("")
                            toeic.set("")
                            wage.set("")
                            prosp.set("")
                            sex.set("")
                        else:
                            messagebox.showinfo(buttonName, "중복확인 해주세요.")
                    else:
                        messagebox.showinfo(buttonName, "등록이 되지 않았습니다.")
            except(NameError):
                messagebox.showinfo(buttonName, "중복확인 해주세요.")

# 직업 선택하면 빈 칸을 채워준다
        def JobLoad(value):
            file = open("JobDB.csv")
            reader = csv.reader(file, delimiter=",")
            print(value)
            for row in reader:
                if value == row[0]:
                    print(row[4])
                    information.set(row[1])
                    department.set(row[2])
                    certifi.set(row[3])
                    toeic.set(row[4])
                    wage.set(row[5])
                    prosp.set(row[6])
                    sex.set(row[7])
            file.close()

# 직업수정
        def JobEditDB():
            data = []
            file = open("JobDB.csv", "r")
            read = csv.reader(file, delimiter=",")
            for row in read:
                if row[0] == JobNameEntry.get():
                    data.append([JobNameEntry.get(), JobInformationEntry.get(), JobDepartmentEntry.get(),
                                 JobCertifiEntry.get(), JobToeicEntry.get(), JobWageEntry.get(), JobProspEntry.get(), JobMaleEntry.get()])
                else:
                    data.append(row)
            file.close()

            if (JobInformationEntry.get() == "" or JobDepartmentEntry.get() == "" or JobCertifiEntry.get() == ""
                    or JobToeicEntry.get() == "" or JobWageEntry.get() == "" or JobProspEntry.get() == "" or JobMaleEntry.get() == ""):
                messagebox.showinfo(buttonName, "빈 칸이 있습니다.")
            else:
                file = open("JobDB.csv", "w")
                write = csv.writer(file, delimiter=",", lineterminator="\n")
                write.writerows(data)
                file.close()
                messagebox.showinfo(buttonName, "수정이 완료 되었습니다.")

        def JobDeleteDB():
            data = []
            file = open("JobDB.csv", "r")
            read = csv.reader(file, delimiter=",")
            for row in read:
                if row[0] == JobNameEntry.get():
                    pass
                else:
                    data.append(row)
            file.close()

            CheckBox = messagebox.askquestion(
                buttonName, "정말 삭제하시겠습니까?")
            if CheckBox == 'yes':
                file = open("JobDB.csv", "w")
                write = csv.writer(file, delimiter=",", lineterminator="\n")
                write.writerows(data)
                file.close()
                messagebox.showinfo(buttonName, "삭제가 완료 되었습니다.")
            else:
                messagebox.showinfo(buttonName, "삭제가 되지 않았습니다.")

# 등록, 수정, 삭제에 따라 버튼이 달라짐
        if(buttonName == "직업 등록"):
            CheckButton = Button(win, text="중복 확인", font=(
                "맑은고딕", 9), command=JobCheck).place(x=520, y=46)
            OkButton = Button(win, text=buttonName, font=(
                "맑은고딕", 9), width=17, height=2, command=JobAddDB, bg="#DAE3F3").place(x=160, y=370)
        elif(buttonName == "직업 수정"):
            JobChoice = ttk.OptionMenu(win, name, "직업 선택", *
                                       JobNameList, command=JobLoad).place(x=518, y=46)
            OkButton = Button(win, text=buttonName, font=(
                "맑은고딕", 9), width=17, height=2, command=JobEditDB, bg="#DAE3F3").place(x=160, y=370)
        elif(buttonName == "직업 삭제"):
            JobChoice = ttk.OptionMenu(win, name, "직업 선택", *
                                       JobNameList, command=JobLoad).place(x=518, y=46)
            OkButton = Button(win, text=buttonName, font=(
                "맑은고딕", 9), width=17, height=2, command=JobDeleteDB, bg="#DAE3F3").place(x=160, y=370)

        CancleButton = Button(win, text="닫기", font=(
            "맑은고딕", 9), width=17, height=2, command=win.destroy, bg="#DAE3F3").place(x=330, y=370)

        win.mainloop()
