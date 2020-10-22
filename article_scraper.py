# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:04:33 2018

@author: mjeshtri
"""

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

    
def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)
    
    
def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

# Specify the number of pages to go through
r = 2

for page in range(1, r+1):

    url = 'https://www.brainpickings.org/page/' + str(page)
    raw_html = simple_get(url)
    html = BeautifulSoup(raw_html, 'html.parser')

    part = html.findAll("h1", {"class": "entry-title"})
    print('--------------------------')
    print('\n')
    print('PAGE ', page)
    print('\n')
    for i, j in enumerate(part):
        print(part[i].text)
        print('##########')
        print('LINK: ' , part[i].a['href'])
        print()
