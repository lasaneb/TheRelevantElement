#Initial Imports


from helium import *
import shutil
import time
from selenium import webdriver

# Function to get wombo art
def create_wombo_art(title, art_style):

    helium.start_chrome('https://app.wombo.art')
    helium.write(title, into="Type anything")
    helium.click(Image(alt = art_style))
    helium.click("Create")
    helium.wait_until(Text("Name artwork").exists,timeout_secs=60)
    title = title.replace(" " , "_") 
    helium.write(title, into="Enter title")
    helium.click("Save")
    time.sleep(10)
    original = r"C://Users//Airma//Downloads//" + title + "_TradingCard.jpg"
    target = r"C://Users//Airma//FinTechClass//MiamiClasswork//other_projects//relevant_element//resources//Images//" + title + ".jpg"
    shutil.move(original,target)
    helium.kill_browser()
    
    return title