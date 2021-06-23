from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Declaring Infos

MailAdress = input("Enter your Falix Email")
Password = input("Enter your FalixPanel Password. Its Private. I dont get it!")
FalixNodesServerURL = input("Enter the URL to your FalixNodes Server-Panel.")
JavaVersion = input("Enter your Java Version. Java Version can be: java8, java11 or default")
CheckServerIntervall = (60)


# Initializing Webdriver and making Chrome Headless. The other Options are used to bypass Cloudflare´s Bot Detection
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')
options.add_argument("--allow-running-insecure-content")
driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
time.sleep(2)


# Logging In

driver.get(FalixNodesServerURL)

time.sleep(10)


CookiesButton = driver.find_element_by_xpath("/html/body/cloudflare-app/cf-dialog/cf-dialog-content/cf-dialog-content-text/form/input")
CookiesButton.click()

MailField = driver.find_element_by_name("username")
PassField = driver.find_element_by_name("password")
LoginButton = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/form/div/div[2]/div[3]/button")


MailField.send_keys(MailAdress)
PassField.send_keys(Password)
LoginButton.click()

#print ("Solve Chaptcha")
#input("Press Enter to after you solved the Chaptcha...")

time.sleep(2)

driver.get(FalixNodesServerURL)

time.sleep(5)
print("Script is starting")

wait = WebDriverWait(driver, 10)


StartButton = driver.find_element_by_css_selector("#app > div.sc-2l91w7-0.kBdQEn > div.sc-1p0gm8n-0.cKsaPm > section > div.x3r2dw-0.kbxq2g-0.kHheKg.jlQaqB.sc-1j2y518-0.fWkOrl.fade-appear-done.fade-enter-done > div.sc-1j2y518-1.kouwIw > div.sc-1ikkfm-0.gpqVmG > button.sc-1qu1gou-0.cDMUVV.sc-1ikkfm-1.otvZv")
ConsoleTextField = driver.find_element_by_css_selector("#app > div.sc-2l91w7-0.kBdQEn > div.sc-1p0gm8n-0.cKsaPm > section > div.x3r2dw-0.kbxq2g-0.kHheKg.jlQaqB.sc-1j2y518-0.fWkOrl.fade-appear-done.fade-enter-done > div.sc-1j2y518-6.hiqQuj > div.itaf37-2.imOGfg > div.itaf37-4.bKVHVd > div.itaf37-6.eJbAav > input")


while 3 < 4:
    time.sleep(5)

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
        print("Most likely the Wings from FalixNodes are down. Your Server is still running, but the Script cant restart it at the moment.")
        time.sleep(60)



    if StatusText == " STARTING":
        print("Server is starting")
        time.sleep(30)
