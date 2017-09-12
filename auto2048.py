#1 python3
# auto plays 2048

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
# gameOverElem = browser.find_element_by_class_name('game-message game-over')

for x in range(0,100):
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)

