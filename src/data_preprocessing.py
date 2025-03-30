# src/data_preprocessing.py
import pandas as pd
import os

# Function to load raw CSV data into DataFrame
def load_data(filepath):
    # Get the current working directory and join it with the relative path to the file
    current_dir = os.path.dirname(__file__) 
    full_path = os.path.join(current_dir, '..', 'data', filepath)

    # Check if the file is empty
    if os.stat(full_path).st_size == 0:
        print("Warning: The CSV is empty!")
        return pd.DataFrame() # Return an empty DataFrame or handle the error accordingly
    
    return pd.read_csv(full_path)

# Function to clean data
def clean_data(df):
    # Remove rows with missing 'production_date'
    df = df.dropna(subset=['production_date'])

    # Convert 'production_data' column to datetime type
    df['production_date'] = pd.to_datetime(df['production_date'], errors= 'coerce')

    # Drop any rows with invaild 'production_date' after conversion
    df = df.dropna(subset=['production_date'])

    # Covert 'production_date' column to datetime type'
    df = df.drop_duplicates()

    # Ensure volume is numeric
    df['volume_produced'] = pd.to_numeric(df['volume_produced'], errors='coerce')

    # Handle missing numeric values (e.g., fill with 0)
    df['volume_produced'].fillna(0, inplace=True)

    return df

# Example usage
if __name__ == "__main__":

    # Load and clean the data
    df_production = load_data('raw_production_data.csv')

    if not df_production.empty:
        df_cleaned = clean_data(df_production)
        print(df_cleaned.head())

    else:
        print("No data loaded.")