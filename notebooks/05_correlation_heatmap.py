
# ============================================================
# YUVA INTERNSHIP - WEEK 3
# Project: Netflix Data Visualization and Reporting
# Chart 4: Numerical Correlation Heatmap
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
# 3. Prepare numerical variables
# ------------------------------------------------------------

df["date_added"] = pd.to_datetime(
    df["date_added"],
    format="mixed",
    errors="coerce"
)

df["year_added"] = df["date_added"].dt.year

# Extract movie duration in minutes
df["duration_minutes"] = pd.to_numeric(
    df["duration"].str.extract(r"(\d+)")[0],
    errors="coerce"
)

# Retain the numerical columns relevant to our analysis
numeric_df = df[
    [
        "release_year",
        "year_added",
        "duration_minutes"
    ]
].copy()

# ------------------------------------------------------------
# 4. Calculate correlation matrix
# ------------------------------------------------------------

correlation_matrix = numeric_df.corr(
    method="pearson"
)

# ------------------------------------------------------------
# 5. Create the heatmap
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
    "Correlation Between Netflix Numerical Variables",
    fontsize=16,
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
# 6. Save the chart
# ------------------------------------------------------------

output_path = CHART_DIR / "05_correlation_heatmap.png"

fig.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close(fig)

# ------------------------------------------------------------
# 7. Display correlation results
# ------------------------------------------------------------

print("\nNETFLIX NUMERICAL CORRELATION MATRIX")
print("=" * 50)

print(correlation_matrix.round(3))

print("\nPAIRWISE CORRELATIONS")
print("=" * 50)

for i in range(len(correlation_matrix.columns)):
    for j in range(i + 1, len(correlation_matrix.columns)):

        variable_1 = correlation_matrix.columns[i]
        variable_2 = correlation_matrix.columns[j]

        correlation = correlation_matrix.iloc[i, j]

        print(
            f"{variable_1} vs {variable_2}: "
            f"{correlation:.3f}"
        )

print("\nChart saved successfully:")
print(output_path)