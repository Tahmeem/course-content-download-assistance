from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import time
course = input("Enter course code: ")

PATH = r"C:\Users\tahme\PycharmProjects\LoginAssistance\chromedriver.exe"
driver = webdriver.Chrome(PATH)

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
    linkClasses = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.result.col-12'))
    )
    for linkClass in linkClasses:
        try:
            url = linkClass.find_element_by_tag_name("a").get_attribute("href")
            pageName = linkClass.find_element_by_tag_name("a").get_attribute("text")
            linkClass.find_element_by_tag_name("a").click()
            urllib.request.urlretrieve(url, rf"C:\Users\tahme\Downloads\{pageName}.pdf")
            print("File downloaded")
        except:
            continue
except:
    print("Course does not have resources in skule website")

time.sleep(3)
driver.quit()
