# import necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

def bowl_list_dict_init():
    """Function that creates an empty dictionary of the bowlers columns"""
    list_dicts = {'Player':[], "Span":[],"Mat":[],"Inns":[], "Balls":[],"Runs":[],"Wkts":[], "BBI":[],"BBM":[],"Ave":[],"Econ":[], "SR":[],"5":[],"10":[]}
    return list_dicts

def bowl_row_append(url, **dictionary):
    """Function takes in the website url, dictionary. It then appends new elements to each of the dictionary lists"""
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    tables = soup.find_all('table',{'class':'engineTable'})
    table = tables[2]
    rows = table.find_all('tr')
    for col in rows:
        elements = col.find_all('td')
        if elements != []:
            dictionary['Player'].append(elements[0].text.strip())
            dictionary['Span'].append(elements[1].text.strip())
            dictionary['Mat'].append(elements[2].text.strip())
            dictionary['Inns'].append(elements[3].text.strip())
            dictionary['Balls'].append(elements[4].text.strip())
            dictionary['Runs'].append(elements[5].text.strip())
            dictionary['Wkts'].append(elements[6].text.strip())
            dictionary['BBI'].append(elements[7].text.strip())
            dictionary['BBM'].append(elements[8].text.strip())
            dictionary['Ave'].append(elements[9].text.strip())
            dictionary['Econ'].append(elements[10].text.strip())
            dictionary['SR'].append(elements[11].text.strip())
            dictionary['5'].append(elements[12].text.strip())
            dictionary['10'].append(elements[13].text.strip())
                
    return 

def bowl_database_init(last_page, url1, url2):
    """"Function takes in the last page of of the bowlers website database and the two halves of the url. Returns a dataframe 
    of all the test bowlers that have taken a test wicket"""
    
    bowl_list_dict = bowl_list_dict_init()
    for i in range(1, last_page, 1):
        url = url1 + str(i) + url2 # concatenates the two halves of the url with the page number in the middle
        bowl_row_append(url, **bowl_list_dict)
        
    bowl_df = pd.DataFrame(bowl_list_dict)
    
    return bowl_df

def bat_list_dict_init():
    """Function that creates an empty dictionary of the batters columns"""
    
    list_dict = {'Player':[], "Span":[],"Mat":[],"Inns":[], "No":[],"Runs":[],"HS":[], "Ave":[],"100":[],"50":[],"0":[]}
    return list_dict

def bat_row_append(url, **dictionary):
    """Function takes in the website url, dictionary. It then appends new elements to each of the dictionary passed in"""
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    tables = soup.find_all('table',{'class':'engineTable'})
    table = tables[2]
    rows = table.find_all('tr')
    for col in rows:
        elements = col.find_all('td')
        if elements != []:
            dictionary['Player'].append(elements[0].text.strip())
            dictionary['Span'].append(elements[1].text.strip())
            dictionary['Mat'].append(elements[2].text.strip())
            dictionary['Inns'].append(elements[3].text.strip())
            dictionary['No'].append(elements[4].text.strip())
            dictionary['Runs'].append(elements[5].text.strip())
            dictionary['HS'].append(elements[6].text.strip())
            dictionary['Ave'].append(elements[7].text.strip())
            dictionary['100'].append(elements[8].text.strip())
            dictionary['50'].append(elements[9].text.strip())
            dictionary['0'].append(elements[10].text.strip())               
    return 

def bat_database_init(last_page, url1, url2):
    """"Function takes in the last page of of the bowlers website database and the two halves of the url. Returns a dataframe 
    of all the test batters to have scored a run"""
    
    bat_list_dict = bat_list_dict_init()
    for i in range(1,last_page,1):
        url = url1 + str(i) + url2
        bat_row_append(url, **bat_list_dict)
        
    bat_df = pd.DataFrame(bat_list_dict)
    return bat_df
