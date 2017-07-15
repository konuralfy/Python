import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

# automaticly opens Chrome connects youtube-mp3 and download it

url = input("Please enter the URL: ")
if not url[:8] == "https://":
    url = "https://" + url

print("Progressing...")

driver = webdriver.Chrome(os.path.join(os.path.dirname(__file__),'chromedriver'))
driver.get("http://www.youtube-mp3.org")
inputElement = driver.find_element_by_id("youtube-url")
inputElement.clear()
inputElement.send_keys(url)
inputElement.send_keys(Keys.ENTER)
time.sleep(2)

# The website creates link more than one. So i picked the long one with this code

driver.execute_script('var a=document.getElementById("dl_link");'
                      'var ChdNum = a.children.length;'
                      'for(var i=0;i<ChdNum;i++){var b = a.children[i];'
                      'if (b.toString().length >=115){b.click()}}'
                      )



					  

time.sleep(8)					  
driver.close()
print ("Mp3 file will be in your 'Download' folder")
time.sleep(3)
driver.quit()