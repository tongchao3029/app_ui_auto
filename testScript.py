from Utils.ExcelParser import *
from Config.ProVar import *
from Action.PageAction import *
from Utils.GetDesiredcaps import *
from Utils.DateAndTime import *
import traceback

def main():
    ep=ExcelParser(TestDataPath)
    ep.getSheetByName("测试用例")
    rows=ep.getSheetAllCellValuesByRow()
    print(rows)
    for rowNum,row in enumerate(rows[1:],2):
        if row[ifExecute]=="n":
            print("第%s条用例【%s】不执行"%(rowNum-1,row[caseName]))
        else:
            framework_type = row[frameworkType]
            print("-"*20+"调用%s框架"%framework_type+"-"*20)
            case_step_sheet = row[caseStepSheet]
            ep.getSheetByName(case_step_sheet)
            cases=ep.getSheetAllCellValuesByRow()
            for caseid,case in enumerate(cases[1:],2):
                framework_keyword=case[caseKeyword]
                location_method=case[caseLocationMethod]
                location_exp=case[caseLocationExp]
                operation_value=case[caseOperationValue]
                if framework_keyword and location_method and location_exp and operation_value:
                    step=framework_keyword+"('%s','%s','%s')"%(location_method,location_exp,operation_value)
                    print(step)
                elif framework_keyword and location_method and location_exp:
                    if location_method=="MobileBy.ANDROID_UIAUTOMATOR":
                        step = framework_keyword + "(%s,'%s')" % (location_method, location_exp)
                        print(step)
                    else:
                        step = framework_keyword + "('%s','%s')" % (location_method, location_exp)
                        print(step)
                elif framework_keyword and operation_value:
                    if framework_keyword=="sleep":
                        step = framework_keyword + "(%s)"%(str(operation_value))
                        print(step)
                    else:
                        step=framework_keyword + "('%s')" % (operation_value)
                        print(step)
                elif framework_keyword:
                    step = framework_keyword +"()"
                    print(step)
                try:
                    ep.writeCellValue(caseid, caseExecuteTime + 1, TimeUtil().get_datetime())
                    eval(step)
                    ep.writeCellValue(caseid,caseResult+1,"Pass","green")
                except Exception as e:
                    print(e)
                    ep.writeCellValue(caseid, caseResult + 1, "Fail", "red")
                    ep.writeCellValue(caseid,caseErrorInfo+1,traceback.format_exc())
                    image=takeScreenshots()
                    newsize=(242,130)
                    ep.insertImage(image,newsize,"I"+str(caseid))

            if "Fail" in ep.getColValues(caseResult+1):
                print(ep.getColValues(caseResult+1))
                ep.getSheetByName("测试用例")
                ep.writeCellValue(rowNum,executeTime+1,TimeUtil().get_datetime())
                ep.writeCellValue(rowNum,result+1,"Fail","red")
            else:
                print(ep.getColValues(caseResult + 1))
                ep.getSheetByName("测试用例")
                ep.writeCellValue(rowNum, executeTime + 1, TimeUtil().get_datetime())
                ep.writeCellValue(rowNum, result + 1, "Pass", "green")
    ep.saveExcel()








if __name__=="__main__":
    main()