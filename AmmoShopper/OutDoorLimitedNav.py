from config import *
from selenium.webdriver.common import keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
def ScrapeOutdoorLimited():
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    options.add_experimental_option("excludeSwitches",["test-type"])
    driver = webdriver.Chrome(chrome_options=options, executable_path=f'{WebInterface.path}')
    count = 0
    for links in Sites.OutdoorLimitedLinks:
        if(PurchaseParameters.CurrentSpent > PurchaseParameters.Allowance):
            break
        driver.get(links)
        time.sleep(2)
        OutOfStock = driver.find_elements_by_class_name('is-out-of-stock')
        if(OutOfStock != []): #Item out of stock
            print('This is out of stock: ', links, '\n')

        else: #Item is in stock
            print('This is available', links, '\n')
            available = driver.find_element_by_class_name('form-field--stock')
            available = available.find_element_by_tag_name('span').text #amount in stock
            if(int(available) < int(Sites.OutdoorLimitedQuantity[count])): #if stock lower than quantity requested
                quantity = str(available) #order the full stock
                print('Quantity wanted was more than Available... Adjusted the quantity to amount available \n')
            else:
                quantity = str(Sites.OutdoorLimitedQuantity[count])#quantity wanted is available
            pricePerItem = driver.find_element_by_xpath("//meta[@itemprop='price']").get_attribute("content")
            if((PurchaseParameters.CurrentSpent + (float(quantity)*float(pricePerItem))) <= PurchaseParameters.Allowance): #Make sure you can spend this     
                if(float(pricePerItem) <= float(Sites.OutdoorLimitedMaxPricePerItem[count])):   #Make sure price per item is in range
                    quantityBox = driver.find_element_by_class_name('form-input--incrementTotal')
                    quantityBox.clear() #clear the quantity field
                    quantityBox.send_keys(quantity) #enter quantity wanted onto webpage
                    driver.find_element_by_id('form-action-addToCart').click() #add to cart
                else:
                    print('Price Per Item too high: ', links, '\n')
            else:
                print('Would go over allowance: ', links, '\n')
            time.sleep(2) #let cart load
        count += 1
    driver.find_element_by_class_name('cart-quantity').click()
    time.sleep(3)
    driver.find_element_by_class_name('btn-checkout').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@href="/checkout"]').click()
    time.sleep(5)
    driver.find_element_by_id('email').send_keys(PurchaseInfo.EmailAddress)
    driver.find_element_by_id('checkout-customer-continue').click()
    time.sleep(2)
    driver.find_element_by_id('firstNameInput').send_keys(PurchaseInfo.FirstName)
    driver.find_element_by_id('lastNameInput').send_keys(PurchaseInfo.LastName)
    driver.find_element_by_id('addressLine1Input').send_keys(PurchaseInfo.Address)
    if(PurchaseInfo.Address2):
        driver.find_element_by_id('addressLine2Input').send_keys(PurchaseInfo.Address2)
    driver.find_element_by_id('cityInput').send_keys(PurchaseInfo.City)
    select = driver.find_element_by_id('provinceCodeInput')
    for option in select.find_elements_by_tag_name('option'):
        if (option.text == PurchaseInfo.State):
            option.click()
            break
    driver.find_element_by_id('postCodeInput').send_keys(PurchaseInfo.ZipCode)
    driver.find_element_by_id('phoneInput').send_keys(PurchaseInfo.Phone)
    time.sleep(20)
    x = driver.find_elements_by_class_name('shippingOption')
    x[0].click()
    time.sleep(5)
    driver.find_element_by_id('checkout-shipping-continue').click()
    time.sleep(5)