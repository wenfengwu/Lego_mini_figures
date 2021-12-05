import requests, pprint
from bs4 import BeautifulSoup
import re
import json, os
# pip install requests
# pip install BeautifulSoup4
regex = re.compile(r'https:\/\/brickset\.com\/minifigs\/year-(\d{4})\/page-(\d{1,3})')
# resp = requests.get('http://google.com') # send request to website which you want to scrape
# print(resp.text) #print out as text (string)
def fetch(year, page=None):
    if not page:
        page = 1
    filename = f'{year}-{page}.json'
    if os.path.exists(filename):#check if file has already been scraped
        return

    resp = requests.get(f'https://brickset.com/minifigs/year-{year}/page-{page}') # send request to website which you want to scrape
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

    with open(filename, 'w') as jsonfile: # 'w' means write. Default is read
        json.dump(items, jsonfile, indent=4) # write json to file

    last_href = soup.find(class_='last').a['href'] # the html has a class = "last" which is the last page of the minifigs, we can use a for loop to get all pages' info
    result = regex.findall(last_href)
    # result = [('2001', '4')]
    for page_num in range(page + 1 , int(result[0][1])):
        fetch(year, page_num)
    #fetch(result[0][0], result[0][1])
    # fetch(*result[0])
    # pprint.pprint(items)

for year in range(2021, 1975, -1): 
    fetch(year, 1)
