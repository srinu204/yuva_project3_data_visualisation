
# ============================================================
# YUVA INTERNSHIP - WEEK 3
# Corrected Movie Correlation Heatmap
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# ------------------------------------------------------------
# 3. Filter movies only
# ------------------------------------------------------------

movies = df[df["type"] == "Movie"].copy()

# ------------------------------------------------------------
# 4. Prepare numerical variables
# ------------------------------------------------------------

movies["date_added"] = pd.to_datetime(
    movies["date_added"],
    format="mixed",
    errors="coerce"
)

movies["year_added"] = movies["date_added"].dt.year

movies["duration_minutes"] = pd.to_numeric(
    movies["duration"].str.extract(r"(\d+)")[0],
    errors="coerce"
)

numeric_df = movies[
    [
        "release_year",
        "year_added",
        "duration_minutes"
    ]
].dropna()

# ------------------------------------------------------------
# 5. Calculate correlations
# ------------------------------------------------------------

correlation_matrix = numeric_df.corr(method="pearson")

# ------------------------------------------------------------
# 6. Create the heatmap
# ------------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="RdBu_r",
    vmin=-1,
    vmax=1,
    center=0,
    linewidths=1.5,
    square=True,
    cbar_kws={
        "label": "Pearson Correlation Coefficient"
    },
    annot_kws={
        "fontsize": 12,
        "fontweight": "bold"
    },
    ax=ax
)

ax.set_title(
    "Correlation Analysis of Netflix Movies",
    fontsize=17,
    fontweight="bold",
    pad=20
)

ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=25,
    ha="right"
)

ax.set_yticklabels(
    ax.get_yticklabels(),
    rotation=0
)

plt.tight_layout()

# ------------------------------------------------------------
# 7. Save the corrected chart
# ------------------------------------------------------------

output_path = CHART_DIR / "09_movie_correlation_heatmap.png"

fig.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close(fig)

# ------------------------------------------------------------
# 8. Display results
# ------------------------------------------------------------

print("\nCORRECTED MOVIE CORRELATION MATRIX")
print("=" * 50)

print(f"Movies included: {len(numeric_df):,}")

print(correlation_matrix.round(3))

print("\nChart saved successfully:")
print(output_path)