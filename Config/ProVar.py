import os



ProjectPath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DesiredcapsPath=os.path.join(ProjectPath,"Config","Desiredcaps.ini")
LogPath=os.path.join(ProjectPath,"Log")
TestDataPath=os.path.join(ProjectPath,"TestData","邢帅教育.xlsx")


###测试用例sheet
caseName=0
caseDescription=1
frameworkType=2
caseStepSheet=3
datadrivenData=4
ifExecute=5
executeTime=6
result=7

###测试用例步骤sheet
caseStepDescription=0
caseKeyword=1
caseLocationMethod=2
caseLocationExp=3
caseOperationValue=4
caseExecuteTime=5
caseResult=6
caseErrorInfo=7
caseWrongPic=8












if __name__=="__main__":
    print(ProjectPath)
    print(DesiredcapsPath)
    print(LogPath)
    print(TestDataPath)