#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import supervisely as sly
from tqdm import tqdm
import random
import os


team_name = "AI Team - Defects"
workspace_name = "Defects"
project_name = "Defects"


serv = input("whats your server? quantigo or ag or app or Oddbot or kill-sup: ")
if serv == "quantigo" :
    address = "quantigo.supervise.ly" #os.environ['SERVER_ADDRESS']
    token = "lxR3U7rp1Y2aFld8wLUEjDgdH5RyquUMaFvOwTIa4uSAP9WyT2VY1TaBzLeqa3RYy1n7gpxwbNZxT4HUsJbDD5iZVtbYKu99UAlUKBdErRU44tr9BjQ4rvgux93S3Iq6"
    api = sly.Api(address, token)
if serv == "ag":
    address = 'https://ag-quantigo.supervise.ly/'
    token = 'TbUAAv0Qgt0xOcnMtFlvupKiuMCoPa7lC9GELg8WExiyxfBy9ehWT6snxmSwaImk79B0HSAmGOPXp6imwDms3RWLImC85rD81CmbO9xcqfIVfvNwNflQxzlOIZeI2d5k'
    api = sly.Api(address, token)
if serv == "app":
    address = "https://app.supervise.ly/" #os.environ['SERVER_ADDRESS']
    token = "55uQoEbOlfANSIrSuAU4YlsO6vlXlePuTYiW7umlWhTUEP4J16hPzvm5nIzE57iIIpOsTUdlfhZmwK9Odyz3ra1ZnCqlESO0s9x5FgvID9l7emdIJXvjMXYWJEIduCfH"
    api = sly.Api(address, token)
if serv == "Oddbot":
    address = "http://40.115.30.124/" #os.environ['SERVER_ADDRESS']
    token = "r0fZ3xO7Gro7d7pYh3L9oSJqJiwbFk9pCC85leqU9Uz7j3xRuD3P7HjJ5N84k7pLqsVP2xcAZHXqtlSBfbYuDW4xDXYsVKW92PjGwmipCz6IzUka1lj0VFnJJ2wKTF5M"
    api = sly.Api(address, token)
if serv == "kill":
    address = "https://kil-sup.westeurope.cloudapp.azure.com/" #os.environ['SERVER_ADDRESS']
    token = "dnutUuKJjsbPHUGa2tTetyghRlbjoTwvVcSsYua3fJkDW7jYquXgbRIGXKCVZU2NvuHn0ARJ0ojChiejO56NLOrUy0OzutrjxSNyDQqTuaAb4MdQAOZYdt5B3OCAmRgI"
    api = sly.Api(address, token)

if serv == "airnil":
    address = "https://data.aiir.nl/" #os.environ['SERVER_ADDRESS']
    token = "lU1DMJrLXpO1ic7GBYGxHzqyt3iuBCSJhXjCnsgmrclT7GxS9DFH7bHlhz4kK0WBoZT1Lezqy3ISwOgggju9KLscA7CAFc42drhuHbHACNxO36zjwDVMw0NVs0z6zQxF"
    api = sly.Api(address, token)

if serv == "sp":
    address = "https://sprvs.e80group.com/" #os.environ['SERVER_ADDRESS']
    token = "nEVSXO361XMN3dVdb9wWp1rF4r6Z3mlz5q65xhmspui87yn5JmMRFAdC3Eq1oXbmqe5bUtFLluBEpFcQoj3JgKrDgvuGHPCRNi3B4K6uxgj2zPGYX6D2s8u43najr35n"
    api = sly.Api(address, token)

api = sly.Api(address, token)


team = api.team.get_info_by_name(team_name)
if team is None:
    raise RuntimeError("Team {!r} not found".format(team_name))

workspace = api.workspace.get_info_by_name(team.id, workspace_name)
if workspace is None:
    raise RuntimeError("Workspace {!r} not found".format(workspace_name))

project = api.project.get_info_by_name(workspace.id, project_name)
if project is None:
    raise RuntimeError("Project {!r} not found".format(project_name))


print("Team: id={}, name={}".format(team.id, team.name))
print("Workspace: id={}, name={}".format(workspace.id, workspace.name))
print("Project id={}, name={}".format(project.id, project.name))
print("______________________________________")
print("")


meta_json = api.project.get_meta(project.id)
meta = sly.ProjectMeta.from_json(meta_json)
datasets = api.dataset.get_list(project.id)

dataset_list = list(map(int, input("Enter dataset values separated by commas: ").split(',')))
print("")
print("Total Datasets : ",len(dataset_list))


matched_count=0


print("_________________________")
print("")
print("Printing Dataset Name : Image Count")
for dataset in api.dataset.get_list(project.id):
    
    if dataset.id in dataset_list:
        matched_count+=1
        image_list = api.image.get_list(dataset.id)  
        image_count = len(image_list)  
        print(f"{dataset.name}:{image_count}")
        
        
print("")
print("")
print("Total Found",matched_count)


# In[ ]:




