#! python3
# download images from imgur based on search term

import webbrowser, sys, requests, os, bs4

category = sys.argv[1]      # message is second

url = 'https://imgur.com/search?q=' + category 

# Download the page
print('Downloading Page %s ... ' % url)
res = requests.get(url)
res.raise_for_status()

# create the soup
soup = bs4.BeautifulSoup(res.text, "html.parser")

# make directory
os.makedirs(category, exist_ok = True)

i = 0

for link in soup.find_all('img'):

     # Find Image in the soup
    imgElem = soup.select('img')
    imgURL = 'https:' + imgElem[i].get('src')

    if not imgURL.startswith('https://s.'):

        # Download Image
        print('Downloading %s ... ' % (imgURL))
        res = requests.get(imgURL)
        res.raise_for_status()

        # Save the image to folder
        imageFile = open(os.path.join(category, os.path.basename(imgURL)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        i += 1
        
print('Done')

