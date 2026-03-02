
# 📊 User Data ETL & Analytics Pipeline 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Requests](https://img.shields.io/badge/Requests-FF6633?style=for-the-badge&logo=python&logoColor=white)

A containerized Python project that automates the journey from raw API data to polished visual insights. This pipeline handles data extraction, cleaning, and statistical visualization using a "plug-and-play" Docker environment.


---
## 🏗️ Architecture & Workflow

The pipeline follows a classic **ETL (Extract, Transform, Load)** pattern, ensuring that data retrieval is decoupled from the analysis logic.

1.  **Extract (`1_Fetching_Data.py`):**
    * Connects to the **DummyJSON API**.
    * Implements **pagination logic** (using `limit` and `skip` parameters) to ensure all user records are captured regardless of API defaults.
    * Saves the raw response into a structured `users.csv`.

2.  **Transform & Analyze (`2_Analysis.py`):**
    * **Data Cleaning:** Handles missing values, drops redundant fields (like `maidenName`), and flattens nested JSON objects (like addresses) into flat columns.
    * **Data Normalization:** Ensures numerical consistency for height, weight, and age.
    * **Statistical Analysis:** Performs aggregations to find trends across demographics.

3.  **Visualize (Output):**
    * Generates **8 high-resolution plots** using Seaborn and Matplotlib.
    * Automatically exports results to the `/plots` directory as `.png` files.

---

## 📦 How to Run

Follow these steps to pull the image and run the analysis on your local machine using Docker.

### 1. Pull the Image
Download the latest version from Docker Hub:
```bash
docker pull abdallahahmed7/python_project:v1

```

### 2. Verify the Image

Ensure the image is loaded in your local environment:

```bash
docker images

```

### 3. Run the Container

Run the container with a **volume mount** to save the generated plots directly to your host machine:

```bash
docker run -itd --name project_container -v $(pwd)/plots:/app/plots abdallahahmed7/python_project:v1

```

> **💡 Pro Tip:** The `-v $(pwd)/plots:/app/plots` flag mounts your local "plots" folder to the container. Wait a few seconds after running, and you will see the `.png` files appear in your local directory!

---

## 📊 Generated Visualizations

The pipeline generates the following insights:

* **Average Age by Role** (Bar Chart)
* **Average Age by Gender** (Bar Chart)
* **User Count per Gender** (Count Plot)
* **Top 10 Cities with Most Users** (Bar Chart)
* **Height Distribution** (Histogram with KDE)
* **Weight Distribution** (Histogram with KDE)
* **Age vs. Height Correlation** (Scatter Plot)
* **Age vs. Weight Correlation** (Scatter Plot)

---

## 📂 Project Structure

```
.
├── 1_Fetching_Data.py   # Data Extraction Script
├── 2_Analysis.py        # Data Cleaning & Visualization Script
├── users.csv            # Generated Dataset (Output of Fetching)
├── Dockerfile           # Container Configuration
├── requirements.txt     # Python Dependencies
└── plots/               # Output directory for .png files
```


---
## 👨‍💻 Author

**Abdallah Ahmed**

*Python Developer | Data Enthusiast*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/abdallahahmed7)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/AbdallahAhmed7)




