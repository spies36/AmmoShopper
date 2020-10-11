from config import *
from selenium.webdriver.common import keys
from selenium import webdriver
import time
def ScrapeLuckyGunner():
    driver = webdriver.Chrome(WebInterface.path)
    count = 0
    for links in Sites.LuckyGunnerLinks:
        if(PurchaseParameters.CurrentSpent > PurchaseParameters.Allowance):
            break
        driver.get(links)
        time.sleep(2)
        OutOfStock = driver.find_elements_by_class_name('out-of-stock')
        if(OutOfStock != []): #Item out of stock
            print('This is out of stock: ', links, '\n')
        
        else: #Item is in stock
            print('This is available: ', links, '\n')
            available = driver.find_element_by_class_name('stock-qty').text #amount in stock
            if(int(available) < int(Sites.LuckyGunnerQuantity[count])): #if stock is lower than quantity wanted
                quantity = str(available) #order the full stock
                print('Quantity wanted was more than Available... Adjusted the quantity to amount available \n')
            else:
                quantity = str(Sites.LuckyGunnerQuantity[count]) #quantity wanted is available
            pricePerItem = driver.find_element_by_class_name('price-box').text
            pricePerItem = pricePerItem.replace('$','')
            if((PurchaseParameters.CurrentSpent + (float(quantity)*float(pricePerItem))) <= PurchaseParameters.Allowance): #Make sure you can spend this              
                if(float(pricePerItem) <= float(Sites.LuckyGunnerMaxPricePerItem[count])):   #Make sure price per item is in range
                    quantityBox = driver.find_element_by_id('qty')
                    quantityBox.clear() #clear the quantity field
                    quantityBox.send_keys(quantity) #enter quantity wanted onto web page
                    driver.find_element_by_class_name('btn-cart').click() # add to cart
                else:
                    print('Price Per Item too high: ', links, '\n')
            else:
                print('Would go over allowance: ', links, '\n')
            time.sleep(2) #let cart load
        count += 1

    driver.find_element_by_class_name('top-link-cart').click()
    time.sleep(2)
    emptyCart = driver.find_elements_by_class_name('cart-table-img')
    if(emptyCart == []):
        print("Cart is empty")
        return
    if(PurchaseParameters.CurrentSpent > PurchaseParameters.Allowance):
            return
    driver.find_element_by_class_name('btn-proceed-checkout').click()
    time.sleep(2)
    driver.find_element_by_id('onepage-guest-register-button').click() #continue as guest
    time.sleep(2) #let next section load
    driver.find_element_by_id('billing:firstname').send_keys(PurchaseInfo.FirstName)
    driver.find_element_by_id('billing:lastname').send_keys(PurchaseInfo.LastName)
    driver.find_element_by_id('billing:street1').send_keys(PurchaseInfo.Address)
    if(PurchaseInfo.Address2 != None):
        driver.find_element_by_id('billing:street2').send_keys(PurchaseInfo.Address2)
    driver.find_element_by_id('billing:postcode').send_keys(PurchaseInfo.ZipCode)
    driver.find_element_by_id('billing:city').send_keys(PurchaseInfo.City)
    select = driver.find_element_by_id('billing:region_id')
    for option in select.find_elements_by_tag_name('option'):
        if (option.text == PurchaseInfo.State):
            option.click()
            break
    driver.find_element_by_name('billing[telephone]').send_keys(PurchaseInfo.Phone)
    driver.find_element_by_id('billing:email').send_keys(PurchaseInfo.EmailAddress)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@title="Continue"]').click() #Entered shipping/billing info
    time.sleep(5)
    driver.find_element_by_xpath('//*[@onclick="shippingMethod.save()"]').click() #continue past shipping
    time.sleep(5)