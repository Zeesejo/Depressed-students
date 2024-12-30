# Student Depression Analysis

This project aims to analyze and predict depression among students based on various factors such as academic pressure, work pressure, CGPA, study satisfaction, job satisfaction, sleep duration, dietary habits, and more.

## Project Overview

We have performed the following steps in this project:

1. **Data Loading and Inspection**
   - Loaded the dataset and inspected its structure, shape, and summary statistics.
   - Checked for missing values and handled them appropriately.

2. **Data Preprocessing**
   - Encoded categorical features such as Gender, City, and Profession using One-Hot Encoding.
   - Discretized the Age feature into meaningful age groups.

3. **Exploratory Data Analysis (EDA)**
   - Visualized the distribution of age groups and their relationship with depression status.
   - Created a correlation heatmap to understand the relationships between numerical features.

4. **Feature Engineering**
   - Created new features such as Stress Level by combining Academic Pressure and Work Pressure.
   - Identified important features using feature importance scores from the RandomForest model.

5. **Model Building and Evaluation**
   - Built a RandomForest model to predict depression status.
   - Evaluated the model using accuracy, classification report, and confusion matrix.
   - Performed cross-validation to ensure consistent model performance.
   - Conducted hyperparameter tuning using RandomizedSearchCV to optimize the model.

6. **Model Interpretation and Saving**
   - Visualized the feature importances to understand the impact of different features on the model's predictions.
   - Saved the trained model for future use.

## Results

- The RandomForest model achieved an accuracy of 0.82 on the test set.
- The most important features identified by the model include Academic Pressure, Work Pressure, CGPA, and Study Satisfaction.

## Next Steps

- Further optimize the model using more advanced techniques.
- Explore additional features and their impact on depression prediction.
- Deploy the model for real-time predictions.

## How to Run the Project

1. Clone the repository:
   ```sh
   git clone https://github.com/Zeesejo/Depressed-students/
