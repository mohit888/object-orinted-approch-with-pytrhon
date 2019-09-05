#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# In[ ]:


class Employe:
    no_of_employes = 0
    raise_amount =1.4
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@gmail.com"
        
        Employe.no_of_employes += 1
    def Fullname(self):
        return ('{} {}'.format(self.first, self.last))

emp1 = Employe("mohit","batra",59499)
emp2 = Employe("prince","jain",43366)
print(emp1.email)
print(emp2.email)
print(Employe.Fullname(emp1))
print(Employe.no_of_employes)


# This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).
# 
# Outline of some basics:
# 
# * [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)
# * [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)
# * [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)
# * [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)
# * [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)
# * [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)
# * [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages.

# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/ipython/ipython-in-depth
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook

# In[3]:


class Employe:
    no_of_employes = 0
    raise_amount =1.4
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@gmail.com"
        
        Employe.no_of_employes += 1
    def Fullname(self):
        return ('{} {}'.format(self.first, self.last))

emp1 = Employe("mohit","batra",59499)
emp2 = Employe("prince","jain",43366)
print(emp1.email)
print(emp2.email)
print(Employe.Fullname(emp1))
print(Employe.no_of_employes)
print(emp1.raise_amount)
emp1.raise_ammount = 5.7
print(emp2.raise_amount)



# In[ ]:





# In[ ]:





# In[ ]:




