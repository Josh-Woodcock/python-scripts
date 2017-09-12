#! python3
# download images from imgur based on search term
# irrelevant version using selenium


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

url = 'https://imgur.com/search?q=mountain'

# Download the page
print('Downloading Page %s ... ' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

# Find Image URL
imgElem = soup.select('a > img')
imgURL = 'https:' + imgElem[0].get('src')

# Download Image
print('Downloading image %s ... ' % (imgURL))
res = requests.get(imgURL)
res.raise_for_status()

# Save the image to folder
imageFile = open(os.path.join('mountain', os.path.basename(imgURL)), 'wb')
for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()

print('Done')

