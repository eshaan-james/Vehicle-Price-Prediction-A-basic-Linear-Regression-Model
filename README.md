# Simple Linear Regression Project - Vehicle Price Prediction

## Overview

This project demonstrates the use of **Simple Linear Regression** to predict the selling price of a vehicle based on various features using **Streamlit** for a user-friendly web-based interface. The dataset includes vehicle attributes such as present price, kilometers driven, fuel type, seller type, transmission type, ownership details, and age.

## Features

- **Dataset Used:** Vehicle price dataset with the following attributes:
  - **Selling_Price**: Selling price of the vehicle (target variable).
  - **Present_Price**: Current market price of the vehicle.
  - **Kms_Driven**: Total distance the vehicle has traveled.
  - **Fuel_Type**: Type of fuel (e.g., Petrol, Diesel, CNG).
  - **Seller_Type**: Type of seller (Individual or Dealer).
  - **Transmission**: Type of transmission (Manual or Automatic).
  - **Owner**: Number of previous owners.
  - **Age**: Age of the vehicle in years.

- **Objective:** Build a model to predict the selling price of vehicles based on the input features.

- **Technologies Used:**
  - **Streamlit**: For creating an interactive and user-friendly interface.
  - **Python Libraries**: 
    - `pandas` and `numpy` for data preprocessing and manipulation.
    - `scikit-learn` for model building and evaluation.
    - `matplotlib` and `seaborn` for data visualization.

## How It Works

1. **Data Preprocessing**:
   - Cleaned and processed the dataset by handling missing values and encoding categorical features.
   - Engineered the **Age** feature based on the year of manufacture.

2. **Exploratory Data Analysis (EDA)**:
   - Visualized relationships between features and the target variable (selling price).
   - Analyzed distributions and correlations among features.

3. **Model Building**:
   - Implemented a **Simple Linear Regression** model using `scikit-learn`.
   - Trained the model on the dataset to predict the selling price.

4. **Streamlit Application**:
   - Created a simple interface to accept user inputs for the vehicle attributes.
   - Displayed the predicted selling price based on the input values.
