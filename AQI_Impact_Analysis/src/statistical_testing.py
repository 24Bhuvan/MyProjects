from scipy import stats
import pandas as pd

def perform_statistical_tests(data_path='synthetic_data.csv'):
    data = pd.read_csv(data_path)
    high_aqi = data[data['AQI'] > 100]['Engagement Count']
    low_aqi = data[data['AQI'] <= 100]['Engagement Count']
    
    t_stat, p_val = stats.ttest_ind(high_aqi, low_aqi, equal_var=False)
    print(f"T-Statistic: {t_stat}, P-Value: {p_val}")