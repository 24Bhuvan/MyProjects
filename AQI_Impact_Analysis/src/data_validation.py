import pandas as pd

def cleaning_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the given DataFrame by handling missing values, duplicates, and outliers.
    
    Args:
        data (pd.DataFrame): The input DataFrame containing AQI, commuter counts, and engagement data.
    
    Returns:
        pd.DataFrame: The cleaned DataFrame with no missing values, duplicates, and outliers handled.
    """
    
    # 🧹 Checking for Missing Values
    print("\n🧹 Checking for Missing Values:")
    print(data.isnull().sum())  # Display count of missing values per column
    
    # Drop rows with missing values
    data = data.dropna()

    # 🔍 Checking for Duplicates
    print("\n🔍 Checking for Duplicates:")
    print(f'Duplicates found: {data.duplicated().sum()}')  # Display duplicate count
    
    # Drop duplicate rows
    data = data.drop_duplicates()

    # 📈 Handling Outliers in Numeric Data using the IQR method
    print("\n📈 Handling Outliers in Numeric Data:")
    numeric_columns = [
        'AQI', 
        'Engagement Count', 
        'Car Commuter Count', 
        'Bike Commuter Count', 
        'Public Transport Commuter Count', 
        'Walk Commuter Count'
    ]
    
    for column in numeric_columns:
        q1 = data[column].quantile(0.25)  # First quartile
        q3 = data[column].quantile(0.75)  # Third quartile
        iqr = q3 - q1  # Interquartile range
        
        # Calculate lower and upper bounds for outlier detection
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        # Clip values to stay within the calculated bounds
        data[column] = data[column].clip(lower=lower_bound, upper=upper_bound)

    print("\n✅ Data Validation and Cleaning Complete")
    
    return data  # Return the cleaned DataFrame
