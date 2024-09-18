
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_excel(r'C:/Users/Mahantesh Patil/Downloads/Medical Inventory Optimaization Dataset/Medical Inventory Optimaization Dataset.xlsx')

df = pd.DataFrame(data)

# Display the first few rows of the dataset
print(df.head())

# Information about the dataset
print(df.info())

# Changing DataType of Patient_ID
df.Patient_ID = df.Patient_ID.astype('object')

# Standardizing the 'Dateofbill' column
df['Dateofbill'] = pd.to_datetime(df['Dateofbill'], errors='coerce').dt.date    
 
# Checking and Removing duplicates
dup=df.duplicated()
print(np.sum(dup))
df=df.drop_duplicates()

# Checking for missing values
missing_values = df.isnull().sum()
print(missing_values)

# Filling missing values by Mode for Formulation,drugName,SubCat,SubCat1
# Only these column have missing values and these are categorical type
df['Formulation']=df['Formulation'].fillna(df['Formulation'].mode()[0], inplace = False)
df['DrugName']=df['DrugName'].fillna(df['DrugName'].mode()[0], inplace = False)
df['SubCat']=df['SubCat'].fillna(df['SubCat'].mode()[0], inplace = False)
df['SubCat1']=df['SubCat1'].fillna(df['SubCat1'].mode()[0], inplace = False)

# Again Checking for missing values
missing_values = df.isnull().sum()
print(missing_values)

# Basic statistics
print(df.describe())

# Before Checking Outliers for Final Cost
# Density Plot 
plt.figure(figsize=(40, 5))
sns.kdeplot(df['Final_Cost'], fill=True)
plt.title('Density Plot')
plt.show()

# Boxplot
plt.figure(figsize=(10, 5))
sns.boxplot(df.Final_Cost)
plt.title('Boxplots of Numerical Columns')
plt.show()

# Before Checking Values of Skewness and Kurtosis of Final_Cost 
df['Final_Cost'].skew()
df['Final_Cost'].kurt()

# Handling outliers in Final_Sales using IQR method
Q1 = df['Final_Cost'].quantile(0.25)
Q3 = df['Final_Cost'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identifying outliers
outliers = df[(df['Final_Cost'] < lower_bound) | (df['Final_Cost'] > upper_bound)]
print(f"\nNumber of outliers: {outliers.shape[0]}")

# Handling outliers by capping them to the lower and upper bounds
df['Final_Cost'] = np.where(df['Final_Cost'] > upper_bound, upper_bound,
                             np.where(df['Final_Cost'] < lower_bound, lower_bound, df['Final_Cost']))

# Verifying the result of Final Cost
# boxplot
plt.figure(figsize=(10, 5))
sns.boxplot(df.Final_Cost)
plt.title('Boxplots of Numerical Columns')
plt.show()

# After Checking Values of Skewness and Kurtosis of Final Cost
df['Final_Cost'].skew()
df['Final_Cost'].kurt()

######################################################################

# Before Checking Outliers for Final Sales
# Density Plot
plt.figure(figsize=(40, 5))
sns.kdeplot(df['Final_Sales'], fill=True)
plt.title('Density Plot')
plt.show()

# Boxplot
plt.figure(figsize=(10, 5))
sns.boxplot(df.Final_Sales)
plt.title('Boxplots of Numerical Columns')
plt.show()

# Before Checking Values of Skewness and Kurtosis of Final_Sales
df['Final_Sales'].skew()
df['Final_Sales'].kurt()

# Handling outliers in Final_Sales using IQR method
Q1 = df['Final_Sales'].quantile(0.25)
Q3 = df['Final_Sales'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identifying outliers
outliers = df[(df['Final_Sales'] < lower_bound) | (df['Final_Sales'] > upper_bound)]
print(f"\nNumber of outliers: {outliers.shape[0]}")

# Handling outliers by capping them to the lower and upper bounds
df['Final_Sales'] = np.where(df['Final_Sales'] > upper_bound, upper_bound,
                             np.where(df['Final_Sales'] < lower_bound, lower_bound, df['Final_Sales']))

# Verifying the result of Final Sales
plt.figure(figsize=(10, 5))
sns.boxplot(df['Final_Sales'])
plt.title('Boxplot for Final Sales after Handling Outliers')
plt.show()

# Again Checking Values of Skewness and Kurtosis of Final Sales
df['Final_Sales'].skew()
df['Final_Sales'].kurt()

####################

