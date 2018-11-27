# -- coding: utf-8 --
  # coding: utf-8
  # modify_response.py
  # https://g.alicdn.com/secdev/sufei_data/3.6.8/index.js u盟反扒脚本
  # mitmdump -s modify_response.py -w log

import re

from bs4 import BeautifulSoup
from mitmproxy import ctx


with open('headless.js', 'r') as f:
  injected_javascript = f.read()

with open('114.js', 'r') as g:
  injected_javascript114 = g.read()
def response(flow):
  """修改应答数据
  """
  # print('拦截请求')
  # print( 'sufei_data/3.6.8/index.' in 'https://g.alicdn.com/secdev/sufei_data/3.6.8/index.js')
  # print(flow.request.url)

  if 'sufei_data/3.6.8/index.' in flow.request.url:
    # print('拦载到关键脚 本')
      # 屏蔽selenium检测
    for webdriver_key in ['webdriver', '__driver_evaluate', '__webdriver_evaluate', '__selenium_evaluate', '__fxdriver_evaluate', '__driver_unwrapped', '__webdriver_unwrapped', '__selenium_unwrapped', '__fxdriver_unwrapped', '_Selenium_IDE_Recorder', '_selenium', 'calledSelenium', '_WEBDRIVER_ELEM_CACHE', 'ChromeDriverw', 'driver-evaluate', 'webdriver-evaluate', 'selenium-evaluate', 'webdriverCommand', 'webdriver-evaluate-response', '__webdriverFunc', '__webdriver_script_fn', '__$webdriverAsyncExecutor', '__lastWatirAlert', '__lastWatirConfirm', '__lastWatirPrompt', '$chrome_asyncScriptInfo', '$cdc_asdjflasutopfhvcZLmcfl_']:
      ctx.log.info('Remove "{}" from {}.'.format(webdriver_key, flow.request.url))
      flow.response.text = flow.response.text.replace('"{}"'.format(webdriver_key), '"adlfkjadfo2342adsfasdfznxzxcqiworu234123w"')
    flow.response.text = flow.response.text.replace('f.webdriver', 'false')
    flow.response.text = flow.response.text.replace('chrome', 'adlfkjadfo2342adsfasdfznxzxcqiworu234123w')
    flow.response.text = flow.response.text.replace('ChromeDriver', '')
    # flow.response.text = flow.response.text.replace('case 12:se[ne](be),As=1255;', 'case 12:debugger;se[ne](be),As=1255;')

  # if 'passport.alibaba.com/mini_login.htm?lang=zh_cn' in flow.request.url:
  if 'passport.alibaba.com/mini_login.htm?lang=zh_cn' in flow.request.url:


    html = BeautifulSoup(flow.response.text, 'lxml')
    container = html.head or html.body
    if container:
      script = html.new_tag('script', type='text/javascript')
      script.string = injected_javascript
      container.insert(0, script)
      flow.response.text = str(html)

      ctx.log.info('Successfully injected the `headless.js` script.')

  if 'AWSC/uab/114.js' in flow.request.url:
    print('替换114')
    flow.response.text = injected_javascript114

