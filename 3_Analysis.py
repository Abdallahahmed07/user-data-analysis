import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv('users.csv')


#--------------------------------   Cleaning/Preparation   --------------------------------

###################### Show Number of missing values per column  ######################
print("Number of missing values per column : \n",df.isnull().sum())

###################### maidenName column has 148 Null so it is better to drop it ######################
df.drop(columns='maidenName',inplace=True)

###################### Add new column "country" extracted from Address ######################
def get_country(address_text):
        address_dictionary=json.loads(address_text.replace("'","\"")) #JSON requires double quotes
        return address_dictionary.get('country', 'Unknown')  #return "country" if exists otherwise return "Unknown"

df['country']=df['address'].apply(get_country) 


###################### Add new column "city" extracted from Address ######################
def get_city(address_text):
        address_dictionary=json.loads(address_text.replace("'","\"")) #JSON requires double quotes
        return address_dictionary.get('city', 'Unknown')  #return "city" if exists otherwise return "Unknown"

df['city']=df['address'].apply(get_city) 







#--------------------------------  Analysis   --------------------------------


#################### Average Age by role ######################
sns.set_style("whitegrid")
plt.figure(figsize=(5,6))
sns.barplot(data=df, 
            x='role', 
            y='age',
            hue='role',
            estimator='mean',
            palette='Set2',
            legend=False,
            errorbar=None
           
            )  

plt.title("Average Age by Role")
plt.xlabel("Role")
plt.ylabel("Average Age")
plt.tight_layout()
plt.show()


##################### Average Age by Gender ######################

sns.set_style("whitegrid")
plt.figure(figsize=(5,6))
sns.barplot(data=df, 
            x="gender", 
            y="age",
            hue='gender',
            estimator='mean',
            palette='Set2',
            legend=False,
            errorbar=None
           
            )  

plt.title("Average Age by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Age")
plt.tight_layout()
plt.show()


##################### Number of users per Gender ######################
sns.set_style("whitegrid")
plt.figure(figsize=(5,6))
sns.countplot(data=df, 
            x="gender", 
            hue='gender',
            palette='Set2',

            )  

plt.title("Number of users per Gender")
plt.xlabel("Gender")
plt.ylabel("Number Of Users")
plt.tight_layout()
plt.show()



##################### Top 10 cities with the most users ######################
users_per_city=df['city'].value_counts().sort_values(ascending=False).reset_index()
users_per_city.columns=['city','user_count']

sns.set_style("whitegrid")
plt.figure(figsize=(10,6))
sns.barplot(data=users_per_city.head(10), 
            x="city", 
            y="user_count",
            hue='city',
            palette='Set2',

            )  

plt.title("Top 10 cities with the most users")
plt.xlabel("City")
plt.ylabel("Number Of Users")
plt.tight_layout()
plt.show()




##################### Average height colored by role ######################

sns.set_style("whitegrid")
sns.histplot(data=df, 
             x="height", 
             hue='role',
             multiple='stack',
             kde=True)   


plt.title(f"Average height={df['height'].mean():.2f} cm")
plt.xlabel("Height (cm)")
plt.ylabel("Number of users")
plt.tight_layout()
plt.show()

##################### Average Weight colored by role ######################

sns.set_style("whitegrid")
sns.histplot(data=df, 
             x="weight", 
             hue='role',
             multiple='stack',
             kde=True)   

plt.title(f"Average Weight={df['weight'].mean():.2f} kg")
plt.xlabel("Weight (kg)")
plt.ylabel("Number of users")
plt.tight_layout()
plt.show()



##################### relationship between Age and height colored by gender ######################

sns.scatterplot(
        data=df, 
        x='age', 
        y='height', 
        hue='gender',
        )

plt.title("Relationship Between Age and Height")
plt.xlabel("Age")
plt.ylabel("Height (cm)")
plt.show()


##################### relationship between Age and weight colored by gender ######################

sns.scatterplot(
        data=df, 
        x='age', 
        y='weight', 
        hue='gender',
        )

plt.title("Relationship Between Age and Weight")
plt.xlabel("Age")
plt.ylabel("Weight (Kg)")
plt.show()


