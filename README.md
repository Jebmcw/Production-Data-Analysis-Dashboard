# Production Data Analysis Dashboard

A modular data analysis pipeline that processes oil & gas production data, generates visualizations, and exports automated reports. Designed as a resume project to demonstrate practical skills in data preprocessing, analysis, visualization, reporting, and testing.

---

## 📊 Features

- **Data Preprocessing**  
  - Cleans raw CSV files: handles missing values, invalid dates, and ensures numeric types.
  - Removes duplicates and formats timestamps.

- **Analysis**
  - Calculates total production by well and by region.
  - Supports custom aggregations.

- **Visualization**
  - Generates bar plots using `matplotlib` for regional and well-level production.
  - Saves plots to disk for use in reports.

- **Reporting**
  - Creates a PDF report using `reportlab`, embedding plots and summary statistics.

- **Testing**
  - Unit tests included for data cleaning and aggregation logic using `unittest`.

---

## 🧠 Tech Stack

- Python 3.x
- Pandas
- Matplotlib
- ReportLab
- unittest (for testing)

---

## 🗂 Project Structure


---

## 🚀 How to Run

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/Production-Data-Analysis-Dashboard.git
   cd Production-Data-Analysis-Dashboard

 - ✅ **Preprocess and plot production data**

    ```bash
    python src/visualization.py

 - ✅ **Generate the final PDF report**

    ```
    python src/reporting.py
    ```

 - ✅ **Run tests for analysis logic**

    ```
    python src/test_analysis.py
    ```

 - ✅ **Run tests for data cleaning**

    ```
    python src/test_data_preprocessing.py
    ```   