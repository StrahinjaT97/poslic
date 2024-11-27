from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as DC
import time
import os
import sys

#arg 1 - site url
#arg 2 - username
#arg 3 - password

try:
    cService = webdriver.ChromeService(executable_path="..\\res\\chromedriver.exe", log_output='NUL')


    driver = webdriver.Chrome(service=cService)
    driver.maximize_window()
    wdwait = WebDriverWait(driver, 5) #TODO: Vratiti na neko bolje verem

    driver.get(sys.argv[1])

    #try and accept cookies
    #TODO: promeniti iz xpath u nesto pametnije
    wdwait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"ion-overlay-2\"]/app-cookie-settings-modal/app-modal-footer/ion-footer/ion-grid/ion-row/div[2]/ion-button")))
    wdwait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"ion-overlay-2\"]/app-cookie-settings-modal/app-modal-footer/ion-footer/ion-grid/ion-row/div[2]/ion-button")))
    driver.find_element(By.XPATH, "//*[@id=\"ion-overlay-2\"]/app-cookie-settings-modal/ion-content/app-cookie-selection/div[2]/ion-list/div[2]/ion-toggle").click()
    driver.find_element(By.XPATH, "//*[@id=\"ion-overlay-2\"]/app-cookie-settings-modal/ion-content/app-cookie-selection/div[2]/ion-list/div[3]/ion-toggle").click()
    driver.find_element(By.XPATH, "//*[@id=\"ion-overlay-2\"]/app-cookie-settings-modal/app-modal-footer/ion-footer/ion-grid/ion-row/div[2]/ion-button").click()
    
    #log in
    time.sleep(2) #TODO: bez ovoga klikce na pogresno dugme
    wdwait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root-play-site/ion-app/ion-nav/app-view/div/ion-header/ion-toolbar/ion-buttons[2]/ion-button[1]")))
    wdwait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root-play-site/ion-app/ion-nav/app-view/div/ion-header/ion-toolbar/ion-buttons[2]/ion-button[1]")))
    driver.find_element(By.XPATH, "/html/body/app-root-play-site/ion-app/ion-nav/app-view/div/ion-header/ion-toolbar/ion-buttons[2]/ion-button[1]").click()
    wdwait.until(EC.presence_of_element_located((By.ID, "login-email")))
    wdwait.until(EC.element_to_be_clickable((By.ID, "login-email")))
    driver.find_element(By.ID, "login-email").send_keys(sys.argv[2])
    driver.find_element(By.ID, "login-password").send_keys(sys.argv[3])
    driver.find_element(By.ID, "login-password").send_keys(Keys.ENTER)

    #fetch video links
    videos = driver.find_elements(By.XPATH, "//app-upcoming-past-broadcasts/app-card-list")[0]\
        .find_elements(By.XPATH, "*//div[@class='card card-clickable card-hover']")
    print(len(videos))


except Exception as e:
    print(e)

finally:
    try:
        #log out
        time.sleep(2) #TODO: bez ovoga zibacuje stale element
        driver.find_element(By.XPATH, "/html/body/app-root-play-site/ion-app/ion-nav/app-view/div/ion-header/ion-toolbar/ion-buttons[2]/ion-button[2]").click()
        if "en/" in driver.current_url:
            wdwait.until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(., 'Log out')]]")))
            wdwait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()[contains(., 'Log out')]]")))
            driver.find_element(By.XPATH, "//*[text()[contains(., 'Log out')]]").click()
        else:
            wdwait.until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(., 'Logga ut')]]")))
            wdwait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()[contains(., 'Logga ut')]]")))
            driver.find_element(By.XPATH, "//*[text()[contains(., 'Logga ut')]]").click()

    except Exception as e:
        print(e)
    
    finally:
        print("Enter anything to close:")
        input()
        print("Closing ...")