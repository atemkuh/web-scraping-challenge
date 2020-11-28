from flask_app import scrape
import os
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests as reg

def init_browser():
    # path to chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
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
def scrape():
    browser = init_browser()

    nasa_jpl_url ='https://www.jpl.nasa.gov/'
    nasa_jpl_images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(nasa_jpl_images_url)
    soup_images = bs(html,'html.parser')

# to get featured image
    featured_image_path = soup_images.find_all('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
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

    # Scrape USGS webpage for Mars hemispehere images
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, "html.parser")

    # store titles & links in dict
    hemisphere_image_urls = []

    # Retrieve all data containing image
    results = soup.find("div", class_ = "result-list" )
    hemispheres = results.find_all("div", class_="item")

    # Iterate through each image
    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        html = browser.html
        soup = bs(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        hemisphere_image_urls.append({"title": title, "img_url": image_url})

    mars_dict = {
        "latest_news_title": latest_news_title,
        "latest_news_paragraph": latest_news_paragraph,
        "featured_image_url": featured_image_url,
        "mars_facts_html": str(mars_facts_html),
        "hemisphere_images": hemisphere_image_urls
    }