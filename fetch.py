# -- coding: utf-8 --

import requests
import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from requests.packages import urllib3


ts = str(int(time.time() * 1000))
today = datetime.date.today()
yesterday = (today - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

url = "https://passport.umeng.com/login"
alibabaUrl = "https://passport.alibaba.com/mini_login.htm?lang=zh_cn&appName=youmeng&appEntrance=default&styleType=auto&bizParams=&notLoadSsoView=true&notKeepLogin=false&isMobile=false&cssLink=https://passport.umeng.com/css/loginIframe.css&rnd=0.6379908951190967"
baseUrl = "https://web.umeng.com/"
# 获取昨天的日期

eventDetailUrl = "main.php?c=eanalysis&a=edetail&ajax=module%3DgetList_currentPage%3D1_pageType%3D1000&siteid=1275148014" + "&st=" + yesterday + "&et=" + yesterday + "&visitorType=&location=&ip=&referer=&cnzz_eid=&eventname=&_=" + ts

eventTargetUrl = 'https://web.umeng.com/main.php?c=eanalysis&a=frame&siteid=1275148014#!/1543224092367/eanalysis/edetail/1/1275148014/' + yesterday +'/' + yesterday



ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'

account = ''
pwd = ''

chrome_options = Options()
# 无头模式启动
# chrome_options.add_argument('--headless')
# 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--disable-gpu')
# 禁用 cache
chrome_options.add_argument('--disable-cache')

# 禁用图片
chrome_options.add_argument('blink-settings=imagesEnabled=false')
# chrome_options.add_argument('executable_path=/Applications/chromedriver')
chrome_options.add_argument('user-agent=' + ua)


# 初始化实例
browser = webdriver.Chrome(executable_path='/Applications/chromedriver',chrome_options=chrome_options)

# 清除缓存
browser.delete_all_cookies()

# browser.maximize_window()

# 登陆动作
browser.get(url)
# alibabaw登陆框

browser.switch_to_frame("alibaba-login-box")
# 帐号
accDom = browser.find_element_by_id("fm-login-id")
# 密码
pwdDom = browser.find_element_by_id("fm-login-password")

# 登陆帐号
loginSubmitBtn = browser.find_element_by_id("fm-login-submit")


time.sleep(10)
accDom.send_keys(account)
time.sleep(7)
pwdDom.send_keys(pwd)
time.sleep(5)
pwdDom.send_keys(Keys.ENTER)
# loginSubmitBtn.click()
# 切回主页面

browser.switch_to_default_content()


time.sleep(5)
# 附加cookies
list_cookies = browser.get_cookies()
cookies = {}
for ck in list_cookies:
	cookies[ck['name']] = ck['value']
browser.get(eventTargetUrl)
# cookies = browser.get_cookies()

time.sleep(5)
urllib3.disable_warnings()
res = requests.get(baseUrl + eventDetailUrl, cookies=cookies, verify=False)


# 保存到本地
locate = open('locate/' + yesterday + '.json', 'w')
locate.write(str(res.json()))
locate.close()
# 退出
browser.quit()



