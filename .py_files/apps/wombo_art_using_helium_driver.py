#Initial Imports

import helium as he
# from helium import *
import shutil
import time
from selenium import webdriver

# Function to get wombo art
def create_wombo_art(title, art_style):

    he.start_chrome('https://app.wombo.art')
    he.write(title, into="Type anything")
    he.click(Image(alt = art_style))
    he.click("Create")
    he.wait_until(Text("Name artwork").exists,timeout_secs=60)
    title = title.replace(" " , "_") 
    he.write(title, into="Enter title")
    he.click("Save")
    time.sleep(10)
    original = r"C://Users//Airma//Downloads//" + title + "_TradingCard.jpg"
    target = r"C://Users//Airma//FinTechClass//MiamiClasswork//other_projects//relevant_element//resources//Images//" + title + ".jpg"
    shutil.move(original,target)
    he.kill_browser()
    
    return title