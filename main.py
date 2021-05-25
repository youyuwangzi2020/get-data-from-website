# This is a webdriver Python script.
# function1：get website data
# function2：save to Excel

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
import time
import string
import openpyxl
import os
import re


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def write_to_text(filename,content):
    with open(filename,'a',encoding='utf-8') as f:
        f.write(content)
        f.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    url="https://jingcai.okooo.com/"
    url_temp2=url                                       #old website
    # Loading Selenium Webdriver
    driver = webdriver.Chrome()                         #open Chrome
    wait = WebDriverWait(driver, 5)                     #等待5s

    # Opening website
    driver.get(url)                                     #打开网址
    time.sleep(3)                                       #等待3s

    page_text=driver.page_source

    results=re.findall('<div class="touzhu_1".*?data-end="0".*?data-mid="(.*?)".*?data-morder.*?</div>.*?paim paim_sel.*?title="(.*?)>.*?paim paim_sel.*?title="(.*?)>',page_text,re.S)

    for result in results:
        print(result)
        write_to_text('1.txt',result[0]+','+result[1]+','+result[2]+','+'\n')




    #while 1:
        #url_temp1=driver.current_url                    #new website

        #if url_temp1 != url_temp2 and url_temp1=="https://jingcai.okooo.com/":
            #print(driver.title)                         #网址变化，进行操作
            #url_temp2 = driver.current_url
            #print(driver.page_source)
            #entries = driver.find_elements_by_class_name('touzhu')
            #for entry in entries:
                #adress = entry.find_element_by_class_name('touzhu_1').text
                #print(adress)