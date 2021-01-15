import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string


login = input("login: ")
passwd = input("password: ")
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
cart = "https://www.banggood.com/shopping_cart.html"

driver.get("https://www.banggood.com/login.html")
driver.find_element_by_name("login-email").click()
driver.find_element_by_name("login-email").send_keys(Keys.CONTROL + "a")
driver.find_element_by_name("login-email").send_keys(Keys.DELETE)
driver.find_element_by_name("login-email").send_keys(login)
driver.find_element_by_name("login-pwd").click()
driver.find_element_by_name("login-pwd").send_keys(Keys.CONTROL + "a")
driver.find_element_by_name("login-pwd").send_keys(Keys.DELETE)
driver.find_element_by_name("login-pwd").send_keys(passwd)
driver.find_element_by_xpath("//input[@id='login-submit']").click()
time.sleep(4)
print("Login Done")
driver.get(cart)
time.sleep(4)
driver.find_element_by_class_name("proceed-checkout ").click()
time.sleep(3)

#generate and check coupons
n_total = driver.find_element_by_id("chkout_panel_grandtotal")
total = driver.find_element_by_id("chkout_panel_grandtotal")
print(total)

while total == n_total:
    n_total = driver.find_element_by_id("chkout_panel_grandtotal")
    letters_and_digits = string.ascii_uppercase + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(6)))
    print("Using coupon:", result_str)

    driver.find_element_by_xpath("//input[@class='input-text']").send_keys(result_str)
    driver.find_element_by_xpath("//span[@class='input-btn']").click()
    time.sleep(2)
    n_total = driver.find_element_by_id("chkout_panel_grandtotal")
    if total != n_total:
        file = open("coupons.txt", "w")
        file.write(result_str + "\n")
        break

print("New price: ", n_total)