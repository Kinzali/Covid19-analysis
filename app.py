import pandas as pd

# Load COVID-19 data
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
covid_data = pd.read_csv(url)


# Remove unnecessary columns
covid_data.drop(['Lat', 'Long'], axis=1, inplace=True)

# Aggregate data at country level
covid_data_grouped = covid_data.groupby('Country/Region').sum().reset_index()


import matplotlib.pyplot as plt

# Plotting time series data for a specific country (e.g., US)
country = 'US'
cases = covid_data_grouped.loc[covid_data_grouped['Country/Region'] == country].iloc[:, 1:]
dates = pd.to_datetime(cases.columns)
plt.plot(dates, cases.values.flatten(), marker='o')
plt.title(f'COVID-19 Cases in {country}')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# Example: Calculate correlation matrix
correlation_matrix = covid_data_grouped.corr()

import seaborn as sns

# Example: Heatmap of correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
