import os
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import pymongo

def init_browser():
    # path to chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    Browser = init_browser()
    mars_dict ={}

    #URL of Mars data to be scraped
    news_url = 'https://mars.nasa.gov/news/'
    Browser.visit(news_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    