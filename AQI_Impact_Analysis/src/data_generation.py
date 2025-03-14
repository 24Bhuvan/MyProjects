import numpy as np
import pandas as pd

def synthetic_data():
    """
    Generates synthetic data for AQI, commuter counts, and engagement over a 60-day period 
    with hourly frequency.
    
    Returns:
        pd.DataFrame: A DataFrame containing date, AQI, commuter counts by mode, and engagement count.
    """
    np.random.seed(42)  # Ensuring reproducibility
    
    # Create a date range for 60 days with hourly intervals
    data_range = pd.date_range(start='2025-01-01', periods=60 * 24, freq='h')
    
    # Generate synthetic AQI values using a normal distribution
    aqi = np.random.normal(loc=100, scale=20, size=len(data_range))
    
    # Generate random commuter counts for different transport modes
    mode_data = {
        'Car': np.random.randint(20, 100, size=len(data_range)),  # Car commuters
        'Bike': np.random.randint(5, 50, size=len(data_range)),   # Bike commuters
        'Walk': np.random.randint(10, 60, size=len(data_range)),  # Walking commuters
        'Public Transport': np.random.randint(50, 150, size=len(data_range))  # Public transport users
    }
    
    # Generate random engagement counts
    engagement_counts = np.random.randint(0, 500, size=len(data_range))
    
    # Create a DataFrame to store the generated data
    data = pd.DataFrame({
        'Date': data_range,
        'AQI': np.round(aqi, 2),  # Round AQI values for clarity
        'Car Commuter Count': mode_data['Car'],
        'Bike Commuter Count': mode_data['Bike'],
        'Walk Commuter Count': mode_data['Walk'],
        'Public Transport Commuter Count': mode_data['Public Transport'],
        'Engagement Count': engagement_counts
    })
    
    return data  # Return the structured DataFrame
