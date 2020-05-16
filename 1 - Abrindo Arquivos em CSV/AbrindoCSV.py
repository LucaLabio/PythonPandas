#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
#importando pandas


# In[10]:


#Abrindo o arquivo csv
df = pd.read_csv('Dados aula 1.csv', encoding='utf-8', sep=';')


# In[8]:


#Especificando um cabecalho
df = pd.read_csv('Dados aula 1.csv', encoding='utf-8', sep=';', header=4)


# In[12]:


#Selecionar algumas colunas
df = pd.read_csv('Dados aula 1.csv', encoding='utf-8', sep=';', usecols=["AddressID","AddressLine1"])


# In[14]:


#Lendo X linhas
df = pd.read_csv('Dados aula 1.csv', encoding='utf-8', sep=';', usecols=["AddressID","AddressLine1"], nrows=200)


# In[13]:


#Exibindo o csv
df.head()


# In[15]:


#(Linhas, Colunas)
df.shape

