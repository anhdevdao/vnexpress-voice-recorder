# -*- coding: utf-8 -*-

import requests
import pandas as pd
import urllib
import re

from bs4 import BeautifulSoup
from vnnews import const

def listToString(s):
    space = " " 
    breakLine = "\n"
    text = space.join(s)
    array = re.split(r'(?<=\.) ', text)
    return (breakLine.join(array))

def get_article_content(url, s=0):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    if s == 1:
        title = soup.find('h1',attrs={"class":"title_gn_detail"}).string

        if soup.find_all('p',attrs={"class":"Normal"}):
            content_array = soup.find_all('p',attrs={"class":"Normal"})
            content_array.pop() # Remove p/s
            content = []
            for ct in content_array:
                content.append(ct.text)
            text = listToString(content)

            if soup.find('span',attrs={"class":"location-stamp"}):
                location = soup.find('span',attrs={"class":"location-stamp"})
                description = location.next_sibling # Description after location span tag
                return (title + "\n" + location.string + "\n" + description + "\n" + text)
            else:
                if soup.find('p',attrs={"class":"description"}):
                    description = soup.find('p',attrs={"class":"description"})
                    return (title + "\n" + description + "\n" + text)
                else: 
                    return (title + "\n" + text)
        else:
            return title

    else:
        title = soup.find('h1',attrs={"class":"title_news_detail"}).string

        if soup.find_all('p',attrs={"class":"Normal"}):
            content_array = soup.find_all('p',attrs={"class":"Normal"})
            content_array.pop() # Remove p/s
            content = []
            for ct in content_array:
                content.append(ct.text)
            text = listToString(content)

            if soup.find('p',attrs={"class":"description"}):
                description = soup.find('p',attrs={"class":"description"})
                return (title + "\n" + description.text + "\n" + text)

            if soup.find('span',attrs={"class":"location-stamp"}):
                location = soup.find('span',attrs={"class":"location-stamp"})
                description = location.next_sibling # Description after location span tag
                return (title + "\n" + location.text + "\n" + description + "\n" + text)
            else:
                return (title + "\n" + text)
        else:
            return title


def thoisu():
    data = get_article_content(const.VNEXPRESS_THOISU)
    return data

def gocnhin():
    data = get_article_content(const.VNEXPRESS_GOCNHIN, 1)
    return(data)

def thegioi():
    data = get_article_content(const.VNEXPRESS_THEGIOI)
    return(data)

def kinhdoanh():
    data = get_article_content(const.VNEXPRESS_KINHDOANH)
    return(data)

def giaitri():
    data = get_article_content(const.VNEXPRESS_GIAITRI)
    return(data)

def thethao():
    data = get_article_content(const.VNEXPRESS_THETHAO)
    return(data)

def phapluat():
    data = get_article_content(const.VNEXPRESS_PHAPLUAT)
    return(data)

def giaoduc():
    data = get_article_content(const.VNEXPRESS_GIAODUC)
    return(data)

def suckhoe():
    data = get_article_content(const.VNEXPRESS_SUCKHOE)
    return(data)

def doisong():
    data = get_article_content(const.VNEXPRESS_DOISONG)
    return(data)

def dulich():
    data = get_article_content(const.VNEXPRESS_DULICH)
    return(data)

def khoahoc():
    data = get_article_content(const.VNEXPRESS_KHOAHOC)
    return(data)

def sohoa():
    data = get_article_content(const.VNEXPRESS_SOHOA)
    return(data)

def xe():
    data = get_article_content(const.VNEXPRESS_XE)
    return(data)

def ykien():
    data = get_article_content(const.VNEXPRESS_YKIEN)
    return(data)

def tamsu():
    data = get_article_content(const.VNEXPRESS_TAMSU)
    return(data)


