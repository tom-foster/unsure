from selenium import webdriver


browser = webdriver.Chrome('/mnt/d/Users/Tom/Documents/Python Scripts/chromedriver.exe')
browser.get('http://localhost:8000')

assert 'Django' in browser.title