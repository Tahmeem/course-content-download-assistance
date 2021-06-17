from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import time
from selenium.webdriver.common.action_chains import ActionChains
course = input("Enter course code: ")
seeWindow = input("Do you want to see the window?(yes/no) ")

PATH = r"C:\Users\tahme\PycharmProjects\LoginAssistance\chromedriver.exe"
driver = webdriver.Chrome(PATH)
if seeWindow == "yes":
    driver.maximize_window()
else:
    driver.minimize_window()

driver.get("https://skule.ca/")

coursesWebsite = ""
aTags = driver.find_elements_by_tag_name("a")
for aTag in aTags:
    hrefVal = aTag.get_attribute('href')
    if hrefVal == "http://courses.skule.ca/":
        coursesWebsite = "http://courses.skule.ca/"

driver.get(coursesWebsite)

searchField = driver.find_element_by_class_name("form-control")
searchField.send_keys(course)
searchField.send_keys(Keys.RETURN)
try:
    MainLink = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, f'{course}'))
        )
    MainLink.click()
    try:
        linkClasses = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.result.col-12'))
        )
        for linkClass in linkClasses:
            # print(linkClass)
            try:
                url = linkClass.find_element_by_tag_name("a").get_attribute("href")
                pageName = linkClass.find_element_by_tag_name("a").get_attribute("text")
                urllib.request.urlretrieve(url, rf"C:\Users\tahme\Downloads\{pageName}.pdf")
            except:
                continue
    except:
        print("This course might have multiple course pages or a page with no resources. Please check again in course site and enter exact course code with name")
except:
    print("Course does not have resources in skule website")

driver.quit()