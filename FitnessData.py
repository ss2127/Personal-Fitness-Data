import pandas as pd

df = pd.read_csv('personal_fitness_data.csv')

# DATA CLEANING
# CLEANING EMPTY CELLS
# REMOVE ROWS THAT CONTAIN EMPTY CELLS.
# REPLACE EMPTY VALUES

x = df['Steps'].mean()
df['Steps'].fillna(x, inplace=True)


y = df['HeartRate'].mode()[0]
df['HeartRate'].fillna(y, inplace=True)

# CLEANING WRONG DATA
for w in df.index:
    if df.loc[w, 'HeartRate'] < 50:
        df.loc[w, 'HeartRate'] = df['HeartRate'].mode()[0]

# REMOVING DUPLICATES

df.drop_duplicates(inplace=True)
print(df.to_string())

df.to_csv('cleaned_updated_personal_fitness_data.csv', index=False)