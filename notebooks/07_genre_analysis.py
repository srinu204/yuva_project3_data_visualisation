
# ============================================================
# YUVA INTERNSHIP - WEEK 3
# Project: Netflix Data Visualization and Reporting
# Chart 6: Most Common Netflix Genres
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

# ------------------------------------------------------------
# 3. Split and count genre appearances
# ------------------------------------------------------------

genre_df = df[["show_id", "listed_in"]].copy()

genre_df["listed_in"] = genre_df["listed_in"].str.split(",")

genre_df = genre_df.explode("listed_in")

genre_df["listed_in"] = genre_df["listed_in"].str.strip()

genre_counts = (
    genre_df["listed_in"]
    .value_counts()
    .head(10)
    .sort_values(ascending=True)
)

# ------------------------------------------------------------
# 4. Create the horizontal bar chart
# ------------------------------------------------------------

fig, ax = plt.subplots(figsize=(12, 8))

colors = plt.cm.plasma(
    [i / (len(genre_counts) - 1) for i in range(len(genre_counts))]
)

bars = ax.barh(
    genre_counts.index,
    genre_counts.values,
    color=colors,
    height=0.72
)

# ------------------------------------------------------------
# 5. Add labels to each bar
# ------------------------------------------------------------

for bar in bars:
    width = bar.get_width()

    ax.text(
        width + max(genre_counts.values) * 0.015,
        bar.get_y() + bar.get_height() / 2,
        f"{int(width):,}",
        va="center",
        fontsize=10,
        fontweight="bold"
    )

# ------------------------------------------------------------
# 6. Format the visualization
# ------------------------------------------------------------

ax.set_title(
    "Top 10 Netflix Genres and Categories",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.set_xlabel(
    "Number of Genre Appearances",
    fontsize=12
)

ax.set_ylabel(
    "Genre or Category",
    fontsize=12
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
    "Source: Netflix Movies and TV Shows dataset. A title may appear in multiple categories.",
    ha="center",
    fontsize=9,
    color="dimgray"
)

plt.tight_layout(rect=[0, 0.04, 1, 1])

# ------------------------------------------------------------
# 7. Save the chart
# ------------------------------------------------------------

output_path = CHART_DIR / "07_top_10_genres.png"

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

print("\nTOP 10 NETFLIX GENRES AND CATEGORIES")
print("=" * 50)

print(
    genre_counts.sort_values(ascending=False).to_string()
)

print("\nTotal distinct genre/category labels:")
print(genre_df["listed_in"].nunique())

print("\nChart saved successfully:")
print(output_path)