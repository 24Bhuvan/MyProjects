import numpy as np 
import pandas as pd

def synthetic_data():
    np.random.seed(42)
    data_range = pd.date_range(start = '2025-01-01', periods = 60*24, freq = 'h')
    aqi = np.random.normal(loc = 100, scale = 20, size = len(data_range))
    mode_data = {
        'Car': np.random.randint(20, 100, size=len(data_range)),
        'Bike': np.random.randint(5, 50, size=len(data_range)),
        'Walk': np.random.randint(10, 60, size=len(data_range)),
        'Public Transport': np.random.randint(50, 150, size=len(data_range))
    }
    engagement_counts = np.random.randint(0, 500, size=len(data_range))
    data = pd.DataFrame({
        'Date': data_range,
        'AQI': np.round(aqi, 2),
        'Car Commuter Count': mode_data['Bus'],
        'Bike Commuter Count': mode_data['Bike'],
        'Walk Commuter Count': mode_data['Walk'],
        'Public Transport Commuter Count': mode_data['Public Transport'],
        'Engagement Count': engagement_counts
    })
    return data