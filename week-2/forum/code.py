import pandas as pd
import matplotlib.pyplot as plt

# Load data
url = "https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/avengers/avengers.csv"
data = pd.read_csv(url, encoding='latin 1')

# Filter valid entries
data = data[data['Year'] > 0]  # Remove rows without a year

# Group by YEAR and SEX, count entries
gender_year_count = data.groupby(['Year', 'Gender']).size().unstack().fillna(0)

# Plot
gender_year_count.plot(kind='bar', stacked=False, figsize=(12, 6))
plt.title("Number of Avengers Appearances per Year by Gender")
plt.xlabel("Year")
plt.ylabel("Number of Appearances")
plt.legend(title="Gender")
plt.tight_layout()
plt.show()
