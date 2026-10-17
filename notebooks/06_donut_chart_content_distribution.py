
# ============================================================
# YUVA INTERNSHIP - WEEK 3
# Project: Netflix Data Visualization and Reporting
# Chart 5: Movies vs. TV Shows
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
# 2. Load and summarize the dataset
# ------------------------------------------------------------

df = pd.read_csv(DATA_PATH)

content_counts = df["type"].value_counts()

labels = content_counts.index.tolist()
values = content_counts.values

total_titles = int(values.sum())

# ------------------------------------------------------------
# 3. Create the donut chart
# ------------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 8))

fig.patch.set_facecolor("#171717")
ax.set_facecolor("#171717")

colors = ["#E50914", "#F5C518"]

wedges, texts, autotexts = ax.pie(
    values,
    labels=labels,
    colors=colors,
    startangle=90,
    counterclock=False,
    autopct="%1.1f%%",
    pctdistance=0.78,
    labeldistance=1.08,
    wedgeprops={
        "width": 0.38,
        "edgecolor": "#171717",
        "linewidth": 3
    },
    textprops={
        "color": "white",
        "fontsize": 12
    }
)

# Make percentage labels bold
for autotext in autotexts:
    autotext.set_fontweight("bold")
    autotext.set_fontsize(13)

# ------------------------------------------------------------
# 4. Add total count to the center
# ------------------------------------------------------------

ax.text(
    0,
    0.08,
    f"{total_titles:,}",
    ha="center",
    va="center",
    fontsize=25,
    fontweight="bold",
    color="white"
)

ax.text(
    0,
    -0.13,
    "Total Titles",
    ha="center",
    va="center",
    fontsize=11,
    color="#CCCCCC"
)

# ------------------------------------------------------------
# 5. Add title and subtitle
# ------------------------------------------------------------

ax.set_title(
    "Netflix Content Distribution",
    fontsize=20,
    fontweight="bold",
    color="white",
    pad=25
)

fig.text(
    0.5,
    0.04,
    "Movies and TV Shows in the available dataset",
    ha="center",
    fontsize=11,
    color="#CCCCCC"
)

# ------------------------------------------------------------
# 6. Save the chart
# ------------------------------------------------------------

output_path = CHART_DIR / "06_content_distribution_donut.png"

plt.tight_layout(rect=[0, 0.08, 1, 1])

fig.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight",
    facecolor=fig.get_facecolor()
)

plt.show()
plt.close(fig)

# ------------------------------------------------------------
# 7. Display the results
# ------------------------------------------------------------

print("\nNETFLIX CONTENT DISTRIBUTION")
print("=" * 40)

for label, value in content_counts.items():
    percentage = value / total_titles * 100

    print(
        f"{label}: {value:,} titles "
        f"({percentage:.2f}%)"
    )

print(f"\nTotal titles: {total_titles:,}")
print(f"Chart saved successfully: {output_path}")