from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
import json


class Game:
    def __init__(self, competition, date, home, away, video):
        self.competition = competition
        self.date = date
        self.home = home
        self.away = away
        self.video = video

    def __eq__(self, other):
        return (isinstance(other, self.__class__)) and \
            getattr(other, 'competition', None) == self.competition and \
            getattr(other, 'date', None) == self.date and \
            getattr(other, 'home', None) == self.home and \
            getattr(other, 'away', None) == self.away and \
            getattr(other, 'video', None) == self.video 

    def __ne__(self, other):
        return not self.__eq__(self, other)

    def __hash__(self):
       return hash((self.competition, self.date, self.home, self.away, self.video))
    
    def __repr__(self):
        return "competition = " + self.competition + "\ndate = " + self.date + "\nhome = " + self.home + "\naway = " + self.away + "\nvideo = " + str(self.video)

    def toJson(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)

try:
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    options.add_experimental_option("detach", True)

    seleniumwire_options = {
        'request_storage': 'memory',
        #'ca_key': f'{os.getcwd()}\\ca.key',
        #'ca_cert': f'{os.getcwd()}\\ca.crt'
    }

    #os.system(".\\addCertsToChrome.bat " + ".\\ca.crt")

    driver = webdriver.Chrome(options=options, seleniumwire_options=seleniumwire_options)

    driver.get("https://operation.sportcontract.net/monitoring/games")
    wdwait = WebDriverWait(driver, 20)
    driver.maximize_window()

    wdwait.until(EC.presence_of_element_located((By.ID, "email")))
    wdwait.until(EC.element_to_be_clickable((By.ID, "email")))
    driver.find_element(By.ID, "email").send_keys("robert.sabados13@gmail.com")
    wdwait.until(EC.presence_of_element_located((By.ID, "password")))
    wdwait.until(EC.element_to_be_clickable((By.ID, "password")))
    driver.find_element(By.ID, "password").send_keys("Capriola89SC")
    driver.find_element(By.ID, "password").send_keys(Keys.ENTER)


    rows_set = set()
    old_count = 0
    while True:
        wdwait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'ReactVirtualized__Table__row') and @role='row']")))
        rows = driver.find_elements(By.XPATH, "//div[contains(@class, 'ReactVirtualized__Table__row') and @role='row']")
        for r in rows:
            competition = r.find_element(By.XPATH, ".//div/span/span/a").text
            date = r.find_element(By.XPATH, ".//div[2]/span/span/a").text
            home = r.find_element(By.XPATH, ".//div[3]/span").text
            away = r.find_element(By.XPATH, ".//div[4]/span").text
            video = False
            try:
                r.find_element(By.XPATH, ".//span[contains(@class, 'StatusIcon-module_iconWrapper_ji6XZ')]")
                video = True
            except:
                #try:
                    #r.find_element(By.XPATH, ".//svg[contains(@class, 'video')]")
                    #video = True
                #except:
                    #video = false
                video = False

            game = Game(competition, date, home, away, video)
            rows_set.add(game)
            
            
        new_count = len(rows_set)
        if new_count == old_count:
            break
        old_count = new_count
        last_one = rows[len(rows) - 1]
        driver.execute_script("arguments[0].scrollIntoView()", last_one)

    print(len(rows_set))

    f = open("games.json", "w")
    f.write("[\n")
    for game in rows_set:
        f.write(game.toJson())
        f.write(",\n")
    f.write("{}\n]")
    f.close()

    
    

except Exception as e:
    print(e)

finally:
    print("Enter anything to close:")
    input()
    print("Closing ..")