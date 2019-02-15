__author__ = "wang ting ting"
from  Element.WebDriverWait import is_visible
from selenium import webdriver
import time

#web客户端点击“咨询客服”
def client_bution_click(obj):
    time.sleep(3)
    obj.driver.find_element_by_css_selector(".chat-icon.chat_icon_3").click()

#点击转人工服务(需求切换iframe)
def client_ren_gong_click(obj):
    time.sleep(2)
    #切换iframe
    obj.driver.switch_to.frame(obj.driver.find_element_by_css_selector("iframe#bw8-chatIframe"))
    time.sleep(3)
    obj.driver.find_element_by_css_selector("a#bw8_whole_footer_artificial").click()
    time.sleep(3)

#点击选择第一个客服组
def client_ke_fu_zu_click(obj):
    is_visible("ul.bw8_skill_middle_ul li a")
    obj.driver.find_element_by_css_selector("ul.bw8_skill_middle_ul li a")

#在输入框内点击
def client_input_click(obj):
    #is_visible(".w8_footer_text_import")
    obj.driver.find_element_by_css_selector(".bw8_footer_text_import").click()

#在输入框内输入内容
def client_input_content(obj, inpurtContent):
    #obj.driver.find_element_by_css_selector(".w8_footer_text_import").click()
    obj.driver.find_element_by_css_selector(".bw8_footer_text_import").send_keys(inpurtContent)

#点击发送按钮
def client_send(obj):
    time.sleep(2)
    obj.driver.find_element_by_css_selector("input.bw8_btn_send_btn_input.bw8_btn_enabled.skin_chat_win").click()
    time.sleep(3)





