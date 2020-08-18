from Config.ProVar import *
from Utils.ConfigParser import *


def getDesiredcaps():
    cfp=ConfigFileParser(DesiredcapsPath)
    items=cfp.getItemsOfSection("desired_caps")
    desired_caps = {
        "platformName": items["platformname"],
        "platformVersion": items["platformversion"],
        "deviceName":items["devicename"],
        "appPackage": items["apppackage"],
        "appActivity": items["appactivity"],
        "noReset": items["noreset"],
        "resetKeyboard": items["resetkeyboard"],
        "unicodeKeyboard": items["unicodekeyboard"],
        "autoAcceptAlerts": items["autoacceptalerts"],
        "automationName": items["automationname"],
        "newCommandTimeout": int(items["newcommandtimeout"])
    }
    return desired_caps








if __name__=="__main__":
    print(getDesiredcaps())