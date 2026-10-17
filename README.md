# Netflix Data Visualization and Reporting

## Project Overview

This project was completed as part of the Yuva Internship Week 3 Data Visualization and Reporting task. It explores the Netflix Movies and TV Shows dataset using Python to identify patterns, compare categories, and communicate findings through clear and informative visualizations.

The project demonstrates practical skills in data exploration, data preparation, statistical analysis, visualization, and report writing.

## Objectives

* Explore the structure and quality of the Netflix dataset.
* Compare content distribution across countries.
* Analyze annual and monthly content addition patterns.
* Examine relationships between movie release years and durations.
* Identify the most frequent genres and categories.
* Compare movies and TV shows.
* Present findings in a structured Word report.

## Dataset

The project uses the Netflix Movies and TV Shows dataset available on Kaggle.

Dataset source: https://www.kaggle.com/datasets/shivamb/netflix-shows

The dataset contains 8,807 records and 12 columns.

## Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Plotly
* Jupyter
* python-docx

## Visualizations

The project includes:

1. Top 10 countries by content count — bar chart
2. Annual content additions — line chart
3. Monthly content additions — line chart
4. Movie duration versus release year — scatter plot
5. Movie-only numerical correlation — heatmap
6. Movie and TV show distribution — donut chart
7. Top 10 genres and categories — bar chart
8. Movie duration distribution — histogram

## Key Findings

* The dataset contains 8,807 titles, including 6,131 movies and 2,676 TV shows.
* Movies represent approximately 69.62% of the dataset.
* The United States has the highest number of country-associated title appearances.
* International Movies is the most frequent category in the genre analysis.
* Movie durations are concentrated in the 91–120-minute range.
* The movie-only correlation analysis identifies a negative association between release year and duration.

These findings describe the available dataset and should not be interpreted as a representation of Netflix's current catalog.

## Project Structure

```text
yuva_project3_data_visualisation/
├── data/
│   └── netflix_titles.csv
├── notebooks/
│   └── Python analysis and visualization scripts
├── outputs/
│   ├── charts/
│   └── reports/
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

1. Clone or download the project repository.

2. Install Python and create a virtual environment.

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure the dataset is saved at `data/netflix_titles.csv`.

5. Run the Python scripts in the `notebooks` folder to explore the data and generate visualizations.

6. Run `10_generate_week3_report.py` to create the Word report.

Run commands from the project's root directory.

## Project Report

The final report is saved at:

`outputs/reports/Yuva_Week3_Data_Visualization_Report.docx`

It includes the project objectives, dataset description, methodology, visualizations, findings, recommendations, limitations, conclusion, and references.

## Conclusion

This project demonstrates how Python-based visualization techniques can transform raw data into meaningful insights. It emphasizes data quality, appropriate chart selection, clear communication, and careful interpretation of analytical results.

**Project:** Yuva Internship — Week 3
**Title:** Netflix Data Visualization and Reporting
