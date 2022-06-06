from SpecSearchUI_right import*
import tkinter.messagebox as msg


#컨트롤 클래스
class SpecSearchSystem() :
    def __init__(self):
        #직업DB 객체 생성
        self.jobDB = JobDB()
        self.df_Job = self.jobDB.get_df()

    def SearchClick(self,word,treeView): #(검색단어, 표)
        # 테이블 초기화
        for item in treeView.get_children():
            treeView.delete(item)

        # 검색어(자격증)가 포함된 df
        df_contains = self.df_Job[self.df_Job['jobCertifi'].str.contains(word)]
        if df_contains.empty:
            msg.showinfo('입력오류','존재하지 않는 자격증입니다.')
        else :
            # 추출한 df에서 직업이름을 Table에 추가
            for select_name in df_contains['jobName']:
                name= df_contains['jobName'].loc[select_name]
                treeView.insert('','end',text='',value=name,iid=name)
