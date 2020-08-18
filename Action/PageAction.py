from appium import webdriver
from Utils.ObjectMap import *
from Utils.DateAndTime import *
from Config.ProVar import *
from Utils.GetDesiredcaps import *
import traceback



driver=""

def launchApp():
    global driver
    try:
        desired_caps=getDesiredcaps()
        driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    except Exception as e:
        print(traceback.format_exc())
        raise e

def click(locationMethod,locationExp):
    try:
        findElement(driver,locationMethod,locationExp).click()
    except Exception as e:
        print(traceback.format_exc())
        raise e

def clear(locationMethod,locationExp,content):
    try:
        findElement(driver,locationMethod,locationExp).clear()
    except Exception as e:
        print(traceback.format_exc())
        raise e

def inputContent(locationMethod,locationExp,content):
    try:
        findElement(driver,locationMethod,locationExp).send_keys(content)
    except Exception as e:
        print(traceback.format_exc())
        raise e

def assertKeyword(keyword):
    assert keyword in driver.page_source


def takeScreenshots():
    filename = str(TimeUtil().get_chinesedatetime()) + ".png"
    driver.get_screenshot_as_file(os.path.join(LogPath, filename))
    print("截图")
    return os.path.join(LogPath, filename)

def sleep(seconds):
    time.sleep(int(seconds))

def quitServer():
    driver.quit()








if __name__=="__main__":
    launchApp()
    click('id','com.xsteach.appedu:id/content_rb_mine')