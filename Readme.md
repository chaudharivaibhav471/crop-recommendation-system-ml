# 🌱 Crop Recommendation System using Soil and Weather Data

## 📌 Project Overview

The **Crop Recommendation System** is a machine learning–based web application that recommends the most suitable crop to grow based on soil nutrients and environmental conditions.

The system takes inputs such as:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* Soil pH
* Rainfall

Based on these parameters, the trained **Machine Learning model predicts the most suitable crop** for cultivation.

This project demonstrates how **Machine Learning can assist agriculture and help farmers make better decisions**.

---

# 🎯 Objectives

* Recommend the best crop based on soil and weather conditions
* Help farmers make informed agricultural decisions
* Demonstrate the use of **Machine Learning in Agriculture**
* Build a simple **web-based prediction system**

---

# 📊 Dataset

Dataset used: **Crop Recommendation Dataset**

The dataset contains soil nutrients and weather conditions mapped to the most suitable crop.

Example structure:

| Nitrogen | Phosphorus | Potassium | Temperature | Humidity | pH  | Rainfall | Crop |
| -------- | ---------- | --------- | ----------- | -------- | --- | -------- | ---- |
| 90       | 42         | 43        | 20.8        | 82       | 6.5 | 202      | Rice |

---

# 🔎 Exploratory Data Analysis (EDA)

Before building the machine learning model, **Exploratory Data Analysis (EDA)** was performed to understand the dataset and extract useful insights.

## Steps Performed in EDA

### 1. Data Loading

The dataset was loaded using **Pandas** and inspected.

### 2. Data Inspection

* Checked dataset shape
* Checked column names
* Verified data types
* Checked for missing values

### 3. Statistical Summary

Descriptive statistics were generated to understand feature distributions.

### 4. Data Visualization

Several visualizations were used to analyze the data:

* Distribution plots
* Box plots
* Correlation heatmap
* Feature relationships with crop labels

### 5. Feature Analysis

Analyzed how the following features influence crop prediction:

* Nitrogen
* Phosphorus
* Potassium
* Temperature
* Humidity
* Soil pH
* Rainfall

### 6. Correlation Analysis

A **correlation matrix** was generated to study relationships between variables.

### Libraries used for EDA

* Pandas
* NumPy
* Matplotlib
* Seaborn

EDA helped understand the dataset better and prepare it for model training.

---

# 🧠 Machine Learning Model

The machine learning model was trained using **Scikit-learn**.

## Algorithm Used

Random Forest Classifier

### Why Random Forest?

* Handles nonlinear relationships well
* Reduces overfitting
* Provides good accuracy for classification problems

---

# ⚙️ Model Training Process

The model training followed these steps:

1. Load dataset
2. Perform Exploratory Data Analysis (EDA)
3. Separate features and target variable
4. Encode crop labels using **LabelEncoder**
5. Split dataset into **training and testing sets**
6. Train model using **Random Forest Classifier**
7. Evaluate model accuracy
8. Save trained model using **Joblib**

Saved files:

```
crop_prediction_model.pkl
label_encoder.pkl
```

---

# 🌐 Web Application

A **Flask web application** was developed to allow users to interact with the machine learning model.

Users can enter:

* Soil nutrient levels
* Weather conditions

The application then predicts the **most suitable crop**.

---

# 🛠 Technologies Used

## Programming Language

Python

## Machine Learning Libraries

* Scikit-learn
* Pandas
* NumPy
* Joblib

## Data Visualization

* Matplotlib
* Seaborn

## Web Technologies

* Flask
* HTML
* CSS
* JavaScript

## Development Tools

* VS Code
* Python 3.x

---

# 📁 Project Structure

```
crop_recommendation_project/

│
├── app.py
├── requirements.txt
├── crop_prediction_model.pkl
├── label_encoder.pkl
├── Crop_recommendation.csv
├── crop_project.ipynb
│
├── templates/
│     └── index.html
│
├── static/
│     ├── css/
│     │     └── style.css
│     │
│     └── images/
│           ├── farm.jpg
│           └── logo.png
│
└── README.md
```

---

# ⚙️ Installation and Setup

## Step 1 — Install Python

Install **Python 3.8 or above**

Check installation:

```
python --version
```

---

## Step 2 — Download or Clone the Project

Download the project folder or clone from GitHub.

---

## Step 3 — Open Project in VS Code

Open the project folder in **Visual Studio Code**.

---

## Step 4 — Open Terminal in VS Code

Press:

```
Ctrl + `
```

---

## Step 5 — Install Required Libraries

Run:

```
pip install -r requirements.txt
```

This installs all necessary dependencies.

---

## Step 6 — Run the Application

Run:

```
python app.py
```

---

## Step 7 — Open in Browser

Open:

```
http://127.0.0.1:5000
```

---

# 🖥 Application Workflow

```
Dataset
   ↓
Exploratory Data Analysis (EDA)
   ↓
Data Preprocessing
   ↓
Model Training
   ↓
Model Saving (.pkl files)
   ↓
Flask Web Application
   ↓
User Input
   ↓
Crop Prediction
```

---

# 🌾 Example Prediction

Input:

```
Nitrogen: 90
Phosphorus: 42
Potassium: 43
Temperature: 20
Humidity: 80
pH: 6.5
Rainfall: 200
```

Output:

```
Recommended Crop: Rice
```

---

# 🚀 Future Enhancements

* Display crop images after prediction
* Integrate real-time weather API
* Mobile application for farmers
* Fertilizer recommendation system
* Online deployment of the application

---

# 👨‍💻 Author

**Vaibhav Chaudhari**
**Email:- chaudharivaibhav471@gmail.com**
**GitHub :- https://github.com/chaudharivaibhav471?tab=projects**
