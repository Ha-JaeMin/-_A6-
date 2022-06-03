from tkinter import *
from Job_Management_UI import *
import csv


class JobDeleteUI(JobManagementUI):

    def JobDelete():
        JobManagementUI("직업 삭제 화면", "기존 직업 삭제", "직업 삭제")

    if __name__ == "__main__":
        JobDelete()
