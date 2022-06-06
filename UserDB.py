import pandas as pd

class UserDB():
    def __init__(self):
        self.index_key = None
        df_User = pd.read_csv("csv/User.csv",encoding='CP949')
        self.df_User = df_User.set_index('UserName',drop=False)
    def set_index_key(self,index_key):
        self.index_key = index_key
    def get_df(self):
        return self.df_User
    def get_row(self):
        self.row = self.df_User.loc[[self.index_key],:]
        return self.row
    def get_name(self):
        name = self.df_User['UserName'].loc[self.index_key]
        return name
    def get_id(self):
        id = self.df_User['UserId'].loc[self.index_key]
        return id
    def get_PW(self):
        PW = self.df_User['jobEquality'].loc[self.index_key]
        return PW
    def get_Phone(self):
        Phone = self.df_User['UserPhone'].loc[self.index_key]
        return Phone
    def get_Certifi(self):
        Certifi = self.df_User['UserCertifi'].loc[self.index_key]
        return Certifi
    def get_Toeic(self):
        Toeic = self.df_User['UserToeic'].loc[self.index_key]
        return Toeic
    def get_Department(self):
        Department = self.df_User['UserDepartment'].loc[self.index_key]
        return Department

