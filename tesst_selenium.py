#!/usr/bin/env python
# coding: utf-8

# In[1]:


import winsound

import requests, csv, random, time, json, re, ast, logging, os, platform
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from datetime import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.proxy import *


# In[2]:


def find_proxy():
    soup_test = True
    while soup_test == True:
        res = requests.get('https://free-proxy-list.net/', headers={'User-Agent':'Mozilla/5.0'})
        soup = BeautifulSoup(res.text,"lxml")
        if len(soup) > 0:
            soup_test = False
        else:
            print('Trying get next proxy')
            
        proxy_list_set = set()
    for i, items in enumerate(soup.select("#proxylisttable tbody tr")):
        if 'elite proxy' in items.select("td")[4]:
            proxy_list = ':'.join([item.text for item in items.select("td")[:2]])
            proxy_list_set.add(proxy_list)
    return list(proxy_list_set)


# In[3]:


resolutions = [(120,90),
     (352,240),
     (352,288),
     (480,272),
     (352,480),
     (352,576),
     (480,480),
     (480,576),
     (352,480),
     (704,480),
     (720,480),
     (352,576),
     (704,576),
     (720,576),
     (352,480),
     (480,480),
     (528,480),
     (544,480),
     (640,480),
     (704,480),
     (720,480),
     (480,576),
     (544,576),
     (704,576),
     (720,576),
     (640,720),
     (960,720),
     (1280,720),
     (960,1080),
     (1280,1080),
     (1440,1080),
     (1920,1080),
     (960,540),
     (1600,900),
     (2560,1440),
     (3200,1800),
     (2880,2160),
     (3840,2160),
     (7680,4320),
     (15360,8640)]


# In[4]:


def get_html(link):
    i = 1
    html = None
    result = False
    PROXY = find_proxy()
    SCROLL_PAUSE_TIME = 1
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 100  # Set Duration To 1000 ms == 1 second
#    winsound.Beep(frequency, duration)
    while not result:
        resolution = resolutions[random.randint(0,len(resolutions) - 1)]
        res_len = resolution[0]
        res_high = resolution[1]
        argument = str("--window-size=" + str(res_len)+ "," + str(res_high))
        print('link is ',link,'Proxy server used:', PROXY[i],'\n', argument)
        ua = UserAgent()
        user_agent = str(ua.random)
        op = webdriver.ChromeOptions()
#        op.add_argument('headless')
        op.add_argument(argument)
        op.add_argument('user-agent=%s' % user_agent)
        op.add_argument("--no-sandbox")
        op.add_argument('--proxy-server=%s' % PROXY[i])
        if platform.system() == 'Linux':
            driver = webdriver.Chrome( options=op)
            print('OS linux recognized')
        elif platform.system() == 'Windows':
            print('OS windows recognized')
            PATH = 'D:\Software\chromedriver.exe'
            driver = webdriver.Chrome(PATH, options=op)
            print('loaded chromedriver. Attempt number', i)
        try:
            print('Processing link')
            driver.get(link)
            #print(driver.get(link))
            print('Have got link. Attempt number', i)
            '''
            try:
                element = WebDriverWait(driver, 2).until(
                    EC.visibility_of_element_located((By.CLASS_NAME,'survey__section'))#((By.CLASS_NAME, "breakpoint"))
                )
                print('element found', element)
                #winsound.Beep(frequency, duration)
                time.sleep(1)
            except Exception as err:
                print('element not found in visibility search section')
                print(err.args)
                print('link is ',link,'changing proxy, attempt number', i)
                driver.quit()
                i += 1
                continue
            '''
            check = driver.page_source
            print("*"*50)
            title = driver.title
            print('title:',title)
#            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print('link is',link,' was scrolled, waited, then exiting')          
            time.sleep(1)
 #           driver.find_element(By.XPATH,"/html/body/div[1]/form/div[1]/div[2]/fieldset[1]/div[1]/div/table/tbody/tr/td[3]/span[1]/button/span").click()
            winsound.Beep(frequency, duration)
            print("!"*75)
            time.sleep(10)
            driver.find_element(By.XPATH,'//*[@id=\"uniq160753749428813\"]').click()
            winsound.Beep(frequency, duration)
            print("!"*75)
            time.sleep(10)
            winsound.Beep(frequency, duration)
            driver.find_element(By.XPATH,'//*[@id="uniq16075353876097438371"]').click()
            driver.find_element(By.XPATH,"/html/body/div/form/div[1]/div[2]/fieldset[1]/div[3]/div/table/tbody/tr[2]/td[2]/span/label[3]/span[1]").click()

            driver.find_element(By.XPATH,"/html/body/div/form/div[1]/div[2]/fieldset[1]/div[4]/div/table/tbody/tr[2]/td[2]/span/label[1]/span[1]").click()
            driver.find_element(By.XPATH,"/html/body/div/form/div[1]/div[2]/fieldset[1]/div[5]/div/table/tbody/tr[2]/td[2]/span/label[1]/span[1]").click()
            driver.find_element(By.XPATH,"/html/body/div[1]/form/div[1]/div[2]/fieldset[1]/div[8]/div/table/tbody/tr[2]/td[2]/div[1]/span/span").click()
            driver.find_element(By.XPATH,"/html/body/div[1]/form/div[1]/div[2]/fieldset[1]/div[8]/div/table/tbody/tr[2]/td[2]/div[2]/span/span").click()
            driver.find_element(By.XPATH,"//*[@id=\"uniq160734051745018151985\"]").click()

            driver.find_element_by_xpath("").click()
            driver.find_element_by_xpath("").click()
            driver.find_element_by_xpath("").click()
            driver.find_element_by_xpath("").click()
            driver.find_element_by_xpath("").click()
            driver.find_element_by_xpath("").click()
            driver.find_element_by_xpath("").click()

            # frequency = 2500  # Set Frequency To 2500 Hertz
            # duration = 1000  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
            time.sleep(6)
            result = True
            driver.delete_all_cookies()
            driver.quit()
            text = "Have done all job with " + str(link)
            return text
            # break# print(html)
            # save_file(html)
        except Exception as err:
            print('Link processing failed because of ', err.args)
            i += 1
            driver.delete_all_cookies()
            driver.quit()
            print(err.args)
            if i > 10:
            	result = True
            	break
            continue
#         finally:
#             print('finally 2')
#             driver.delete_all_cookies()
#             driver.quit()
#             i += 1


# In[ ]:


links = [
		'https://zhilishnik-tn.mos.ru/presscenter/news/detail/9493830.html',
		]
if __name__ == "__main__":
        while True:      
            for link in links:
                try:
                    print('trying to process link', link)
                    print(get_html(link))
                except Exception as err:
                    print(err.args)
                    pass


# In[ ]:


driver.quit()


# In[ ]:





