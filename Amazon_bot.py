# Whole lotta bot shit
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
from datetime import datetime
import logging
import requests
import time

logging.basicConfig(filename='amazon.log', level=logging.DEBUG)
config_key = {'alert_delay':1, 'email':'email', 'password':'password'}
#asins = ['B08FC5L3RG','B08H75RTZ8','B08HR3Y5GQ','B0815XFSGK','B08164VTWH','B0815Y8J9N','B08HH5WF97','B08HR7SV3M']
asins = ['B08H75RTZ8']

def checkout(config,url):
    driver = webdriver.Firefox()
    driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
    element = driver.find_element_by_id("ap_email")
    element.send_keys(config['email'])
    element1 = driver.find_element_by_xpath('//*[@id="continue"]')
    element1.click()
    try:
        element2 = driver.find_element_by_xpath('//*[@id="ap_password"]')
        element2.send_keys(config['password'])
        ele = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
        ele.click()
        ele1 = driver.find_element_by_xpath('//*[@id="ap_password"]')
        ele1.send_keys(config['password'])
        time.sleep(3)
        ele12 = driver.find_element_by_xpath('//*[@id="auth-captcha-guess"]')
        ele12.send_keys('392532')
        ele123 = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
        ele123.click()
        ele1234 = driver.find_element_by_xpath('//*[@id="ap_password"]')
        ele1234.send_keys(config['password'])
        time.sleep(3)
        ele2 = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
        ele2.click()
        driver.get(url)
    except:
        driver.get(url)
    try:
        driver.find_element_by_xpath('//*[@id="buy-now-button"]').click()
        time.sleep(1)
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="turbo-checkout-pyo-button"]')
    except:
        driver.find_element_by_css_selector('.place-your-order-button').click()







def stock_check(asin_lst):
    in_stock = False
    while in_stock==False:
        try:
            for i in asin_lst:
                url = 'https://www.amazon.com/gp/product/' + i + '?pf_rd_r=K99S53W1MZB15J8ZJZZN&pf_rd_p=9d9090dd-8b99-4ac3-b4a9-90a1db2ef53b&pd_rd_r=661fa9ce-e845-4aa8-a1ae-58163a083eb2&pd_rd_w=fPlYy&pd_rd_wg=HJEwt&ref_=pd_gw_unk'
                headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "Accept-Encoding":"gzip, deflate, br",
                    "Accept-Language":"en-US,en;q=0.5",
                    "Cache-Control":"max-age=0",
                    "Connection":"keep-alive",
                    "Host":"www.amazon.com",
                    "Referer":"https://www.amazon.com/ref=nav_logo",
                    "TE":"Trailers",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"}
                doc = requests.get(url, headers=headers)
                soup = BeautifulSoup(doc.content, 'html.parser')
                now = datetime.now()
                if "Add to Cart" in soup.prettify() and "Currently unavailable" not in soup.prettify():
                    print(i + " In stock")
                    in_stock = True
                    break
                elif "Correios.DoNotSend" in soup.prettify():
                    pass
                else:
                    print(now.strftime("%H:%M:%S") + " " + i + " Not in stock")
        except: pass
    return url





if __name__ == '__main__':
    product = stock_check(asins)
    checkout(config_key,product)












#w = requests.get('https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08MVC76SR&Quantity.1=1')
#soup = BeautifulSoup(w, 'html.parser')
#print(soup.prettify())


