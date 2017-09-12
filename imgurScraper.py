#! python3
# download images from imgur based on search term

from selenium import webdriver
import webbrowser, sys, requests, os, bs4


# open Firefox at this page
browser = webdriver.Firefox()     
browser.get('https://www.imgur.com/')

# Find search bar, enter term and submit
searchElem = browser.find_element_by_class_name('icon-search')
searchElem.click()

searchBarElem = browser.find_element_by_class_name('search')

searchBarElem.send_keys('mountain')
searchBarElem.submit()


# make directory
os.makedirs('mountain', exist_ok = True)

imgUrl = soup.select('src')

# Download the image
print('Downloading Image %s ... ' % (imgUrl)
res = requests.get(imgUrl)
res.raise_for_status()

# Save the image to folder
imageFile = open(os.path.join('mountain', os.path.basename(imgUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
