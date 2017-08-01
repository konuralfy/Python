# this program 

import pyautogui
import pytesseract
from PIL import Image
import time

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract' #(you need to install Tesseract-OCR first)

screenWidth,screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth,screenHeight)  			# move to Desktop button
pyautogui.click()
pyautogui.typewrite("league")					# type league to find LoL Client
pyautogui.press('enter')					# opens it
time.sleep(8)
pyautogui.moveTo(1600,380)					# goes password textarea
pyautogui.typewrite('xxxxxxxxxxxxx')				# enters password
pyautogui.press('enter')					# login
time.sleep(8)
pyautogui.moveTo(290,100)					# goes to 'Play' button
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(820,920)					# selects game mode 
pyautogui.click()
time.sleep(4)
pyautogui.click()						# goes to 'find match' and clicks it


while True:							# checks if i found a match
    im1 = pyautogui.screenshot('find.png', region=(500, 250, 700, 650))  # takes screenshot of middle of client
    img = Image.open('find.png')
    result = pytesseract.image_to_string(img)			# converts image to text
    if "BULUNDU" in result:					# if there is 'FOUND' in text
        time.sleep(2)
        pyautogui.moveTo(880, 750)				# then clicks 'accept' button 
        pyautogui.click()
        break
								# while im making my coffee :)
		
