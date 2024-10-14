from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os

try:
    #cService = webdriver.ChromeService(executable_path="C:\\Users\\Strahinja\\Documents\\cp\\python\\hockey\\chromedriver.exe")
    
    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}

    #driver = webdriver.Chrome(service=cService)
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    options.add_experimental_option("detach", True)
    
    seleniumwire_options = {
        'request_storage': 'memory',
        'ca_key': f'{os.getcwd()}\\ca.key',
        'ca_cert': f'{os.getcwd()}\\ca.crt'
    }

    #add certs to chrome
    os.system(".\\addCertsToChrome.bat " + ".\\ca.crt")


    driver = webdriver.Chrome(options=options, seleniumwire_options=seleniumwire_options)


    driver.get("https://www.svenskhockey.tv/sv/game/66ffb7ecee56f13ea003f6c0")
    wdwait = WebDriverWait(driver, 20)



    #try and accept cookies
    wdwait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"ion-overlay-2\"]/app-cookie-settings-modal/app-modal-footer/ion-footer/ion-grid/ion-row/div[2]/ion-button")))
    wdwait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"ion-overlay-2\"]/app-cookie-settings-modal/app-modal-footer/ion-footer/ion-grid/ion-row/div[2]/ion-button")))
    driver.find_element(By.XPATH, "//*[@id=\"ion-overlay-2\"]/app-cookie-settings-modal/app-modal-footer/ion-footer/ion-grid/ion-row/div[2]/ion-button").click()

    wdwait.until(EC.presence_of_element_located((By.ID, "login-email")))
    wdwait.until(EC.element_to_be_clickable((By.ID, "login-email")))
    driver.find_element(By.ID, "login-email").send_keys("soskicilija@hotmail.com")
    driver.find_element(By.ID, "login-password").send_keys("Il!ja064")
    driver.find_element(By.ID, "login-password").send_keys(Keys.ENTER)


    time.sleep(30) #experiment with time
    videos = set()
    for request in driver.requests:
        if request.response:
            if ".m3u8" in request.url:
                videos.add(request.url)
                print(request.url)
                print("===")

    wdwait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root-play-site/ion-app/ion-nav/app-view/div/ion-header/ion-toolbar/ion-buttons[2]/ion-button[2]")))
    wdwait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root-play-site/ion-app/ion-nav/app-view/div/ion-header/ion-toolbar/ion-buttons[2]/ion-button[2]")))
    driver.find_element(By.XPATH, "/html/body/app-root-play-site/ion-app/ion-nav/app-view/div/ion-header/ion-toolbar/ion-buttons[2]/ion-button[2]").click()

    #time.sleep(1)
    if "en/" in driver.current_url:
        wdwait.until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(., 'Log out')]]")))
        driver.find_element(By.XPATH, "//*[text()[contains(., 'Log out')]]").click()
    else:
        wdwait.until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(., 'Logga ut')]]")))
        #dowdwait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()[contains(., 'Logga ut')]]")))
        driver.find_element(By.XPATH, "//*[text()[contains(., 'Logga ut')]]").click() #TODO: preci na JS executor jer nekada nije u vidiku

    driver.close()

    for video in videos:
        os.system(".\\download.bat " + "\"" + video + "\"")

    #print("sleeping")
    #time.sleep(5)
    #print("done")

except Exception as e:
    print(e)

finally:
    print("Enter anything to close:")
    input()
    print("Closing ..")











