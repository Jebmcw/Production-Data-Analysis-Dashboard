# src/visualization.py
import matplotlib.pyplot as plt
from analysis import production_by_region, production_by_well  # Import analysis functions
from data_preprocessing import load_data  # Import the load_data function from data_preprocessing.py

# Function to plot production by region
def plot_production_by_region(region_prod):
    # Create a bar plot for production by region
    region_prod.plot(kind='bar', color='skyblue')  # Fixed typo in color

    # Customize plot appearance
    plt.title('Total Production by Region')
    plt.xlabel('Region')
    plt.ylabel('Total Volume Produced')
    plt.xticks(rotation=45, ha='right')  # Rotate region names if needed
    plt.tight_layout()  # Make sure labels fit inside the plot
    
    # Save the plot as an image
    plt.savefig('visualization/production_by_region.png')
    plt.close() # Close the plot to prevent it from displaying in the console

# Function to plot production by well
def plot_production_by_well(well_prod):
    # Create a bar plot for production by well
    well_prod.plot(kind='bar', color='lightcoral')

    # Customize plot appearance
    plt.title('Total Production by Well')
    plt.xlabel('Well ID')
    plt.ylabel('Total Volume Produced')
    plt.xticks(rotation=0)  # Ensure well IDs are readable
    plt.tight_layout()  # Make sure labels fit inside the plot
    
    # Save the plot as an image
    plt.savefig('visualization/production_by_well.png')
    plt.close()  # Close the plot to prevent it from displaying in the console

# Example usage
if __name__ == "__main__":
    # Load and clean the data using load_data function from data_preprocessing.py
    df_cleaned = load_data('raw_production_data.csv')  # Make sure the file exists in the 'data' folder

    if df_cleaned.empty:
        print("No data loaded!")
    else:
        # Perform the analysis using the functions from analysis.py
        region_prod = production_by_region(df_cleaned)
        well_prod = production_by_well(df_cleaned)

        # Plot the production data
        plot_production_by_region(region_prod)
        plot_production_by_well(well_prod)
