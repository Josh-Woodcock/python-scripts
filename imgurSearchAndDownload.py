#! python3
# download images from imgur based on search term

from selenium import webdriver
import webbrowser, sys, requests, os, bs4

url = 'https://imgur.com/search?q=%mountain'

# Download the page
print('Downloading Page %s ... ' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

# make directory
os.makedirs('mountain', exist_ok = True)

i = 0

for link in soup.find_all('img'):

    imgElem = soup.select('a > img')
    imgURL = 'https:' + imgElem[i].get('src')

    # Download Image
    print('Downloading %s ... ' % (imgURL))
    res = requests.get(imgURL)
    res.raise_for_status()

    # Save the image to folder
    imageFile = open(os.path.join('mountain', os.path.basename(imgURL)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    i += 1
    
print('Done')

