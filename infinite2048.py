#! python3
# infinitely plays 2048

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException        
import webbrowser

# open web browser
browser = webdriver.Firefox()     
browser.get('https://gabrielecirulli.github.io/2048/')

# Find New Game Button
newGameElem = browser.find_element_by_class_name('restart-button')
newGameElem.click()

# Key Press
htmlElem = browser.find_element_by_tag_name('html')

#Your Score

class tryAgainExist:
    if browser.find_element_by_link_text('Try again') is True:
        newGameElem.click()
    else:
        pass

for x in range(0,100):
    htmlElem.send_keys(Keys.UP)
    tryAgainExist
    htmlElem.send_keys(Keys.RIGHT)
    tryAgainExist()
    htmlElem.send_keys(Keys.DOWN)
    tryAgainExist()
    htmlElem.send_keys(Keys.LEFT)
    tryAgainExist()

 
# TODO: Find a way to click try again button when it appears. Best bet is to
# check for it after every key press. Problem I'm having is that selenium doesn't
# find element it crashes. Need a way to stop this. Have tried a TRY but it
# menas I can't click on element.



    
