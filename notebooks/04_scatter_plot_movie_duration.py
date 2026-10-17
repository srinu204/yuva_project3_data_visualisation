
# ============================================================
# YUVA INTERNSHIP - WEEK 3
# Project: Netflix Data Visualization and Reporting
# Chart 3: Movie Duration vs. Release Year
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ------------------------------------------------------------
# 1. Define project paths
# ------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_DIR / "data" / "netflix_titles.csv"
CHART_DIR = PROJECT_DIR / "outputs" / "charts"

CHART_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------
# 2. Load the dataset
# ------------------------------------------------------------

df = pd.read_csv(DATA_PATH)

# Select movies only
movies = df[df["type"] == "Movie"].copy()

# Extract duration in minutes
movies["duration_minutes"] = pd.to_numeric(
    movies["duration"].str.extract(r"(\d+)")[0],
    errors="coerce"
)

# Remove rows without usable values
movies = movies.dropna(
    subset=["release_year", "duration_minutes"]
)

# ------------------------------------------------------------
# 3. Create scatter plot
# ------------------------------------------------------------

fig, ax = plt.subplots(figsize=(13, 7))

scatter = ax.scatter(
    movies["release_year"],
    movies["duration_minutes"],
    c=movies["duration_minutes"],
    cmap="plasma",
    alpha=0.65,
    s=35,
    edgecolors="none"
)

# Add color bar
colorbar = fig.colorbar(scatter, ax=ax)

colorbar.set_label(
    "Movie Duration (minutes)",
    fontsize=11
)

# ------------------------------------------------------------
# 4. Add a rolling trend line
# ------------------------------------------------------------

yearly_median = (
    movies.groupby("release_year")["duration_minutes"]
    .median()
    .sort_index()
)

# Use a centered 5-year rolling median to smooth variation
rolling_median = yearly_median.rolling(
    window=5,
    center=True,
    min_periods=2
).median()

ax.plot(
    rolling_median.index,
    rolling_median.values,
    color="#00E5A8",
    linewidth=2.8,
    label="Smoothed yearly median"
)

# ------------------------------------------------------------
# 5. Format the chart
# ------------------------------------------------------------

ax.set_title(
    "Netflix Movie Duration vs. Release Year",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.set_xlabel(
    "Release Year",
    fontsize=12
)

ax.set_ylabel(
    "Movie Duration (minutes)",
    fontsize=12
)

ax.grid(
    linestyle="--",
    alpha=0.25
)

ax.legend(frameon=False)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.text(
    0.5,
    0.01,
    "Source: Netflix Movies and TV Shows dataset. Each point represents a movie with a recorded duration.",
    ha="center",
    fontsize=9,
    color="dimgray"
)

plt.tight_layout(rect=[0, 0.04, 1, 1])

# ------------------------------------------------------------
# 6. Save the chart
# ------------------------------------------------------------

output_path = CHART_DIR / "04_movie_duration_vs_release_year.png"

fig.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close(fig)

# ------------------------------------------------------------
# 7. Display analytical results
# ------------------------------------------------------------

print("\nMOVIE DURATION ANALYSIS")
print("=" * 45)

print(f"Movies analyzed: {len(movies):,}")

print(
    f"Median movie duration: "
    f"{movies['duration_minutes'].median():.1f} minutes"
)

print(
    f"Average movie duration: "
    f"{movies['duration_minutes'].mean():.1f} minutes"
)

print("\nDURATION SUMMARY BY RELEASE PERIOD")
print("=" * 45)

movies["release_period"] = pd.cut(
    movies["release_year"],
    bins=[1900, 1979, 1989, 1999, 2009, 2019, 2021],
    labels=[
        "Before 1980",
        "1980–1989",
        "1990–1999",
        "2000–2009",
        "2010–2019",
        "2020–2021"
    ]
)

period_summary = (
    movies.groupby("release_period", observed=False)["duration_minutes"]
    .agg(["count", "median", "mean"])
    .round(1)
)

print(period_summary)

print("\nChart saved successfully:")
print(output_path)