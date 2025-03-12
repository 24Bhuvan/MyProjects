import pandas as pd

def cleaning_data(data: pd.DataFrame) -> pd.DataFrame:
    print("\n🧹 Checking for Missing Values:")
    print(data.isnull().sum())
    data = data.dropna()  
    print("\n🔍 Checking for Duplicates:")
    print(f'Duplicates found: {data.duplicated().sum()}')
    data = data.drop_duplicates()  
    print("\n📈 Handling Outliers in Numeric Data:")
    numeric_columns = ['AQI', 'Engagement Count', 'Car Commuter Count', 'Bike Commuter Count', 'Public Transport Commuter Count', 'Walk Commuter Count']
    for column in numeric_columns:
        q1 = data[column].quantile(0.25)
        q3 = data[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        data[column] = data[column].clip(lower=lower_bound, upper=upper_bound)

    print("\n✅ Data Validation and Cleaning Complete")
    return data