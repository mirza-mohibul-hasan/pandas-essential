# Step-01
# Import Pandas
import pandas as pd

""" 1.Create """
# 1.1 Create from CSV
df = pd.read_csv("telco.csv")

# 1.2 Create from dictonary
tempdict = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
dictdf = pd.DataFrame.from_dict(tempdict)

""" 2.Read """
# 2.1.0 Show top 5 rows
top5 = df.head()  # by default it's top 10
# print(top5)

# 2.1.1 Show top 10 rows
top10 = df.head(10)
# print(top10)

# 2.1.1 Show top 5 of dictonaries
top5dictdf = dictdf.head()
# print(top5dictdf)

# 2.1.2 Show bottom 5 rows
bottom5 = df.tail()
# print(bottom5)

# 2.2.3 Show bottom 5 of dictonaries
bottom5dictdf = dictdf.tail()
# print(bottom5dictdf)

# 2.2.1 Show column
col = df.columns
# print(col)

# 2.2.2 Show data types
data_types = df.dtypes
# print(data_types)

# 2.3.0 Summary Statistics for numbers
num_stat = df.describe()
# print(num_stat)

# 2.3.1 Summary Statistics for objects
obj_stat = df.describe(include='object')
# print(obj_stat)

# 2.4.1 Filtering Colum
state = df.State  # State is a column name in data file
# print(state)

# 2.4.2 Filtering Colum if column name had space
int_plan = df["International plan"]
# print(int_plan)

# 2.4.3 Filtering multiple column
state_int_plan = df[["State", "International plan"]]
# print(state_int_plan)

# 2.4.4 Filtering column unique value named Churn
churn_unique = df.Churn.unique()
# print(churn_unique)

# 2.5.1 Filtering rows
int_plan_no = df[df['International plan'] == 'No']
# print(int_plan_no)

# 2.5.2 Filtering rows with multiple condition
int_plan_no_churn_true = df[(
    df['International plan'] == 'No') & (df['Churn'] == True)]
# print(int_plan_no_churn_true)

# 2.6 Indexing with iloc -> it use integers
# 2.6.1 data from a single index with row
single_index_row = df.iloc[14]
# print(single_index_row)

# 2.6.2 data from a single index row and col
# first one is row number and second one is col number
single_index_data = df.iloc[14, -1]
# print(single_index_data)

# 2.6.3 data from a row range
index_range_data = df.iloc[14:18]
# print(index_range_data)

# 2.7 Indexing with loc -> it use kewyword
# Step-01 Create a copy
state = df.copy()
# step-02 set as index-> here we using state as index
state.set_index('State', inplace=True)

# 2.7.1 data from state row where index is 'OH
index_data_loc = state.loc['OH']
print(index_data_loc)

""" 3. Update """
# 3.1 Droppping Rows
# print(df.isnull().sum())  # Number of rows that has missing values
df.dropna(inplace=True)  # Drop all rows that has missing values
# print(df.isnull().sum())

# 3.2 Droppping Column
df.drop('Area code', axis=1)
# print(df.head())

# 3.3 Creating Calculated Columns
df['New Column'] = df['Total night minutes'] + df['Total intl minutes']
# print(df.head())

# 3.4 Updating an Entire Column
df['New Column'] = 100
# print(df.head())

# 3.5 Updating a Single Value
df.iloc[0, -1] = 10
# print(df.head())

""" 4. Delete/Output """
# 4.1 Output to CSV
df.to_csv('output.csv')

# 4.2 Output to JSON
telco_json = df.to_json()
# print(telco_json)

# 4.3 Delet Dataframe
del df
# print(df.head())
