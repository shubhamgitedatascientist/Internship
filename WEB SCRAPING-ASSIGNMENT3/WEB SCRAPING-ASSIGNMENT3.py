#!/usr/bin/env python
# coding: utf-8
WEB SCRAPING-ASSIGNMENT3
# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


#import all the required libraries
import pandas as pd
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
import re


# In[3]:


driver = webdriver.Chrome()


# In[4]:


driver.get('https://www.amazon.in/')


# In[5]:


inputU = input('please enter product here--->')


# In[6]:


search_bar = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")         # Finding the search bar using it's xpath
search_bar.send_keys(inputU)                                                                                                 # Inputing keyword to search 
search_button = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")  # Finding the xpath of search button
search_button.click()                                                                                                     # Clicking the search button


# In[7]:


productName=[]


# In[8]:


#scraping the Product_Name 
PName=driver.find_elements(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")
# PName=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for i in PName:
    if i.text is None :
        productName.append("--") 
    else:
        productName.append(i.text)
print(len(productName),productName)


# In[9]:


start_page = 0
end_page = 3
urls = []
for page in range(start_page,end_page+1):
    try:
        page_urls = driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-no-outline"]')
        
        # appending all the urls on current page to urls list
        for url in page_urls:
            url = url.get_attribute('href')     # Scraping the url from webelement
            if url[0:4]=='http':                # Checking if the scraped data is a valid url or not
                urls.append(url)                # Appending the url to urls list
        print("Product urls of page {} has been scraped.".format(page+1))
        
        # Moving to next page
        nxt_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[66]/div/div/div/div/div/div[2]/span/div[2]/div/div/div[2]')      # Locating the next_button which is active
        if nxt_button.text == 'Next→':                                            # Checking if the button located is next button
            nxt_button.click()                                                    # Clicking the next button
            time.sleep(5)                                                         # time delay of 5 seconds
        # If the current active button is not next button, the we will check if the next button is inactive or not    
        elif driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[67]/div/div/span/span[4]').text == 'Next→':    
            print("No new pages exist. Breaking the loop")  # Printing message and breakinf loop if we have reached the last page
            break
            
    except StaleElementReferenceException as e:             # Handling StaleElement Exception   
        print("Stale Exception")
        next_page = nxt_button.get_attribute('href')        # Extracting the url of next page
        driver.get(next_page)        


# In[10]:


prod_dict = {}
prod_dict['Brand']=[]
prod_dict['Name']=[]
prod_dict['Price']=[]
prod_dict['Return/Exchange']=[]
prod_dict['Expected Delivery']=[] 
prod_dict['Availability']=[]
prod_dict['URL']=[]


# In[11]:


for url in urls[:4]:
    driver.get(url)                                                        # Loading the webpage by url
    print("Scraping URL = ", url)
    #time.sleep(2)
    
    try:
        brand = driver.find_element(By.XPATH,'//a[@id="bylineInfo"]')      # Extracting Brand from xpath
        prod_dict['Brand'].append(brand.text)
    except NoSuchElementException:
        prod_dict['Brand'].append('-')
    
    try:
        name = driver.find_element(By.XPATH,'//h1[@id="title"]/span')      # Extracting Name from xpath
        prod_dict['Name'].append(name.text)
    except NoSuchElementException:
        prod_dict['Name'].append('-')
    try:
        price = driver.find_element(By.XPATH,'//span[@id="priceblock_ourprice"]')            # Extracting Price from xpath
        prod_dict['Price'].append(price.text)
    except NoSuchElementException:
        prod_dict['Price'].append('-')
    try:                                                                                     # Extracting Return/Exchange policy from xpath
        ret = driver.find_element(By.XPATH,'//div[@data-name="RETURNS_POLICY"]/span/div[2]/a')
        prod_dict['Return/Exchange'].append(ret.text)
    except NoSuchElementException:
        prod_dict['Return/Exchange'].append('-')
    try:
        delivry = driver.find_element(By.XPATH,'//div[@id="ddmDeliveryMessage"]/b')         # Extracting Expected Delivery from xpath
        prod_dict['Expected Delivery'].append(delivry.text)
    except NoSuchElementException:
        prod_dict['Expected Delivery'].append('-')
    
    try:
        avl = driver.find_element(By.XPATH,'//div[@id="availability"]/span')                # Extracting Availability from xpath
        prod_dict['Availability'].append(avl.text)
    except NoSuchElementException:
        prod_dict['Availability'].append('-')
    
    prod_dict['URL'].append(url)                                                            # Saving url
    time.sleep(2)


# In[12]:


prod_df = pd.DataFrame.from_dict(prod_dict)
prod_df


# In[13]:


#saving data to csv
prod_df.to_csv('Amazon_{}.csv'.format(inputU))


# In[3]:


driver = webdriver.Chrome()


# In[4]:


driver.get('https://images.google.com/')


# In[6]:


search_bar = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')    # Finding the search bar using it's xpath
search_bar.send_keys("fruits")       # Inputing "banana" keyword to search rock images
search_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button')    # Finding the xpath of search button
search_button.click()        # Clicking the search button


# In[7]:


print("start scrolling to generate more images on the page...")
# 500 time we scroll down by 10000 in order to generate more images on the website
for _ in range(500):
    driver.execute_script("window.scrollBy(0,10000)")


# In[8]:


images = driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')


# In[9]:


img_urls = []
img_data = []
for image in images:
    source= image.get_attribute('src')
    if source is not None:
        if(source[0:4] == 'http'):
            img_urls.append(source)
len(img_urls)


# In[16]:


import requests


# In[21]:


for i in range(len(img_urls)):
    if i >= 100:
        break
    print("Downloading {0} of {1} images" .format(i, 100))
    response= requests.get(img_urls[i])
    file = open("H\
    
                :/Flip ROBO/banana/img"+str(i)+".jpg", "wb")
    file.write(response.content)


# In[22]:


driver = webdriver.Chrome()


# In[5]:


url="https://www.digit.in/top-products/best-gaming-laptops-40.html"


# In[6]:


driver.get(url)


# In[7]:


Brands=[]
Products_Description=[]
Specification=[]
Price=[]


# In[9]:


br=driver.find_elements(By.XPATH,"//div[@class='TopNumbeHeading active sticky-footer']")
len(br)


# In[10]:


for i in br:
   
    Brands.append(str(i.text).replace("\n",""))
Brands


# In[12]:


sp=driver.find_elements(By.XPATH,"//div[@class='Specs-Wrap']")
len(sp)


# In[13]:


for i in sp:
   
    Specification.append(str(i.text).replace("\n",""))
Specification


# In[15]:


des=driver.find_elements(By.XPATH,"//div[@class='Section-center']")
len(des)


# In[16]:


for i in des:
   
    Products_Description.append(str(i.text).replace("\n",""))
Products_Description


# In[18]:


pri=driver.find_elements(By.XPATH,"//td[@class='smprice']")
len(pri)


# In[19]:


for i in pri:
   
    Price.append(str(i.text).replace("\n",""))
Price


# In[20]:


digit_lap=pd.DataFrame([])
digit_lap['Brands']=Brands[0:10]
digit_lap['Price']=Price[0:10]
digit_lap['Specification']=Specification[0:10]
digit_lap['Description']=Products_Description[0:10]
digit_lap


# In[23]:


# Question 5-Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps. 

# In[3]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import (
    StaleElementReferenceException,
    NoSuchElementException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
import time
import warnings
import requests

warnings.filterwarnings("ignore")


# In[4]:


driver=webdriver.Chrome()  
driver.maximize_window()
driver.get("https://www.google.com/maps/")
user_input=input("Enter city name for which coordinates is required : ")

time.sleep(5)
search=driver.find_element(By.XPATH,'//input[@autofocus="autofocus"]')
search.click()
search.send_keys(user_input)
search_button=driver.find_element(By.ID,'searchbox-searchbutton')
search_button.click()
time.sleep(5)
lat=[]
long=[]
try:
    url_string = driver.current_url
    print("URL Extracted :",url_string)
    lat_long = re.findall(r'@(.*)data',url_string)
    if len(lat_long):
        lat_long_list = lat_long[0].split(",")
        if len(lat_long_list)>=2:
            lat.append(lat_long_list[0])
            long.append(lat_long_list[1])
except Exception as e:
    print("error:",str(e))

time.sleep(2)
driver.close()

location_data=pd.DataFrame({'Enter Location':user_input,'latitude':lat,'longitude':long})
location_data




# In[24]:


# Question 6-Write a program to scrap all the available details of best gaming laptops from digit.in.Question 7-Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped:
# “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”. Question 8-Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted
# from any YouTube Video. Question-9-Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in
# “London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall
# reviews, privates from price, dorms from price, facilities and property description. 

# In[7]:


url=input("Enter the URL: ")
driver=webdriver.Chrome()  
driver.maximize_window()
driver.get(url)
time.sleep(5)

comments = []
upvote = []
posted = []

for _ in range(30):
    driver.execute_script("window.scrollBy(0,100)")
    time.sleep(3)
    
    com_xpath = driver.find_elements(By.ID,"content-text")
    for i in com_xpath:
        comments.append(i.text)
        
    post = driver.find_elements(By.XPATH,'//yt-formatted-string[@class="published-time-text style-scope ytd-comment-renderer"]')
    for i in post:
        posted.append(i.text)
        
        
    upvotes = driver.find_elements(By.ID,"vote-count-middle")
    for i in upvotes:
        upvote.append(i.text)

        
driver.close()      

youtube_video=pd.DataFrame({'Comments':comments,'Comments Upvote':upvote,'Comment is POSTED':posted})
youtube_video


# In[ ]:




