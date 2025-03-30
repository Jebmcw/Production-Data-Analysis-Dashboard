# src/reporting.py
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from analysis import production_by_region, production_by_well
from data_preprocessing import load_data

# Function to save production report as PDF, including charts
def save_production_report_pdf(region_prod, well_prod):
    c = canvas.Canvas("reports/production_report.pdf", pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica", 18)
    c.drawString(100, height - 100, "Production Report")

    # Production by Region Table
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 150, "Production by Region:")
    c.drawString(100, height - 170, f"Texas: {region_prod['Texas']}")
    c.drawString(100, height - 190, f"Oklahoma: {region_prod['Oklahoma']}")

    # Adding the chart to the PDF
    c.drawImage("visualization/production_by_region.png", 100, height - 400, width=400, height=200)

    # Production by Well Table
    c.drawString(100, height - 450, "Production by Well:")
    for well_id, production in well_prod.items():
        c.drawString(100, height - 470 - 20 * (well_id - 1), f"Well {well_id}: {production}")

    # Adding the chart to the PDF
    c.drawImage("visualization/production_by_well.png", 100, height - 700, width=400, height=200)

    # Save the PDF
    c.save()

    print("Production report has been saved to 'production_report.pdf'")

# Example usage
if __name__ == "__main__":
    # Load and clean the data
    df_cleaned = load_data('raw_production_data.csv')

    if not df_cleaned.empty:
        # Perform the analysis using the functions from analysis.py
        region_prod = production_by_region(df_cleaned)
        well_prod = production_by_well(df_cleaned)

        # Save the production report to PDF
        save_production_report_pdf(region_prod, well_prod)
