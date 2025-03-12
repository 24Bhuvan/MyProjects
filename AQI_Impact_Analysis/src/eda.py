import pandas as pd

def perform_eda(data:pd.DataFrame):
    print("\n Starting EDA...")
    print("\n Summary Statistics:")
    print(data.describe())
    print("\n Data Info:")
    print(data.info())
    print("\n🧮 Unique Values in Categorical Columns:")
    print(data.select_dtypes(include=['object']).nunique())