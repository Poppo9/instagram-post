import time
import random
import os
from dotenv import load_dotenv
from funcs.selenium_utils import setup_driver
from selenium.webdriver.common.by import By

load_dotenv('.env')
IG_USER=os.getenv('IG_USER')
IG_PWD=os.getenv('IG_PWD')

def main():

    driver = setup_driver(headless=False)
    driver.get("https://www.instagram.com/")
    
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.x15fl9t6.x1yw9sn2.x1evh3fb.x4giqqa.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x5yr21d.x19onx9a > div > button._a9--._ap36._a9_1').click()
    time.sleep(random.randint(10,20)/10)
    user_field = driver.find_element(By.CSS_SELECTOR, '#loginForm > div.html-div.x14z9mp.xat24cr.x1lziwak.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x9f619.xjbqb8w.x78zum5.x15mokao.x1ga7v0g.x16uus16.xbiv7yw.xqui205.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div:nth-child(1) > div > label > input')
    time.sleep(random.randint(5,10)/10)
    for key in range(len(IG_USER)):
        user_field.send_keys(IG_USER[key])
        time.sleep(random.randint(10,50)/100)
    time.sleep(2)
    pwd_field = driver.find_element(By.CSS_SELECTOR, '#loginForm > div.html-div.x14z9mp.xat24cr.x1lziwak.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x9f619.xjbqb8w.x78zum5.x15mokao.x1ga7v0g.x16uus16.xbiv7yw.xqui205.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div:nth-child(2) > div > label > input')
    time.sleep(random.randint(5,10)/10)
    for key in range(len(IG_PWD)):
        pwd_field.send_keys(IG_PWD[key])
        time.sleep(random.randint(10,50)/100)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#loginForm > div.html-div.x14z9mp.xat24cr.x1lziwak.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x9f619.xjbqb8w.x78zum5.x15mokao.x1ga7v0g.x16uus16.xbiv7yw.xqui205.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div:nth-child(3)').click()
    time.sleep(random.randint(5,10)/10)



    input("Press ENTER to close the browser...")
    driver.quit()



if __name__=='__main__':
    main()