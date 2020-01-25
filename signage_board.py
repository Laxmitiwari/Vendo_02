import urllib3
from time import sleep
from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
http = urllib3.PoolManager()
driver.maximize_window()

def wait_for_internet_connection():
    while True:
        try:

            response = http.request('GET', 'https;//www.youtube.com')
            return
        except:
            print('No internet connection.\nTrying after 5 seconds.\n')
            sleep(5)

wait_for_internet_connection()
driver.get('https://www.bing.com')
driver.close()



