import requests, pprint
from bs4 import BeautifulSoup

# pip install requests
# pip install BeautifulSoup4

# resp = requests.get('http://google.com') # send request to website which you want to scrape
# print(resp.text) #print out as text (string)

resp = requests.get('https://brickset.com/minifigs/year-2001/page-1') # send request to website which you want to scrape
# print(resp.text) #print out as text (string)

# resp.content is byte type
soup = BeautifulSoup(resp.content, 'html.parser') #return an instance of BeautifulSoup

items = []
for element in soup.find_all(class_='meta'): 
    #the info we want is in the div which class = "meta" ; find_all is a build-in function in beautifulsoup.return is a list with all the meta divs
    # print(element.h1) #element + dot to print first html tags

    href = f"https://brickset.com/{element.h1.a['href']}" #to store detail info link of this minifigure
    title = element.h1.a.text # get html inner text to form a title

    tags = {} 
    for a in element.find_all(class_='tags')[0].find_all('a'): #also can use find_all() to get all specified html tag
        tags[a.text] = f"https://brickset.com/{a['href']}"
    
    data = {
        'title': title,
        'href': href,
        'tags': tags
    }
    items.append(data)

last_href = soup.find(class_='last').a['href'] # the html has a class = "last" which is the last page of the minifigs, we can use a for loop to get all pages' info

pprint.pprint(items)

