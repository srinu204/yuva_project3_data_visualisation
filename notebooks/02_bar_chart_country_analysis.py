
# ============================================================
# YUVA INTERNSHIP - WEEK 3
# Project: Netflix Data Visualization and Reporting
# Chart 1: Top 10 Countries by Netflix Content
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ------------------------------------------------------------
# 1. Project paths
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
# 3. Prepare country data
# ------------------------------------------------------------

country_df = df.dropna(subset=["country"]).copy()

country_df["country"] = country_df["country"].str.split(",")

country_df = country_df.explode("country")

country_df["country"] = country_df["country"].str.strip()

country_counts = (
    country_df["country"]
    .value_counts()
    .head(10)
    .sort_values(ascending=True)
)

# ------------------------------------------------------------
# 4. Create the visualization
# ------------------------------------------------------------

fig, ax = plt.subplots(figsize=(12, 7))

colors = plt.cm.viridis(
    [i / (len(country_counts) - 1) for i in range(len(country_counts))]
)

bars = ax.barh(
    country_counts.index,
    country_counts.values,
    color=colors,
    height=0.7
)

# ------------------------------------------------------------
# 5. Add value labels
# ------------------------------------------------------------

for bar in bars:
    width = bar.get_width()

    ax.text(
        width + max(country_counts.values) * 0.015,
        bar.get_y() + bar.get_height() / 2,
        f"{int(width):,}",
        va="center",
        fontsize=10,
        fontweight="bold"
    )

# ------------------------------------------------------------
# 6. Improve chart appearance
# ------------------------------------------------------------

ax.set_title(
    "Top 10 Countries by Netflix Content",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.set_xlabel(
    "Number of Titles",
    fontsize=12,
    labelpad=10
)

ax.set_ylabel(
    "Country",
    fontsize=12,
    labelpad=10
)

ax.grid(
    axis="x",
    linestyle="--",
    alpha=0.25
)

ax.set_axisbelow(True)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.margins(x=0.12)

fig.text(
    0.5,
    0.01,
    "Source: Netflix Movies and TV Shows dataset | Titles may be associated with multiple countries.",
    ha="center",
    fontsize=9,
    color="dimgray"
)

plt.tight_layout(rect=[0, 0.04, 1, 1])

# ------------------------------------------------------------
# 7. Save the chart
# ------------------------------------------------------------

output_path = CHART_DIR / "01_top_10_countries.png"

fig.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close(fig)

# ------------------------------------------------------------
# 8. Display the results
# ------------------------------------------------------------

print("\nTOP 10 COUNTRIES BY NETFLIX CONTENT")
print("=" * 45)

print(
    country_counts.sort_values(ascending=False).to_string()
)

print(f"\nChart saved successfully: {output_path}")