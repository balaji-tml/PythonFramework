def open_website(url):
   from selenium import webdriver
   import time
   driver = webdriver.Chrome()
   driver.get(url)
   time.sleep(2)
   print("Page title is:",driver.title)
   driver.quit()


if __name__ == '__main__':
   url = "https://lambdatest.com/selenium-playground"
   open_website(url)


