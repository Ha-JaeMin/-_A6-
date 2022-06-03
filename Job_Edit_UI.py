from tkinter import *
from Job_Management_UI import *
import csv


class JobEditUI(JobManagementUI):

    def JobEdit():
        JobManagementUI("직업 수정 화면", "기존 직업 수정", "직업 수정")

    if __name__ == "__main__":
        JobEdit()
