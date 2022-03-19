#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cobra


# In[2]:


from cobra import Model,Reaction,Metabolite


# In[3]:


model=Model('first_model')


# In[4]:


v1=Reaction('v1')
v1.name='v1'
v1.lower_bound=0
v1.upper_bound=1000


# In[5]:


v2=Reaction('v2')
v2.name='v2'
v2.lower_bound=0
v2.upper_bound=1000


# In[6]:


M=Reaction('M')
M.name='M'
M.lower_bound=0
M.upper_bound=1000


# In[7]:


v0=Reaction('v0')
v0.name='v0'
v0.lower_bound=1
v0.upper_bound=1


# In[8]:


v3=Reaction('v3')
v3.name='v3'
v3.lower_bound=.9
v3.upper_bound=.9


# In[9]:


v4=Reaction('v4')
v4.name='v4'
v4.lower_bound=0
v4.upper_bound=1000


# In[10]:


A=Metabolite('A',compartment='c')
B=Metabolite('B',compartment='c')
C=Metabolite('C',compartment='c')
ATP=Metabolite('ATP',compartment='c')


# In[11]:


v1.add_metabolites({A:-1,B:1})


# In[12]:


v2.add_metabolites({B:-1,C:1})


# In[13]:


v0.add_metabolites({A:1})


# In[14]:


M.add_metabolites({C:-1})


# In[15]:


v3.add_metabolites({A:-1,ATP:1})


# In[16]:


v4.add_metabolites({ATP:-1})


# In[17]:


model.add_reactions([v0,v1,v2,v3,v4,M])


# In[18]:


model.objective='M'


# In[19]:


model.optimize()


# In[20]:


model.summary()


# In[ ]:




