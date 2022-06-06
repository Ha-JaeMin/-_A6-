import pandas as pd

class JobDB():
    def __init__(self):
        self.index_key = None
        df_Job = pd.read_csv("csv/Job.csv",encoding='CP949')
        self.df_Job = df_Job.set_index('jobName',drop=False)
    def set_index_key(self,index_key):
        self.index_key = index_key
    def get_df(self):
        return self.df_Job
    def get_row(self):
        self.row = self.df_Job.loc[[self.index_key],:]
        return self.row
    def get_name(self):
        name = self.df_Job['jobName'].loc[self.index_key]
        return name
    def get_information(self):
        information = self.df_Job['jobInformation'].loc[self.index_key]
        return information
    def get_Certifi(self):
        Certifi = self.df_Job['jobCertifi'].loc[self.index_key]
        return Certifi
    def get_Department(self):
        Department = self.df_Job['jobDepartment'].loc[self.index_key]
        return Department
    def get_Wage(self):
        Wage = self.df_Job['jobWage'].loc[self.index_key]
        return Wage
    def get_Prospect(self):
        Prospect = self.df_Job['jobProspect'].loc[self.index_key]
        return Prospect
    def get_Equality(self):
        Equality = self.df_Job['jobEquality'].loc[self.index_key]
        return Equality
    def get_View(self):
        View = self.df_Job['jobView'].loc[self.index_key]
        return View
    def get_Sex(self):
        Sex = self.df_Job['jobSex'].loc[self.index_key]
        return Sex
    def get_Link(self):
        Link = self.df_Job['jobLink'].loc[self.index_key]
        return Link
    def get_Toeic(self):
        Toeic = self.df_Job['jobToeic'].loc[self.index_key]
        return Toeic
