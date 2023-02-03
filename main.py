# phere we are going to scrape website using python. first of all we need few libraries with the help of which we can complete our task and the libraries are 
# 1. requests -- this library is use to request from the server to provide the set of commanda which are used in making that website basically it will request the html code from that website and return that in the form string. An HTTP GET request is used to retrieve data from the specified resource, such as a website. When using the Python requests library, you can use the . get() function to create a GET request for a specified resource.

# 2. bs4 beautiful soup to arrangel that string in the readable structure

# 3. html5lib to parse 

# ----------- program begins
import requests
from bs4 import BeautifulSoup
import html5lib



url = "https://codewithharry.com/"
r = requests.get(url)
# now to get html content of specific url we use 
htmlContent = r.content

# Now we are going to parse html content 
soup = BeautifulSoup(htmlContent, 'html.parser')
#soup is basically a tree which consists of all the tags used in particular website
soup.prettify()
# print(soup)

# now we are going to make a tree of that soup which will help us to make things more clear and we can traverse easily

# we are scraping title of that website
title = soup.title
# print(title)
# finding all the paragraphs used in that particular websites
paras = soup.find_all('p')
# print(paras)


# now to get first element simply use 
# print(soup.find('div'))#-- will return first div of tree
# print(soup.find('p')['class'])#00 return the name of class of first div tag

# to find all the element whose class name is "abc"

# print(soup.find_all('p', class_="text-sm"))


# get the text from particular elements
# print(soup.find('p').get_text()) 

# to find all the anchor tags simply use 
anchors = soup.find_all('a')
# print(anchors)
# get all the links on the page 
all_links = set()
for links in anchors:
    link = links.get('href')
    all_links.add(link)
    print(all_links)
    