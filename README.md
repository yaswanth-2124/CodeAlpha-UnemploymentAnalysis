Unemployment Analysis with Python

Project Overview

This project analyzes unemployment rate trends using Python. The dataset is loaded from a CSV file, cleaned, and visualized using various charts to understand unemployment patterns over time.

Objective

- Analyze unemployment rate data.
- Perform data cleaning and preprocessing.
- Visualize unemployment trends using graphs.
- Understand the distribution of unemployment rates.
- Generate insights from the data.

Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

Dataset

The project uses a CSV file named:

Unemployment_Rate_new.csv

If the file is not found, the program automatically creates a sample unemployment dataset and saves it as a CSV file.

Features

1. Loads unemployment data from a CSV file.
2. Handles missing files using exception handling.
3. Cleans and preprocesses the data.
4. Displays dataset preview.
5. Generates the following visualizations:
   - Line Plot: Unemployment Rate Over Time
   - Bar Plot: Monthly Unemployment Rate
   - Histogram: Distribution of Unemployment Rates

How to Run

Install Required Libraries

pip install pandas matplotlib seaborn

Run the Program

python unemployment_analysis.py

Output

The program generates:

- Dataset preview in the terminal.
- Line chart showing unemployment trends.
- Bar chart showing monthly unemployment rates.
- Histogram showing unemployment rate distribution.

Project Structure

Unemployment-Analysis/
│
├── unemployment_analysis.py
├── Unemployment_Rate_new.csv
├── README.md
├── requirements.txt
└── output.png

Conclusion

This project demonstrates basic data analysis, data visualization, and preprocessing techniques using Python. The generated charts help identify unemployment trends and understand how unemployment rates change over time.

Author

Yaswanth sai vangala