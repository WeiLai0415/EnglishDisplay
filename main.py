# coding: utf8
from urllib.request import urlopen 
from bs4 import BeautifulSoup


html = urlopen("https://www.simplyquotes.com/quotes")
bsObj = BeautifulSoup(html)
