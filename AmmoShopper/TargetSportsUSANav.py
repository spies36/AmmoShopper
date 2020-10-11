from config import *
from selenium.webdriver.common import keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time

def ScrapeTargetSportsUSA():
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    options.add_experimental_option("excludeSwitches",["test-type"])
    driver = webdriver.Chrome(chrome_options=options, executable_path=f'{WebInterface.path}')
    driver.fullscreen_window()
    count = 0
    for links in Sites.TargetSportsUSALinks:
        if(PurchaseParameters.CurrentSpent > PurchaseParameters.Allowance):
            break
        driver.get(links)
        time.sleep(4)       
        stock = driver.find_element_by_class_name('stock-info')
        if(stock.text == 'OUT OF STOCK'): #Item out of stock
            print('This is out of stock', links, '\n')
        else: #Item is in stock
            print('This is available', links, '\n')
            pricePerItem = driver.find_element_by_xpath("//div[@itemprop='price']").text
            separator = '/'
            pricePerItem = pricePerItem.split(separator,1)[0]
            pricePerItem = pricePerItem.replace('$','')
            if((PurchaseParameters.CurrentSpent + (float(Sites.TargetSportsUSAQuantity[count])*float(pricePerItem))) <= PurchaseParameters.Allowance): #Make sure you can spend this     
                if(float(pricePerItem) <= float(Sites.TargetSportsUSAMaxPricePerItem [count])):   #Make sure price per item is in range
                    quantityBox = driver.find_element_by_class_name('quantity-field')
                    quantityBox.clear()
                    quantityBox.send_keys(Sites.TargetSportsUSAQuantity[count])
                    driver.find_element_by_class_name('add-to-cart').click()
                else:
                    print('Price Per Item too high ', links, '\n')
            else:
                print('Would go over allowance: ', links, '\n')
        count += 1
        time.sleep(4)
    time.sleep(10)
    popUp = driver.find_elements_by_class_name('mc-closeModal')
    if(popUp != []):
        popUp[0].click()
        time.sleep(5)
    popUp1 = driver.find_elements_by_xpath("//a[@onclick='Shadowbox.close()']")
    if(popUp1 != []):
        popUp1[0].click()
        time.sleep(5)
    driver.find_element_by_xpath("//a[@href='shoppingcart.aspx']").click()
    time.sleep(10)
    driver.find_element_by_id('ctl00_PageContent_btnCheckOutNowTop').click()
    time.sleep(6)

