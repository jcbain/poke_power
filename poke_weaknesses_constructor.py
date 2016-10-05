from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import html5lib
import csv
import re

# create function to read in the html of webpage
def makeSoup(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"html.parser")
    return soup

# create the soup and find all of the titles of the td rows
# this contains information about attacker -> defender = effectiveness
the_soup = makeSoup('http://pokemondb.net/type')
weaknesses = [row['title'] for row in the_soup.findAll(['td'])]

# create list of list by removing stupid characters
# should end up being three strings per list
list_of_lists = []
for i in weaknesses:
    list_of_lists.append(re.split('→|=',i))

# write list of lists to a csv object for future reference
with open("datasets/weaknesses.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(new)
