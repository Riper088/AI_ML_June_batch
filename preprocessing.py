import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# --- Step 1: Understanding the dataset ---
print("--- Step 1: Understanding the Dataset ---")
# Load the Titanic dataset from a reliable source
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nTarget Variable: 'Survived' (0 = No, 1 = Yes)")

# --- Step 2: Checking and handling missing values ---
print("\n--- Step 2: Checking and Handling Missing Values ---")
print("Missing values before:\n", df.isnull().sum())

# 'Cabin' has too many missing values, we'll drop it later in Step 8. 
# Fill 'Age' with the median age.
df['Age'] = df['Age'].fillna(df['Age'].median())
# Fill 'Embarked' with the mode.
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

print("Missing values after:\n", df.isnull().sum())

# --- Step 3: Removing duplicate records ---
print("\n--- Step 3: Removing duplicate records ---")
duplicates_count = df.duplicated().sum()
print(f"Number of duplicate records found: {duplicates_count}")
df = df.drop_duplicates()
print("Shape after removing duplicates:", df.shape)

# --- Step 4: Detecting and handling outliers ---
print("\n--- Step 4: Detecting and handling outliers ---")
# Let's check 'Fare' for outliers using the IQR method.
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers_count = ((df['Fare'] < lower_bound) | (df['Fare'] > upper_bound)).sum()
print(f"Outliers detected in 'Fare': {outliers_count}")

# Cap the outliers (Winsorization) to the upper and lower bounds.
df['Fare'] = np.where(df['Fare'] > upper_bound, upper_bound, df['Fare'])
df['Fare'] = np.where(df['Fare'] < lower_bound, lower_bound, df['Fare'])

# --- Step 5: Handling incorrect data types ---
print("\n--- Step 5: Handling incorrect data types ---")
print("Data types before:\n", df.dtypes)
# 'Survived' and 'Pclass' can be converted to integer/category if needed, 
# 'Sex' and 'Embarked' should be categorical. We'll leave them as object for encoding,
# but let's ensure Pclass is correctly interpreted.
df['Pclass'] = df['Pclass'].astype('category')
print("Changed 'Pclass' to category.")

# --- Step 6: Handling categorical variables ---
print("\n--- Step 6: Handling categorical variables ---")
# One-Hot Encoding for nominal variables 'Sex' and 'Embarked'
# Recommendation: One-Hot Encoding - Best for nominal categories with no order
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
print("Applied One-Hot Encoding on 'Sex' and 'Embarked'.")
print("New columns:", df.columns.tolist())

# --- Step 8: Removing irrelevant or redundant features ---
# (Doing Step 8 before 7 & 9 makes scaling easier on the numeric columns left)
print("\n--- Step 8: Removing irrelevant or redundant features ---")
# 'PassengerId', 'Name', 'Ticket' are unique identifiers. 'Cabin' has 77% missing data.
drop_cols = ['PassengerId', 'Name', 'Ticket', 'Cabin']
df = df.drop(columns=drop_cols)
print(f"Dropped columns: {drop_cols}")
print("Remaining columns:", df.columns.tolist())

# --- Step 9: Handling skewness if present ---
print("\n--- Step 9: Handling skewness if present ---")
# 'Fare' is typically highly right-skewed.
print(f"Skewness of 'Fare' before transformation: {df['Fare'].skew():.2f}")
# Apply Log Transformation to reduce right skewness (add +1 to handle 0 values)
df['Fare'] = np.log1p(df['Fare'])
print(f"Skewness of 'Fare' after Log1p transformation: {df['Fare'].skew():.2f}")

# --- Step 7: Feature scaling ---
print("\n--- Step 7: Feature scaling ---")
# Recommended: StandardScaler for normally distributed/continuous data.
# We apply it to 'Age' and 'Fare' (continuous variables).
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
print("Applied StandardScaler to 'Age' and 'Fare'.")
print(df[['Age', 'Fare']].head())


# Save the final cleaned dataset
output_file = "titanic_cleaned.csv"
df.to_csv(output_file, index=False)
print(f"\nCleaned dataset saved successfully to {output_file}")
print("Final Dataset Shape:", df.shape)
