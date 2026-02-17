import pandas as pd
import json



df = pd.read_csv('users.csv')
 


##########################   Basic Data Exploration   ##########################

#Shape of the DataFrame (rows, columns)
print("Shape of DataFrame: ",df.shape)

# List of all column names
print("DataFrame Column Names: ",df.columns)


# Data types of each column 
print("Data types: \n",df.dtypes)

#Number of missing values per column 
print("Number of missing values per column : \n",df.isnull().sum())

# Number of duplicate rows 
print("Number of duplicate rows: ",df.duplicated().sum())


# Summary statistics for numeric columns
print("Summary statistics for numeric columns: \n",df.describe())


# Value counts for gender column 
print("Value counts for Gender: \n",df['gender'].value_counts())

# Value counts for bloodGroup column
print("Value counts for bloodGroup: \n",df['bloodGroup'].value_counts())

# Value counts for eyeColor column
print("Value counts for eyeColor: \n",df['eyeColor'].value_counts())

# Value counts for role column
print("Value counts for role: \n",df['role'].value_counts())


# Value counts for address.country column
#convert address column from text to dictionary then extract country from it
def get_country(address_text):
        address_dictionary=json.loads(address_text.replace("'","\"")) #JSON requires double quotes
        return address_dictionary.get('country', 'Unknown')  #return "country" if exists otherwise return "Unknown"

address_country=df['address'].apply(get_country) 
print(address_country.value_counts())
