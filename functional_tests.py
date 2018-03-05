from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# profile = FirefoxBinary(firefox_path='firefox')
# profile = FirefoxBinary(firefox_path="/mnt/c/'Program Files (x86)'/'Mozilla Firefox'/firefox.exe")
# profile = FirefoxBinary(firefox_path='/mnt/c/Users/Tom/Desktop/firefox.txt')
# # profile.set_preference("/mnt/c/'Program Files (x86)'/'Mozilla Firefox'/firefox.exe", 0)
# fp = webdriver.FirefoxProfile()
# browser = webdriver.Firefox(firefox_binary=profile, firefox_profile=fp)
browser = webdriver.Chrome('/mnt/d/Users/Tom/Documents/Python Scripts/chromedriver.exe')
browser.get('https://google.com')
# browser.get('http://localhost:8000')

# assert 'Django' in browser.title