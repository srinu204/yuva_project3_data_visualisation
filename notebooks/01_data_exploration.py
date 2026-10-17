
# ============================================================
# YUVA INTERNSHIP - WEEK 3
# Project: Netflix Data Visualization and Reporting
# Stage 1: Data Exploration
# ============================================================

import pandas as pd
from pathlib import Path

# ------------------------------------------------------------
# 1. Define project paths
# ------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_DIR / "data" / "netflix_titles.csv"

# ------------------------------------------------------------
# 2. Load the dataset
# ------------------------------------------------------------

df = pd.read_csv(DATA_PATH)

print("\n" + "=" * 60)
print("NETFLIX DATA VISUALIZATION PROJECT")
print("=" * 60)

# ------------------------------------------------------------
# 3. Display dataset dimensions
# ------------------------------------------------------------

print("\n1. DATASET DIMENSIONS")
print("-" * 40)

print(f"Total records: {df.shape[0]}")
print(f"Total columns: {df.shape[1]}")

# ------------------------------------------------------------
# 4. Display column information
# ------------------------------------------------------------

print("\n2. COLUMN INFORMATION")
print("-" * 40)

df.info()

# ------------------------------------------------------------
# 5. Display the first five records
# ------------------------------------------------------------

print("\n3. FIRST FIVE RECORDS")
print("-" * 40)

print(df.head())

# ------------------------------------------------------------
# 6. Check missing values
# ------------------------------------------------------------

print("\n4. MISSING VALUES")
print("-" * 40)

missing_values = df.isnull().sum()

print(missing_values[missing_values > 0])

# ------------------------------------------------------------
# 7. Check duplicate records
# ------------------------------------------------------------

print("\n5. DUPLICATE RECORDS")
print("-" * 40)

print(f"Duplicate rows: {df.duplicated().sum()}")

# ------------------------------------------------------------
# 8. Analyze content types
# ------------------------------------------------------------

print("\n6. CONTENT TYPE DISTRIBUTION")
print("-" * 40)

print(df["type"].value_counts())

# ------------------------------------------------------------
# 9. Analyze release years
# ------------------------------------------------------------

print("\n7. RELEASE YEAR SUMMARY")
print("-" * 40)

print(df["release_year"].describe())

# ------------------------------------------------------------
# 10. Analyze ratings
# ------------------------------------------------------------

print("\n8. CONTENT RATINGS")
print("-" * 40)

print(df["rating"].value_counts(dropna=False).head(10))

# ------------------------------------------------------------
# 11. Analyze movie durations
# ------------------------------------------------------------

print("\n9. MOVIE DURATIONS")
print("-" * 40)

movies = df[df["type"] == "Movie"].copy()

movie_minutes = pd.to_numeric(
    movies["duration"].str.extract(r"(\d+)")[0],
    errors="coerce"
)

print(movie_minutes.describe())

print("\n" + "=" * 60)
print("DATA EXPLORATION COMPLETED")
print("=" * 60)