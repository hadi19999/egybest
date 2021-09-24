import requests
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import wget

chrome_options = Options()

chrome_options.add_argument("--headless")

driver = webdriver.Chrome("chromedriver",options=chrome_options)

def get_movies():
    driver.get("https://best.egybest.film:2053/egbest/")
    time.sleep(10)

    items = driver.find_elements_by_css_selector("[class='owl-item']")
    movies = []
    counter = 0
    for item in items:
        counter = counter + 1
        movies.append({
            "id": counter,
            "name": item.find_element_by_tag_name('h3').get_attribute('innerHTML'),
            "link": item.find_element_by_tag_name('a').get_attribute('href')
        })
    return movies


# movie = get_movies()[0]

def get_quality(movie):
    driver.get(movie['link'])
    links = driver.find_elements_by_css_selector("[class='tr flex-start'")
    qualities = []
    counter = 0
    for link in links:
        counter = counter + 1
        qualities.append({
            "id": counter,
            "name": link.find_elements_by_tag_name('div')[2].get_attribute('innerHTML'),
            "link": link.find_element_by_tag_name('a').get_attribute('href')
        })
    return qualities

def get_link(quality):
    driver.get(quality['link'])
    time.sleep(7)
    link = driver.find_element_by_id("goNow").get_attribute('href')
    return link

def display():
    movies = get_movies()
    for movie in movies:
        print(movie['id'],movie['name'])
    movie_id = int(input("Enter movie number: "))
    qualities = get_quality(movies[movie_id-1])
    for quality in qualities:
        print(quality['id'],quality['name'])
    quality_id = int(input("Enter quality number: "))
    link = get_link(qualities[quality_id-1])
    # print(link)
    print('Donwloading...')
    wget.download(link)
    print("Download completed")

display()
driver.close()