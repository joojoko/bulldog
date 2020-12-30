# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
from GoogleImageScrapper import GoogleImageScraper
import os
import pandas as pd
df = pd.read_csv('mushroom_data_1.csv')
df1 = df['GnrlNm']
df2 = df1.dropna()
MS = df2.tolist()

for i in MS:
    os.chdir("D:\\PycharmProjects\\pythonProject2\\venv\\Google-Image-Scraper-master")
    webdriver_path = os.getcwd() + "\\webdriver\\chromedriver.exe"
    os.chdir("D:\Mushroom_Folder")
    image_path = os.getcwd() + "\\{}".format(i)
    # add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    search_keys = [i]
    number_of_images = 100
    headless = False
    # min_resolution = (width,height)
    min_resolution = (0, 0)
    # max_resolution = (width,height)
    max_resolution = (1920, 1080)
    for search_key in search_keys:
        image_scrapper = GoogleImageScraper(webdriver_path, image_path, search_key, number_of_images, headless,
                                            min_resolution, max_resolution)
        image_urls = image_scrapper.find_image_urls()
        image_scrapper.save_images(image_urls)