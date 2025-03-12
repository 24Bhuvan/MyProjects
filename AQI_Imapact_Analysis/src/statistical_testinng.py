import pandas as pd
import scipy.stats as stats

def perform_statistical_tests(data: pd.DataFrame):
    aqi_values = data['AQI']
    engagement_values = data['Engagement Count']
    
    shapiro_aqi = stats.shapiro(aqi_values)
    shapiro_engagement = stats.shapiro(engagement_values)
    
    print("Shapiro-Wilk Test for AQI:", shapiro_aqi)
    print("Shapiro-Wilk Test for Engagement:", shapiro_engagement)
    
    if shapiro_aqi.pvalue > 0.05 and shapiro_engagement.pvalue > 0.05:
        t_stat, p_value = stats.ttest_ind(aqi_values, engagement_values)
        print("T-Test Results:", t_stat, p_value)
    else:
        u_stat, p_value = stats.mannwhitneyu(aqi_values, engagement_values)
        print("Mann-Whitney U Test Results:", u_stat, p_value)