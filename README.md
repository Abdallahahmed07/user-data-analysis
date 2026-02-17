# User Data Analysis Project

## Description
This project performs **exploratory data analysis (EDA)** on user data fetched from the **DummyJSON API**. It demonstrates the full workflow of **data fetching, cleaning, analysis, and visualization** using Python.

The dataset contains **208 users**, including information such as age, gender, height, weight, role, and address. The project explores demographic patterns, distributions, and relationships between numeric variables.

**Key features:**
- Data fetching from API in batches  
- Data cleaning and preparation (handling missing values, extracting country and city)  
- Summary statistics for numeric and categorical columns  
- Visual analysis with **Seaborn** and **Matplotlib**  

---

## Tools & Libraries
- Python 3.x  
- pandas  
- seaborn  
- matplotlib  
- requests  
- json  

---


## Visualizations

### 1. Average Age by Role
![avg_age_by_role](https://github.com/user-attachments/assets/c6996348-9334-430e-9005-50c739ed5d1f)


### 2. Average Age by Gender
![avg_age](https://github.com/user-attachments/assets/55c1e531-3134-471f-aa9f-6f0ec8092881)


### 3. Number of Users per Gender
![users_per_gender](https://github.com/user-attachments/assets/e4c77143-2479-4983-857d-19de35f2d061)


### 4. Top 10 Cities with the Most Users
![top_10_cities](https://github.com/user-attachments/assets/07d6880a-abc2-4491-9615-f22dd35055f5)


### 5. Height Distribution by Role
![Avg_height](https://github.com/user-attachments/assets/9690be13-5fef-4d3d-a7a2-c98a0fbc09a7)


### 6. Weight Distribution by Role
![avg_weight](https://github.com/user-attachments/assets/66d9399d-d3f2-4423-9875-7808f0bf7bf1)


### 7. Relationship Between Age and Height
![AGE_HEIGHT](https://github.com/user-attachments/assets/ddb66027-ff93-4fcd-8842-4171aafa3373)


### 8. Relationship Between Age and Weight
![AGE_WEIGHT](https://github.com/user-attachments/assets/22cb9690-cd05-4875-9dd2-dca20cc2f276)


---

## How to Run
1. Install required packages.
2. Fetch user data:
   - python 1_Fetching_Data.py
4. Perform exploratory analysis:
   - python 2_EDA.py
6. Generate visualizations:
   - python 3_Analysis.py






