import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  


def visualize_data(data:pd.DataFrame):
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