import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the data (Assume 'data' is the DataFrame)
from data_validation import cleaning_data
from data_generation import synthetic_data

data = synthetic_data()
data = cleaning_data(data)

def perform_eda(data:pd.DataFrame):
    print("\n Starting EDA...")
    print("\n Summary Statistics:")
    print(data.describe())
    print("\n Data Info:")
    print(data.info())
    print("\n🧮 Unique Values in Categorical Columns:")
    print(data.select_dtypes(include=['object']).nunique())

    plt.figure(figsize=(8, 6))
    sns.histplot(data['AQI'], kde=True, color='skyblue')
    plt.title('Distribution of Air Quality Index (AQI)')
    plt.xlabel('AQI')
    plt.ylabel('Frequency')
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.histplot(data['Engagement Count'], kde=True, color='green')
    plt.title('Distribution of Public Engagement Count')
    plt.xlabel('Engagement Count')
    plt.ylabel('Frequency')
    plt.show()

    plt.figure(figsize=(10, 8))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['AQI'], label='AQI', color='blue')
    plt.plot(data.index, data['Engagement Count'], label='Engagement Count', color='red')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.title('AQI vs. Public Engagement Over Time')
    plt.legend()
    plt.show()
    
perform_eda(data)