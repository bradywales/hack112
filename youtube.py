import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# Returns list of youtube videos with format ['Title','Creator','Thumbnail','Link']
def scrapeYoutube():
    driver = webdriver.Chrome("../hack112/chromedriver")
    url = 'https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620'
    driver.get(url)
    while (driver.current_url != "https://www.youtube.com/"):
        print("Logging in")
    print("Success")

    result = set()
    html = BeautifulSoup(driver.page_source, "html.parser")
    result.update(html.find_all("ytd-rich-grid-media", {"class": "style-scope ytd-rich-item-renderer"}))
    results = []
    result = list(result)
    for item in result:
        title = item.find("h3",
                        {"class": "style-scope ytd-rich-grid-media"})
        creator = item.find("a", {"class": "yt-simple-endpoint style-scope yt-formatted-string"})
        thumbnail = item.find("img", {
            "class": "style-scope yt-img-shadow"})
        thumbnail = str(thumbnail)[60:-16]

        url = item.find("a",{"class": "yt-simple-endpoint inline-block style-scope ytd-thumbnail"})
        url = (str(url)[94:114])

        if(title is None):
            break
        if len(str(thumbnail)) > 69:
            if [title.text,creator.text,thumbnail,"https://www.youtube.com"+url] not in results:
                results.append([title.text,creator.text,thumbnail,"https://www.youtube.com"+url])
    return results
