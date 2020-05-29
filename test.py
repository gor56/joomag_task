import asyncio
import sys
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

def get_url():
    correct = "(https?:\/\/)?(www\.)?[a-z0-9-]+\.(com|org)(\.[a-z]{2,3})?"

    for index in sys.argv:
        if re.search(correct, index):
            print(index)
            return index

async def form_num(a):
    list = a.find_elements_by_xpath('//form[contains(@method, "GET")]')
    if len(list) == 0:
        return 'there were no forms on this website'
    return len(list)

async def img_num(b):
    list = b.find_elements_by_tag_name('img')    
    if len(list) == 0:
        return 'there were no images on this website'
    return len(list)  

async def main():

    options = Options()
    options.add_argument("--disable-infobars")
    options.add_experimental_option("prefs", 
        {"profile.default_content_setting_values.notifications": 1})

    url = get_url()

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.implicitly_wait(15)
    
    
    try:
        num = await form_num(driver)
        img = await img_num(driver)
        print(num)
        print(img)
    finally:
        driver.close()           

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
