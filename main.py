from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Declaring Infos

MailAdress = input("Enter your Falix Email")
Password = input("Enter your FalixPanel Password. Its Private. I dont get it!")
FalixNodesServerURL = input("Enter the URL to your FalixNodes Server-Panel.")
JavaVersion = input("Enter your Java Version. Java Version can be: java8, java11 or default")
CheckServerIntervall = (30)


# Initializing Webdriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.get(FalixNodesServerURL)

time.sleep(2)

# Logging In

CookiesButton = driver.find_element_by_xpath(
    "/html/body/cloudflare-app/cf-dialog/cf-dialog-content/cf-dialog-content-text/form/input")
CookiesButton.click()

MailField = driver.find_element_by_name("username")
PassField = driver.find_element_by_name("password")
LoginButton = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/form/div/div[2]/div[3]/button")


MailField.send_keys(MailAdress)
PassField.send_keys(Password)
LoginButton.click()

print ("Solve Chaptcha")
input("Press Enter to after you solved the Chaptcha...")

time.sleep(1)
print("Script is starting")

wait = WebDriverWait(driver, 10)




while 3 < 4:
    driver.get(FalixNodesServerURL)
    time.sleep(10)
    
    StartButton = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/section/div[1]/div[1]/div[2]/button[1]")
    ConsoleTextField = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/section/div[1]/div[2]/div[2]/div[3]/div[2]/input")
    StatusText = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'sc-')]"))).text

    if StatusText == " RUNNING":

        print("Server is running")

        time.sleep(CheckServerIntervall)

    if StatusText == " OFFLINE":
        print("Server isn´t running it is getting restarted now")
        time.sleep(1)
        StartButton.click()
        time.sleep(11)
        ConsoleTextField.send_keys(JavaVersion)
        ConsoleTextField.send_keys(Keys.ENTER)

    if StatusText == " STOPPING":
        print("Server is stopping. It is getting restarted after it shutdown properly")
        time.sleep(5)


    if StatusText == " CONNECTING...":
        print("The Wings from FalixNodes are down. Your Server is still running, but we cant restart it at the moment.")
        time.sleep(60)



    if StatusText == " STARTING":
        print("Server is starting")
        time.sleep(30)
