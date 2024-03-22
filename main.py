import requests as rq
from bs4 import BeautifulSoup as bs
import re

# URL to be scraped
pattern = r'"views":{"simpleText":"(\d+[.]?\d+ \w+)"}'


url = input("Enter the URL: ")

# Make a GET request to fetch the raw HTML content
html_content = rq.get(url).text

# Parse the html content

soup = bs(html_content, "html.parser") # html.parser is the Parser

# print(soup.prettify()) # print the parsed data of html

matches = re.findall(pattern, soup.prettify())

if matches:
    print(matches[0])

# with open("shorts.html", "w", encoding="utf-8") as f:  ##You can save the html file if you want
#     f.write(soup.prettify())

# print(soup.title)
    
# print(soup.title.text)
