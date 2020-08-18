from Config.ProVar import *
from configparser import ConfigParser
import os

class ConfigFileParser():

    def __init__(self,configFilePath):
        self.cp=ConfigParser()
        if not (os.path.exists(configFilePath) and os.path.basename(configFilePath).endswith(".ini")):
            print("输入的配置文件路径不存在或者文件类型不是.ini")
            return
        self.cp.read(DesiredcapsPath)

    def getSections(self):
        sections=self.cp.sections()
        return sections

    def getOptionsOfSection(self,sectionName):
        options=self.cp.options(sectionName)
        return options

    def getOption(self,sectionName,optionName):
        try:
            value=self.cp.get(sectionName,optionName)
        except Exception as e:
            print("输入的sectionName或者optionName有误：%s"%e)
            return
        return value

    def getItemsOfSection(self,sectionName):
        items=dict(self.cp.items(sectionName))
        return items




if __name__=="__main__":
    cfp=ConfigFileParser("d:\\pydelete\\a.txt")
    cfp = ConfigFileParser("d:\\pydelete\\0720\\Desiredcaps.ini")
    print(cfp.getSections())
    print(cfp.getOptionsOfSection("desired_caps"))
    print(cfp.getOption("desired_caps","platformname"))
    print(cfp.getItemsOfSection("desired_caps"))

