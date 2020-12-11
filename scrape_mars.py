from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import pymongo

def init_browser():
    # path to chromedriver
    executable_path = {"executable_path": "chromedriver"}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dict ={}

    # Mars News URL of page to be scraped
    source_news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    html = browser.html
    mars_soup = bs(html, 'html.parser')


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
    featured_image_url = nasa_jpl_url + featured_image_path

# Mars Facts


    # Visit Mars facts url 
    facts_url = 'https://space-facts.com/mars/'
    get_facts_list_df = pd.read_html(facts_url)
    facts_table_df = tables[2]
    facts_table_df.columns = ["Description", "Value"]
    mars_facts_html = mars_facts_df.to_html()
    mars_facts_html.replace('\n', '')

# Hemispheres data scraping
    usgs_url = 'https://astrogeology.usgs.gov'
    hspheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hspheres_url)
    hspheres_html = browser.html
    hspheres_soup = bs(hspheres_html, 'html.parser')
    # get data from Mars hemispheres
    all_hspheres_data = hspheres_soup.find('div', class_='collapsible results')
    mars_hspheres = all_hspheres_data.find_all('div', class_='item')
    hsphere_image_urls = []
    # traverse through each hemisphere data
    for i in hemispheres:
        # Collect Title
        hemisphere = i.find('div', class_="description")
        title = hsphere.h3.text        
        # Collect image link by browsing to hemisphere page
        hsphere_link = hsphere.a["href"]    
        browser.visit(usgs_url + hsphere_link)        
        image_html = browser.html
        image_soup = bs(image_html, 'html.parser')        
        image_link = image_soup.find('div', class_='downloads')
        image_url = image_link.find('li').a['href']
        #Store title and url info in a dict
        image_dict = {}
        image_dict['title'] = title
        image_dict['img_url'] = image_url        
        hsphere_image_urls.append(image_dict)

    mars_dict = {
        "latest_news_title": latest_news_title,
        "latest_news_paragraph": latest_news_paragraph,
        "featured_image_url": featured_image_url,
        "mars_facts_html": str(mars_facts_html),
        "hemisphere_images": hsphere_image_urls
    } 
    return mars_dict