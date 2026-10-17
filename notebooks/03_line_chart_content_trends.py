
# ============================================================
# YUVA INTERNSHIP - WEEK 3
# Project: Netflix Data Visualization and Reporting
# Chart 2: Netflix Content Addition Trends
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
# 3. Prepare the date_added column
# ------------------------------------------------------------

df["date_added"] = pd.to_datetime(
    df["date_added"],
    format="mixed",
    errors="coerce"
)

df = df.dropna(subset=["date_added"]).copy()

# Extract year and month
df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.to_period("M")

# ------------------------------------------------------------
# 4. Calculate annual and monthly additions
# ------------------------------------------------------------

yearly_additions = (
    df.groupby("year_added")
    .size()
    .sort_index()
)

monthly_additions = (
    df.groupby("month_added")
    .size()
    .sort_index()
)

# ------------------------------------------------------------
# 5. Create the annual trend chart
# ------------------------------------------------------------

fig, ax = plt.subplots(figsize=(13, 7))

ax.plot(
    yearly_additions.index,
    yearly_additions.values,
    color="#E50914",
    linewidth=2.8,
    marker="o",
    markersize=6,
    label="Titles added"
)

# Highlight the highest point
peak_year = yearly_additions.idxmax()
peak_count = yearly_additions.max()

ax.annotate(
    f"Peak: {peak_year}\n{peak_count:,} titles",
    xy=(peak_year, peak_count),
    xytext=(10, 20),
    textcoords="offset points",
    fontsize=10,
    fontweight="bold",
    arrowprops=dict(
        arrowstyle="->",
        color="#333333"
    )
)

ax.set_title(
    "Netflix Content Additions by Year",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.set_xlabel(
    "Year Added to Netflix",
    fontsize=12
)

ax.set_ylabel(
    "Number of Titles Added",
    fontsize=12
)

ax.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

ax.legend(frameon=False)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.set_xticks(yearly_additions.index)
ax.tick_params(axis="x", rotation=45)

fig.text(
    0.5,
    0.01,
    "Source: Netflix Movies and TV Shows dataset. Counts reflect the available dataset snapshot.",
    ha="center",
    fontsize=9,
    color="dimgray"
)

plt.tight_layout(rect=[0, 0.04, 1, 1])

# Save annual chart
annual_path = CHART_DIR / "02_content_additions_by_year.png"

fig.savefig(
    annual_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close(fig)

# ------------------------------------------------------------
# 6. Create a monthly trend chart
# ------------------------------------------------------------

monthly_dates = monthly_additions.index.to_timestamp()

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(
    monthly_dates,
    monthly_additions.values,
    color="#6C5CE7",
    linewidth=2,
    label="Monthly additions"
)

# Add a three-month rolling average
rolling_average = monthly_additions.rolling(
    window=3,
    min_periods=1
).mean()

ax.plot(
    monthly_dates,
    rolling_average.values,
    color="#00A896",
    linewidth=2.5,
    label="Three-month rolling average"
)

ax.set_title(
    "Monthly Netflix Content Additions",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.set_xlabel(
    "Date",
    fontsize=12
)

ax.set_ylabel(
    "Number of Titles Added",
    fontsize=12
)

ax.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

ax.legend(frameon=False)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.text(
    0.5,
    0.01,
    "Source: Netflix Movies and TV Shows dataset. Monthly counts are based on recorded addition dates.",
    ha="center",
    fontsize=9,
    color="dimgray"
)

plt.tight_layout(rect=[0, 0.04, 1, 1])

# Save monthly chart
monthly_path = CHART_DIR / "03_monthly_content_additions.png"

fig.savefig(
    monthly_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close(fig)

# ------------------------------------------------------------
# 7. Display the results
# ------------------------------------------------------------

print("\nNETFLIX CONTENT ADDITIONS BY YEAR")
print("=" * 45)

print(yearly_additions.to_string())

print("\nPEAK ADDITION YEAR")
print("=" * 45)

print(f"Year: {peak_year}")
print(f"Titles added: {peak_count:,}")

print("\nTOP 5 MONTHS BY CONTENT ADDITIONS")
print("=" * 45)

print(
    monthly_additions
    .sort_values(ascending=False)
    .head(5)
    .to_string()
)

print("\nCharts saved successfully:")
print(annual_path)
print(monthly_path)