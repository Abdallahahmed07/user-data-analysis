
#2_Analysis.py

import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt



print("############# Analysis Is Started ##########")


df = pd.read_csv('users.csv')


#--------------------------------   Cleaning/Preparation   --------------------------------


###################### maidenName column has 148 Null so it is better to drop it ######################
df.drop(columns='maidenName',inplace=True)

###################### Add new column "country" extracted from Address ######################

df['country']=df['address.country']

###################### Add new column "city" extracted from Address ######################

df['city']=df['address.city']


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
plt.savefig("plots/avg_age_by_role.png")
plt.close()


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
plt.savefig("plots/avg_age_by_gender.png")
plt.close()


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
plt.savefig("plots/users_per_gender.png")
plt.close()


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
plt.savefig("plots/top_cities.png")
plt.close()



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
plt.savefig("plots/height_distribution.png")
plt.close()


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
plt.savefig("plots/weight_distribution.png")
plt.close()



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
plt.savefig("plots/age_vs_height.png")
plt.close()



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
plt.savefig("plots/age_vs_weight.png")
plt.close()


print("############# Analysis DONE ! ##########")
print("############# plots are saved in plots folder #############")

