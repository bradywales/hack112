import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Returns list of tweets with format ['Name','@handle','Tweet','Url']
def scrapeTwitter():
    driver = webdriver.Chrome("../hack112/chromedriver")
    url = 'https://www.twitter.com/'
    driver.get(url)
    while (driver.current_url != "https://twitter.com/home"):
        print("Logging in")
    print("Success")
    
    result = set()
    time.sleep(2)
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    html = BeautifulSoup(driver.page_source, "html.parser")
    time.sleep(3)
    result.update(html.find_all("div", {"class": "css-1dbjc4n r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l"}))
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    html = BeautifulSoup(driver.page_source, "html.parser")
    result.update(html.find_all("div", {"class": "css-1dbjc4n r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l"}))
    time.sleep(1.5)
    html = BeautifulSoup(driver.page_source, "html.parser")
    result.update(html.find_all("div", {"class": "css-1dbjc4n r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l"}))
    print(result)
    print(len(result))
    results = []
    result = list(result)
    print(result)
    print(len(result))
    for item in result:
        if str(item) == "None":
            continue
        tweet = item.find("div",
                          {
                              "class": "css-901oao r-1fmj7o5 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"})
        name = item.find("span", {"class": "css-901oao css-16my406 css-bfa6kz r-poiln3 r-bcqeeo r-qvutc0"})
        handle = item.find("div", {
            "class": "css-901oao css-bfa6kz r-9ilb82 r-18u37iz r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0"})
        if tweet is None or name is None or handle is None:
            continue
        
        if "/status/" in str(item):
            startUrl = str(item).index("/status/")
            url = "https://twitter.com/" + handle.text[1:] + str(item)[startUrl:startUrl+27]
        else:
            continue
        #if ([name.text, handle.text, tweet.text, url]) not in results:
        results.append([name.text, handle.text, tweet.text, url])
    return results
