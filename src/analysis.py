# src/analysis.py
import pandas as pd
from data_preprocessing import load_data  # Import load_data function from data_preprocessing

# Function to calculate total production
def calculate_total_production(df):
    total_production = df['volume_produced'].sum()
    return total_production

# Function to calculate total production by region
def production_by_region(df):
    return df.groupby('region')['volume_produced'].sum()

# Function to calculate total production by well
def production_by_well(df):
    return df.groupby('well_id')['volume_produced'].sum()

# Example usage
if __name__ == "__main__":
    # Example: Load your cleaned data (you could import it from your preprocessing script)
    df_cleaned = load_data('raw_production_data.csv')

    if df_cleaned.empty:
        print("No data loaded!")
    
    else:

        # Calculate total production
        total_prod = calculate_total_production(df_cleaned)
        print(f"Total Production: {total_prod}")

        # Production by region
        region_prod = production_by_region(df_cleaned)
        print("Production by Region:")
        print(region_prod)

        # Production by well
        well_prod = production_by_well(df_cleaned)
        print("Production by Well:")
        print(well_prod)