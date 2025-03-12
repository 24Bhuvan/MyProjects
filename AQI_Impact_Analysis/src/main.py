import pandas as pd
from data_generation import synthetic_data
from data_validation import cleaning_data
from eda import perform_eda
from statistical_testing import perform_statistical_tests
from data_visualization import visualize_data

def main():
    # Step 1: Generate or load data
    data = synthetic_data()

    # Step 2: Validate and clean data
    cleaned_data = cleaning_data(data)

    # Step 3: Perform Exploratory Data Analysis (EDA)
    perform_eda(cleaned_data)

    # Step 4: Visualize data for insights
    visualize_data(data)

    # Step 5: Conduct statistical tests
    perform_statistical_tests(cleaned_data)

if __name__ == "__main__":
    main()