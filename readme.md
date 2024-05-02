# Pandas DataFrame Operations

## Introduction

This repository contains Python code snippets demonstrating various operations and functionalities of Pandas DataFrame, a powerful tool for data manipulation and analysis in Python.

## Contents

- **01**: Creating DataFrames
- **02**: Reading Data from DataFrames
- **03**: Updating DataFrames
- **04**: Deleting DataFrames and Outputting Data

## Detailed Explanation

### 01: Creating DataFrames

```python
# First need to import Pandas
import pandas as pd

# 1. Create DataFrames

# 1.1 Create DataFrame from CSV
df = pd.read_csv("telco.csv")

# 1.2 Create DataFrame from dictionary
tempdict = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
dictdf = pd.DataFrame.from_dict(tempdict)
```

### 02: Reading Data from DataFrames

```python
# 2.1.0 Show top 5 rows (default)

top5 = df.head()

# 2.1.1 Show top 10 rows

top10 = df.head(10)

# 2.1.2 Show top 5 rows of dictionary DataFrame

top5dictdf = dictdf.head()

# 2.1.3 Show bottom 5 rows

bottom5 = df.tail()

# 2.2.3 Show bottom 5 rows of dictionary DataFrame

bottom5dictdf = dictdf.tail()

# 2.2.1 Show column names

col = df.columns

# 2.2.2 Show data types of columns

data_types = df.dtypes

# 2.3.0 Summary Statistics for numerical columns

num_stat = df.describe()

# 2.3.1 Summary Statistics for object columns

obj_stat = df.describe(include='object')

# 2.4.1 Filtering Column 'State'

state = df.State

# 2.4.2 Filtering Column 'International plan' (if column name had space)

int_plan = df["International plan"]

# 2.4.3 Filtering multiple columns

state_int_plan = df[["State", "International plan"]]

# 2.4.4 Unique values of column 'Churn'

churn_unique = df.Churn.unique()

# 2.5.1 Filtering rows with 'International plan' == 'No'

int_plan_no = df[df['International plan'] == 'No']

# 2.5.2 Filtering rows with multiple conditions

int_plan_no_churn_true = df[(df['International plan'] == 'No') & (df['Churn'] == True)]

# 2.6 Indexing with iloc -> integer-based indexing

# 2.6.1 Data from a single index (row)

single_index_row = df.iloc[14]

# 2.6.2 Data from a single index (row and column)

single_index_data = df.iloc[14, -1]

# 2.6.3 Data from a range of rows

index_range_data = df.iloc[14:18]

# 2.7 Indexing with loc -> label-based indexing

# 2.7.1 Data from 'State' row where index is 'OH'

state = df.copy()
state.set_index('State', inplace=True)
index_data_loc = state.loc['OH']
```

### 3. Update DataFrames

```python
# 3.1 Dropping rows with missing values
df.dropna(inplace=True)

# 3.2 Dropping column 'Area code'
df.drop('Area code', axis=1, inplace=True)

# 3.3 Creating Calculated Columns
df['New Column'] = df['Total night minutes'] + df['Total intl minutes']

# 3.4 Updating an Entire Column with constant value
df['New Column'] = 100

# 3.5 Updating a Single Value
df.iloc[0, -1] = 10
```

# 4. Delete/Output DataFrames

```python
# 4.1 Output to CSV
df.to_csv('output.csv')

# 4.2 Output to JSON
telco_json = df.to_json()

# 4.3 Delete DataFrame
del df
```
