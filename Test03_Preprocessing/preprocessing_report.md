# Data Preprocessing Report

This report documents the preprocessing steps applied to the dataset (Titanic dataset was used as an example) as per the Assignment requirements. The process ensures the data is cleaned, formatted correctly, and prepared for modeling, without performing any actual model training.

## 1. Understanding the Dataset
The initial step involved loading the dataset and inspecting its basic properties:
- **Shape**: The original dataset consisted of 891 rows and 12 columns.
- **Columns**: `PassengerId`, `Survived`, `Pclass`, `Name`, `Sex`, `Age`, `SibSp`, `Parch`, `Ticket`, `Fare`, `Cabin`, `Embarked`.
- **Target Variable**: `Survived` (0 = No, 1 = Yes).

## 2. Checking and Handling Missing Values
Missing values were identified across the dataset:
- **Age (177 missing)**: Handled by filling with the **median** value of the column since age distribution can be skewed. 
- **Cabin (687 missing)**: Contains >75% missing data. Addressed in Step 8 by dropping the column.
- **Embarked (2 missing)**: Handled by filling with the **mode** (most frequent value) since it's a categorical variable.

## 3. Removing Duplicate Records
The dataset was checked for exact row-level duplicates. Any exact duplicated rows were dropped to prevent data leakage and biases.

## 4. Detecting and Handling Outliers
Outliers were identified in continuous variables, specifically the `Fare` column, which has extreme values.
- **Method Used**: Interquartile Range (IQR).
- **Handling**: Outliers were capped (Winsorized) to the upper and lower bounds (`Q1 - 1.5 * IQR` and `Q3 + 1.5 * IQR`). This prevents extreme values from negatively impacting distance-based models.

## 5. Handling Incorrect Data Types
Variables were checked for appropriate typing:
- `Pclass` is represented as an integer (1, 2, 3), but it is essentially a categorical variable indicating socioeconomic status. It was explicitly converted to a **category** type to prevent models from interpreting it as a continuous sequence.

## 6. Handling Categorical Variables
Categorical variables (`Sex` and `Embarked`) need to be converted to a numeric format.
- **Method Used**: **One-Hot Encoding** (via `pd.get_dummies(..., drop_first=True)`).
- **Reasoning**: One-Hot Encoding is the recommended approach for nominal categories with no inherent order (such as Gender or Port of Embarkation). `drop_first=True` was used to avoid the dummy variable trap (multicollinearity).

## 7. Feature Scaling
Distance-based models (like KNN, SVM) are sensitive to feature scales.
- **Method Used**: **Standardization (`StandardScaler`)**.
- **Reasoning**: StandardScaler (subtracting the mean and dividing by standard deviation) is recommended for normally distributed data and distance-sensitive models. It was applied to continuous features (`Age` and `Fare`).

## 8. Removing Irrelevant or Redundant Features
Some columns do not provide predictive value or have too much missing data.
- **Dropped Features**: `PassengerId` (unique identifier), `Name` (unique identifier/text), `Ticket` (unique identifier), and `Cabin` (too many missing values).

## 9. Handling Skewness
Features with high skewness can violate the assumptions of linear models.
- **Method Used**: Log Transformation (`np.log1p`).
- **Reasoning**: The `Fare` feature is highly right-skewed. Applying a log transformation helps approximate a more normal distribution, reducing the impact of long-tailed distributions on models.

---

### Final Output
The dataset has been successfully processed according to these steps. 
- A python script (`preprocessing.py`) has been provided which executes all of these steps programmatically.
- The resulting cleaned dataset (`titanic_cleaned.csv`) is now ready for exploratory data analysis or machine learning model training.
