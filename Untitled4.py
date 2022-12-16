#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import matplotlib.pyplot as plt


# In[2]:


from urllib import request


# In[3]:


url = "https://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
type(raw)


# In[19]:


response


# In[20]:


url


# In[21]:


raw


# In[4]:


len(raw)


# In[5]:


raw[:75]


# In[7]:


from nltk import word_tokenize
tokens = word_tokenize(raw)
type(tokens)


# In[8]:


len(tokens)


# In[9]:


tokens[:10]


# In[10]:


from nltk import Text
text = Text(tokens)
type(text)


# In[12]:


text[1024:1062]


# In[13]:


text.collocations()


# In[34]:


raw.find('PART I')


# In[30]:


raw.find("End of Project Gutenberg's Crime")


# In[33]:


raw =raw[5336:1157812]
raw.find('PART I')


# In[37]:


url = 'http://news.bbc.co.uk/1/hi/health/2284783.stm'
html = request.urlopen(url).read().decode('utf8')
html[:100]


# In[36]:


html


# In[38]:


from bs4 import BeautifulSoup
raw = BeautifulSoup(html, 'html.parser').get_text()
tokens = word_tokenize(raw)
tokens


# In[39]:


tokens = tokens[110:390]
text = Text(tokens)
text.concordance('gene')


# In[ ]:




