
# coding: utf-8

# In[2]:

import pandas as pd
import io
import requests


# In[3]:

def getMassachusetts():
    url1 = 'http://www.mass.gov/eea/docs/doer/rps-aps/solar-carve-out-units.xlsx'
    r1 = requests.get(url1)
    f1 = io.BytesIO(r1.content)
    solarcarveout1 = pd.read_excel(f1, skiprows=6, parse_cols="B:Q")
    solarcarveout1.columns = ['State_ID_1', 'State_ID_2', 'Aggregated?', 'Applicant Entity', 'Name', 'Facility_Type', 'City', 'Zip', 'Capacity (kW)', 'RPS Date', 'Operation Date', 'SQ Date', 'Utility', 'Installer_Developer', 'Install_Cost', 'Cost_per_watt']
    solarcarveout1['Solar Carveout'] = 'I'
    
    url2 = 'http://www.mass.gov/eea/docs/doer/rps-aps/solar-carve-out-ii-qualified-units.xlsx'
    r2 = requests.get(url2)
    f2 = io.BytesIO(r2.content)
    solarcarveout2 = pd.read_excel(f2, skiprows=11, parse_cols="B:Q")
    solarcarveout2.columns = ['State_ID_1', 'MA_Application_ID', 'State_ID_2', 'Applicant Entity', 'Name', 'Facility_Type', 'City', 'Zip', 'Capacity (kW)', 'Market Sector', 'Market Subsector', 'SREC Factor', 'RPS Date', 'Operation Date', 'SQ Date', 'Utility']
    solarcarveout2['Solar Carveout'] = 'II'
    
    frames = [solarcarveout1, solarcarveout2]
    massachusetts = pd.concat(frames)
    
    
    #massachusetts = solarcarveout2
    return massachusetts
    


# In[ ]:

mass_projs = getMassachusetts()
mass_projs.head()
mass_projs.to_excel("C:/Users/AHolm/SEIA/OneDrive - SEIA/codebin/datasources/NREL/MA_proj_getter.xlsx")


# In[ ]:



