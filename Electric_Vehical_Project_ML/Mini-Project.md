# Electric Vehicle Population Data Analysis Project

## Project Overview
This project involves analyzing the Electric Vehicle Population Data to understand trends, patterns, and relationships between various features of electric vehicles. The goal is to build predictive models that can estimate the electric range of vehicles based on other attributes and determine which model performs best.

## Dataset
The dataset contains information about electric vehicles including:
- Vehicle identification details (VIN, DOL Vehicle ID)
- Location information (County, City, State, Postal Code)
- Vehicle specifications (Model Year, Make, Model)
- Electric vehicle characteristics (Electric Vehicle Type, Electric Range)
- Pricing information (Base MSRP)
- Regulatory information (Clean Alternative Fuel Vehicle Eligibility, Legislative District)
- Geographic data (Vehicle Location, Electric Utility, Census Tract)

## Project Tasks

### 1. Data Exploration and Preprocessing
- Load the Electric Vehicle Population Data CSV file
- Explore the dataset structure (shape, columns, data types)
- Generate descriptive statistics to understand the data distribution
- Identify and handle missing values in the dataset
- Perform necessary data cleaning operations

### 2. Exploratory Data Analysis (EDA)
- Analyze the distribution of electric vehicle types (BEV vs PHEV)
- Examine the relationship between model year and electric range
- Investigate price distribution across different vehicle makes and models
- Visualize geographic distribution of electric vehicles
- Identify trends in electric vehicle adoption over time

### 3. Feature Engineering
- Select relevant features for the prediction model
- Transform categorical variables if needed
- Create any additional features that might improve model performance

### 4. Model Selection and Evaluation
- Split the data into training and testing sets
- Implement and compare multiple regression models:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting Regressor
  - Support Vector Regression
  - K-Nearest Neighbors Regressor
- Evaluate each model using multiple metrics:
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
  - R-squared (R²)
  - Mean Absolute Error (MAE)
- Create a comparison table of all models with their performance metrics
- Identify the best performing model based on evaluation metrics

### 5. Hyperparameter Tuning
- Perform hyperparameter optimization for the top-performing models
- Use techniques like Grid Search or Random Search for tuning
- Implement cross-validation to ensure robust model selection
- Compare performance before and after hyperparameter tuning
- Select the final optimized model

### 6. Feature Importance Analysis
- Analyze feature importance for the best performing model
- Identify which features contribute most to predicting electric range
- Visualize feature importance rankings
- Consider feature selection based on importance analysis

### 7. Results Analysis and Visualization
- Visualize the model predictions against actual values
- Create residual plots to analyze model errors
- Generate learning curves to assess model performance with varying data sizes
- Develop visualizations to communicate findings effectively
- Document insights and patterns discovered during analysis

## Resources
- Original dataset: [Electric Vehicle Population Data](https://www.kaggle.com/datasets/ratikkakkar/electric-vehicle-population-data)

