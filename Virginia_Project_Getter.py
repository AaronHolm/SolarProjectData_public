
# coding: utf-8

# In[81]:

import pandas as pd
import xml.etree.ElementTree as ET


# In[82]:

def getVirginia():
    # Need to grab dynamically from: 
    # https://www.google.com/maps/d/viewer?mid=1XZyl-JGFb2B9uAbuXCXfxUrb31k&ll=37.29314557358099%2C-76.97942632812493&z=8
    filePath = r'C:/Users/AHolm/SEIA/OneDrive - SEIA/codebin/datasources/States/VA/Renewable Energy Projects.kml'
    
    tree = ET.parse(filePath)
    root = tree.getroot()
    pmarks = tree.findall('.//{http://www.opengis.net/kml/2.2}Placemark')
    d = []
    for attributes in pmarks:
        for subAttribute in attributes:
            if(subAttribute.tag == '{http://www.opengis.net/kml/2.2}name'):
                name = subAttribute.text
            elif(subAttribute.tag == '{http://www.opengis.net/kml/2.2}ExtendedData'):
                proj_type = subAttribute[0][0].text
                cityCounty = subAttribute[1][0].text
                location = subAttribute[2][0].text
                latitude = subAttribute[3][0].text
                longitude = subAttribute[4][0].text
                capacity = subAttribute[5][0].text
                status = subAttribute[6][0].text
            else:
                pass
        d.append([name, proj_type, cityCounty, location, latitude, longitude, capacity, status])

    columns = ['Name', 'Type', 'City_County', 'Location_Description', 'Lat', 'Lon', 'Capacity (kW)', 'Status']
    va_projects = pd.DataFrame(data=d, columns=columns)
    return va_projects


# In[84]:

va_projs = getVirginia()
va_projs.head()


# In[ ]:



