# -*- coding: utf-8 -*-            
# @Author :Yuan
# @FileName: appiumAPI.py
# @Software: PyCharm
import time

from appium import webdriver

_AppPackage = 'com.xueqiu.android'
_AppActivity = '.view.WelcomeActivityAlias'
caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '7.1.2'
# caps['deviceName'] ='127.0.0.1:62001'       # ios-->caps['uuid']='127.0.0.1:62001'
caps['uuid'] = '127.0.0.1:62001'
caps['appPackage'] = _AppPackage
caps['appActivity'] = _AppActivity  # -->不可变的
caps['noReset'] = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(30)
# app是否被安装
print(driver.is_app_installed(_AppPackage))
# 删除app
driver.remove_app(_AppPackage)
time.sleep(5)
# 安装app
driver.install_app("C:\\Users\\apple\\Desktop\\xueqiu.apk")
time.sleep(2)
# 启动app
driver.start_activity(_AppPackage, _AppActivity)
time.sleep(5)
# 返回（置）后台页面（缩小）等待5秒后再次点开
driver.background_app(5)
time.sleep(2)
# 重置应用
driver.reset()
# 键码表
driver.press_keycode(26)
# 滑动拖拽，手势类操作（滑动、长按、拖拽）
from appium.webdriver.common.touch_action import TouchAction

# 实例化   press按压控件,element或坐标点二选一即可，不能填写两个    release结束动作（松手）释放按压指针   perfrom（执行）
TouchAction(driver).press().perform()
# 长按,先执行后释放
TouchAction(driver).long_press().perform().release()
# 点击 需要列表中的元组，注意：语法：[(x,y)]  1、内置tap函数 2、使用TouchAction类
driver.tap([(100, 200)])  # ==>TouchAction(driver).tap(x,y).perform().release()
# 暂停 wait  2000ms=2秒  单位是毫秒
TouchAction(driver).wait(2000)
# 移动   先长按但不释放移动到对应位置再释放    （element）目标位置元素
# 需要两行代码（长按）配合舒勇
TouchAction.move_to().release()
# 移动（一行代码）
TouchAction(driver).long_press().move_to().perform().release()
# 滑动driver.swipe(x1,y1,x2,y2,times)
driver.swipe()
# 隐藏键盘    ()里什么都不用填写
driver.hide_keyboard()
# 摇一摇   ()里什么都不用填
driver.shake()
# 滚动   从a元素到b元素driver.scroll(A_element,B_element)
driver.scroll()
# appium内置函数滚动  driver.flick(x1,y1,x2,y2)
driver.flick()
# 放大、缩小
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

action1 = TouchAction(driver)
action2 = TouchAction(driver)
zoom = MultiAction(driver)
# action1.press(x1,y1).wait(1000).move_to(x1,y1).wait(1000)
# action2.press(x1,y1).wait(1000).move_to(x1,y1).wait(1000)
# zoom.add(action1,action2)
# 获取屏幕分辨率(宽、高)
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
# 移动
driver.swipe(0.8 * x, 0.5 * y, 0.2 * x, 0.1 * y, 2000)
# 模拟网络0：无网络1：飞行模式2：wifi4：蜂窝（流量）6：所有网络都打开（不包含0和1）
driver.set_network_connection(4)
# 通知栏  ()不用填
driver.open_notifications()
# 修改经纬度  longitude:经度  latitude:纬度   altitude:高度
driver.set_location(latitude=18, longitude=21, altitude=None)
# 判断  assert:断言   is_enabled():编辑    is_selected：选中    is_displayed:是否可见

assert driver.find_element().is_enabled() is True
from appium.webdriver.common.mobileby import MobileBy

driver.find_element()
# 切换页面
driver.switch_to.context('webview页面')


