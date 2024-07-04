import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('cleaned_updated_personal_fitness_data.csv')
# Line plot of daily steps over time

sns.set(style="darkgrid")

# sets window resolution. figure(figsize=(width, height))
plt.figure(figsize=(15, 6), facecolor="lightskyblue")
sns.lineplot(x='Date', y='Steps', data=df)
plt.title('Daily Steps Over Time')
plt.xlabel('Date')
plt.ylabel('Steps')
plt.xticks(rotation=45)
plt.show()

# Histogram of calories burned
plt.figure(figsize=(10, 6), facecolor="lightskyblue")
sns.histplot(df['CaloriesBurned'], bins=30, kde=True)
plt.title('Distribution of Calories Burned')
plt.xlabel('Calories Burned')
plt.ylabel('Frequency')
plt.show()

# Finds average steps by day of the week
df['Date'] = pd.to_datetime(df['Date'])
df['DayOfWeek'] = df['Date'].dt.day_name()
avg_steps_by_day = df.groupby('DayOfWeek')['Steps'].mean().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)

# Bar Plot that shows the average steps by day of the week
plt.figure(figsize=(10, 6), facecolor="lightskyblue")
sns.barplot(x=avg_steps_by_day.index, y=avg_steps_by_day.values)
plt.title('Average Steps by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Steps')
plt.show()
