#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx


# In[2]:


A = nx.Graph()
A.add_nodes_from(['a', 'b', 'c', 'd'])
A.add_edges_from([('a','b'), ('b','c'), ('c','d'), ('a','c')])
nx.draw(A, with_labels = True)


# In[4]:


list(A.neighbors('b'))


# In[5]:


for neighbor in A.neighbors('b'):
    print(neighbor)


# In[6]:


A.has_node('a')


# In[7]:


nx.is_tree(A)


# In[8]:


nx.is_connected(A)


# In[9]:


A.degree('a')


# In[10]:


B = nx.DiGraph()
B.add_edges_from([('1','2'), ('2','3'), ('1','4'), ('3','4')])
nx.draw(B, with_labels = True)


# In[11]:


C=nx.Graph()
C.add_edges_from([(1,2),(2,3),(1,3),(3,4)])
nx.draw(C,with_labels=True,node_size=500)


# In[12]:


dict(C.degree())


# In[13]:


nx.to_numpy_matrix(C)


# In[16]:


graph=nx.read_edgelist('graph.txt',nodetype=str,create_using=nx.DiGraph())
nx.draw(graph,with_labels=True,node_size=500)

