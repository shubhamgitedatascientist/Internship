#!/usr/bin/env python
# coding: utf-8

# In[30]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# Question 1

# In[28]:


from bs4 import BeautifulSoup
import requests
page=requests.get("https://en.wikipedia.org/wiki/Main_Page")
soup = BeautifulSoup(page.content)
Header=[]
for i in soup.find_all(['h1', 'h2','h3','h4','h5','h6']):
    Header.append(i.text)
import pandas as pd
pd.DataFrame({'Header':Header})


# Question 2

# In[18]:


from bs4 import BeautifulSoup
import requests
page=requests.get("https://presidentofindia.nic.in/former-presidents")
soup = BeautifulSoup(page.content)
Name=[]
for i in soup.find_all('h3'):
    Name.append(i.text)
Term=[]
for i in soup.find_all('h5'):
    Term.append(i.text)
import pandas as pd
pd.DataFrame({'Name':Name,'Term':Term})


# in Question 3 and 4 could not scrap data. may be due to some restriction could not able to get data using class names.

# Question 5

# In[7]:


from bs4 import BeautifulSoup
import requests
page=requests.get("https://www.cnbc.com/world/?region=world")
soup = BeautifulSoup(page.content)
Headline=[]
for i in soup.find_all('a', class_='LatestNews-headline'):
    Headline.append(i.text)
Headline
Time=[]
for i in soup.find_all('span', class_='LatestNews-wrapper'):
    Time.append(i.text)
Time
News_link=[]
for i in soup.find_all('a', class_='LatestNews-headline'):
    News_link.append(i['href'])
News_link
import pandas as pd
pd.DataFrame({'Headline':Headline,'Time':Time,'News_link':News_link})


# Question 6

# In[1]:


from bs4 import BeautifulSoup
import requests
page=requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")
soup = BeautifulSoup(page.content)
paper_title=[]
for i in soup.find_all('h2', class_='sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg'):
    paper_title.append(i.text)
Authors=[]
for i in soup.find_all('span', class_='sc-1w3fpd7-0 dnCnAO'):
    Authors.append(i.text)
Published_Date=[]
for i in soup.find_all('span', class_='sc-1thf9ly-2 dvggWt'):
    Published_Date.append(i.text)
Paper_URL=[]
for i in soup.find_all('a', class_='sc-5smygv-0 fIXTHm'):
    Paper_URL.append(i['href'])
import pandas as pd
pd.DataFrame({'paper_title':paper_title,'Authors':Authors,'Published_Date':Published_Date,'Paper_URL':Paper_URL})


# Question 7

# In[80]:


from bs4 import BeautifulSoup
import requests
page=requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")
soup = BeautifulSoup(page.content)
retaurant_names=[]
for i in soup.find_all('a', class_='restnt-name ellipsis'):
    retaurant_names.append(i.text)
cuisins=[]
for i in soup.find_all('span',attrs={'class': 'double-line-ellipsis'}):
    cuisins.append(i.text)
locations=[]
for i in soup.find_all('div', class_='restnt-loc ellipsis'):
    locations.append(i.text)
Ratings=[]
for i in soup.find_all('div', class_='restnt-rating rating-4'):
    Ratings.append(i.text)
Image_URL=[]
for i in soup.find_all('img', class_='no-img'):
    Image_URL.append(i['data-src'])
import pandas as pd
pd.DataFrame({'Restaurant':retaurant_names,'locations':locations,'cuisins':cuisins,'Ratings':Ratings,'Images':Image_URL})


# In[ ]:




