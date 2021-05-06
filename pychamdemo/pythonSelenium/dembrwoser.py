from selenium import webdriver
#every browser has an executable file
#through selenium test we need to invoke the executable file which will then invoke actual browser
driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")

driver.get("https://www.selenium.dev/")  #get method to hit the url on browser
