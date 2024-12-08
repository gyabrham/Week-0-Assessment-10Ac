import pandas as pd
import matplotlib.pyplot as plt

# Load solar radiation data (togo)
data = pd.read_csv(“togo-dapaong_qc.csv")

# Data cleaning and preprocessing (if necessary)
data.dropna(inplace=True)
data['2021-2022’] = pd.to_datetime(data['2021-2022’])

# Exploratory Data Analysis (EDA)
# 1. Time Series Analysis
plt.figure(figsize=(10, 6))
plt.plot(data['2021_2022’], data['GHI'])
plt.xlabel('2021_2022’)
plt.ylabel('Global Horizontal Irradiance (W/m²)')
plt.title('Time Series of Global Horizontal Irradiance')
plt.grid(True)
plt.show()

# 2. Regional Analysis
# Group data by region and calculate average solar radiation
regional_avg = data.groupby('Region')['GHI'].mean()
plt.bar(regional_avg.index, regional_avg.values)
plt.xlabel('Region')
plt.ylabel('Average GHI')
plt.title('Average GHI by Region')
plt.show()

# 3. Correlation Analysis
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title('Correlation Matrix')
plt.show()

# 4. Solar Potential Assessment
# Identify regions with high solar radiation and low cloud cover
high_potential_regions = data[data['GHI'] > threshold_ghi & data['Cloud Cover'] < threshold_cloud_cover]
print(high_potential_regions)