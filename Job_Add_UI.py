from tkinter import *
from Job_Management_UI import *
import csv


class JobAddUI(JobManagementUI):

    def JobAdd():
        JobManagementUI("직업 등록 화면", "신규 직업 등록", "직업 등록")

    if __name__ == "__main__":
        JobAdd()
