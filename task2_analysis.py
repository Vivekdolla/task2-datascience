# Required Libraries 
import seaborn as sns 
import pandas as pd 
import numpy as np 
from scipy import stats 
# Load the inbuilt dataset 
df = sns.load_dataset("tips") 
# 1. Preview and Info 
print(" First 5 rows:\n", df.head()) 
print("\n Dataset Info:") 
df.info() 
# 2. Descriptive Statistics using Pandas 
print("\n Summary Statistics:\n", df.describe()) 
# 3. Central Tendency - total_bill using NumPy 
print("\n Central Tendency (total_bill) using NumPy:") 
print("Mean:", np.mean(df['total_bill'])) 
print("Median:", np.median(df['total_bill'])) 
# Mode returns an array, we take the first mode 
print("Mode:", stats.mode(df['total_bill'], keepdims=False).mode) 
# 4. Central Tendency - total_bill using Pandas 
print("\n Central Tendency (total_bill) using Pandas:") 
print("Mean:", df['total_bill'].mean()) 
print("Median:", df['total_bill'].median()) 
print("Mode:", df['total_bill'].mode().values[0]) # take first mode value 
# 5. Categorical Counts 
print("\n Gender Distribution:\n", df['sex'].value_counts()) 
print("\n Day Distribution:\n", df['day'].value_counts()) 
# 6. Grouped Analysis (with observed=False to avoid warning) 
print("\n Average Tip by Gender:\n", df.groupby('sex', observed=False)['tip'].mean()) 
print("\n Average Total Bill by Day:\n", df.groupby('day', observed=False)['total_bill'].mean()) 
# 7. Correlation 
print("\n Correlation Matrix:\n", df.corr(numeric_only=True))