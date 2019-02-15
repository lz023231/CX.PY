#coding=utf-8
from selenium import webdriver
from time import sleep
#引入keys模块
from selenium.webdriver.common.keys import Keys




def chat_bangwo8():
    
    #在函数里面定义全局变量，也可以在外面定义，在函数内定义需要 global 关键字
    global driver
    driver = webdriver.Chrome()
    driver.get("file://C:/Python35/Lib/idlelib/example/chattest.html")

    #windows 最大化
    #driver.

    driver.find_element_by_xpath("//*[@id='ChatWindowDiv']/div[1]/p").click()
    sleep(2)

    #frame里有iframe
    xf = driver.find_element_by_id("ChatIframe")
    driver.switch_to.frame(xf)
    #sleep(2)

    driver.find_element_by_xpath(".//*[@id='saytext']").send_keys("selenium")
    #sleep(2)

    #用键盘代替鼠标的点击操作
    driver.find_element_by_xpath(".//*[@id='saytext']").send_keys(Keys.ENTER)
    #以下是用鼠标点击
    #driver.find_element_by_xpath("html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/input").click()
    #sleep(2)

    #driver.switch_to.parent_frame()

    #driver.quit()


def call_chat_bangwo8():
        
    count = 0
    chat_bangwo8()
    while (count < 999):

        #切换浏览器窗口
        sreach_windows = driver.current_window_handle
        all_handles = driver.window_handles

        for handle in all_handles:
            if handle != sreach_windows:
                driver.switch_to.window(handle)
                print("now register window!")
        
        print ('The count is:', count)
        count = count + 1
        chat_bangwo8()

        
        print ("Good bye!")
call_chat_bangwo8()
            









