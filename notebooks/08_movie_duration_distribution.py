
# ============================================================
# YUVA INTERNSHIP - WEEK 3
# Project: Netflix Data Visualization and Reporting
# Chart 7: Movie Duration Distribution
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
# 2. Load and prepare movie durations
# ------------------------------------------------------------

df = pd.read_csv(DATA_PATH)

movies = df[df["type"] == "Movie"].copy()

movies["duration_minutes"] = pd.to_numeric(
    movies["duration"].str.extract(r"(\d+)")[0],
    errors="coerce"
)

durations = movies["duration_minutes"].dropna()

# ------------------------------------------------------------
# 3. Calculate summary statistics
# ------------------------------------------------------------

mean_duration = durations.mean()
median_duration = durations.median()

# ------------------------------------------------------------
# 4. Create the histogram
# ------------------------------------------------------------

fig, ax = plt.subplots(figsize=(12, 7))

ax.hist(
    durations,
    bins=25,
    color="#6C5CE7",
    edgecolor="white",
    linewidth=1.2,
    alpha=0.9
)

# Add average and median reference lines
ax.axvline(
    mean_duration,
    color="#E50914",
    linestyle="--",
    linewidth=2.5,
    label=f"Mean: {mean_duration:.1f} minutes"
)

ax.axvline(
    median_duration,
    color="#00A896",
    linestyle="-.",
    linewidth=2.5,
    label=f"Median: {median_duration:.1f} minutes"
)

# ------------------------------------------------------------
# 5. Format the chart
# ------------------------------------------------------------

ax.set_title(
    "Distribution of Netflix Movie Durations",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.set_xlabel(
    "Movie Duration (minutes)",
    fontsize=12
)

ax.set_ylabel(
    "Number of Movies",
    fontsize=12
)

ax.grid(
    axis="y",
    linestyle="--",
    alpha=0.25
)

ax.set_axisbelow(True)

ax.legend(frameon=False)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.text(
    0.5,
    0.01,
    "Source: Netflix Movies and TV Shows dataset. Durations are based on recorded movie runtimes.",
    ha="center",
    fontsize=9,
    color="dimgray"
)

plt.tight_layout(rect=[0, 0.04, 1, 1])

# ------------------------------------------------------------
# 6. Save the chart
# ------------------------------------------------------------

output_path = CHART_DIR / "08_movie_duration_distribution.png"

fig.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close(fig)

# ------------------------------------------------------------
# 7. Display the results
# ------------------------------------------------------------

print("\nMOVIE DURATION DISTRIBUTION")
print("=" * 45)

print(f"Movies analyzed: {len(durations):,}")
print(f"Average duration: {mean_duration:.2f} minutes")
print(f"Median duration: {median_duration:.2f} minutes")
print(f"Shortest duration: {durations.min():.0f} minutes")
print(f"Longest duration: {durations.max():.0f} minutes")

print("\nMOVIES BY DURATION CATEGORY")
print("=" * 45)

duration_categories = pd.cut(
    durations,
    bins=[0, 60, 90, 120, 180, float("inf")],
    labels=[
        "Up to 60 minutes",
        "61–90 minutes",
        "91–120 minutes",
        "121–180 minutes",
        "Over 180 minutes"
    ]
)

print(
    duration_categories
    .value_counts()
    .sort_index()
    .to_string()
)

print("\nChart saved successfully:")
print(output_path)