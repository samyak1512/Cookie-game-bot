from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import os
import time

chrome_driver_path = 'C:/Users/2samy/Desktop/Developer/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://linkedin.com/uas/login")

# waiting for the page to load
time.sleep(5)

# entering username
username = driver.find_element_by_id("username")

# In case of an error, try changing the element
# tag used here.

# Enter Your Email Address
username.send_keys("timewast84@gmail.com")

# entering password
pword = driver.find_element_by_id("password")
# In case of an error, try changing the element
# tag used here.

# Enter Your Password
pword.send_keys("shaurya123456")

# Clicking on the log in button
# Format (syntax) of writing XPath -->
# //tagname[@attribute='value']
driver.find_element_by_xpath("//button[@type='submit']").click()

driver.get("https://www.google.com/search?q=bits+pilani+eee+linkedin&rlz=1C1FKPE_enIN960IN960&oq=bits&aqs=chrome.1.69i57j35i39l2j46i67i433j0i67l4j46i175i199i512j0i131i433i512.4640j0j7&sourceid=chrome&ie=UTF-8")

# Get cookie to click on.
LinksForProfile = driver.find_elements_by_class_name("yuRUbf")
one = LinksForProfile[0]
one.click()
time.sleep(3)
education = driver.find_element_by_id('ember140')
print(education.text)

print(LinksForProfile[0])
#Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 10
five_min = time.time() + 60 * 200  # 5minutes
# import_save = driver.find_element_by_id('importSave')
# import_save.click()
# alert = driver.switch_to.alert
# alert.send_keys('0.1251|12545|30|336|18|583|2|605|0|2000|0|7000|0|50000|0|1000000|0|123456789')
# alert.send_keys( Keys.ENTER)
# alert.accept()
#



while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 10

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break
