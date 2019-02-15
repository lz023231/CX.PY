__author__ = "wang ting ting"
import time

#设置按钮定位
def setup_element_click(obj):
    obj.driver.find_element_by_xpath("//a[@title='设置']").click()


## title方法可以获取当前页面的标题显示的字段
def get_title(obj):
    print(obj.driver.title)
    return obj.driver.title




def to_switch_ifrome(self, obj, locaement):
    obj.driver.switch_to.frame(obj.driver.find_element_by_css_selector(locaement))
def back_to_switch_ifrome(self, obj):
    obj.driver.switch_to.default_content()















