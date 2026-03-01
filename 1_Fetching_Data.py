#1_Fetching_Data.py

import pandas as pd
import requests



limit = 30
skip = 0
users_list = []


print("############# Fetching Is Started ##########")

#1.Loading the data from the API Using requests to fetch data
while True:

    url = f'https://dummyjson.com/users?limit={limit}&skip={skip}'
    response = requests.get(url)
    users=response.json()['users']
    
    if not users:
        break

    users_list.extend(users)
    skip+=limit


#Convert the users list to dataframe
df=pd.json_normalize(users_list)

print("############# Fetching DONE ! ##########")

#save the dataframe into users.csv    
df.to_csv('users.csv', index=False)

print("############# Data is saved in users.csv ##########")




    
