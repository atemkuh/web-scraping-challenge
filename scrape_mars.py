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

ddef scrape():
    browser = init_browser()
    mars_dict ={}

    # Mars News URL of page to be scraped
    source_news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    # Retrieve the latest news title and paragraph
    latest_news_title = news_soup.find_all('div', class_='content_title')[0].text
    latest_news_paragraph = soup.find_all('div', class_='article_teaser_body')[0].text
    #Link to Mars image to be scraped
    nasa_jpl_url ='https://www.jpl.nasa.gov/'
    nasa_jpl_images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(nasa_jpl_images_url)
    soup_images = bs(html,'html.parser')
    # to get featured image
    featured_image_path = soup_images.find_all('img')[3]["src"]
    featured_image_url = nasa_jpl_url+featured_image_path
    