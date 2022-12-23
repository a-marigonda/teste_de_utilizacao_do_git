#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
import io

url = r"http://portalweb.cooxupe.com.br:8080/portal/precohistoricocafe_2.jsp;jsessionid=B2ED3F65AF31A3D2F4638E744FC9D6F7?d-3496238-e=2&6578706f7274=1"

conteudo_url = requests.get(url).content
print(conteudo_url)


# In[29]:


url_decodificada = io.StringIO(conteudo_url.decode('latin1'))

for item in url_decodificada:
    meses = item
    break
    
# Remoção de espaços antes e depois do texto
meses = meses.strip()

meses = meses.split(" ")

meses = str(meses)

print(type(meses))
print(meses)

print(meses.find('Janeiro'))

meses = meses.remove("Janeiro")

print(meses)


# In[ ]:




