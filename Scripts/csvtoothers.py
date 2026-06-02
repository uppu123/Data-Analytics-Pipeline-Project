# ============================================
# CSV TO JSON & PARQUET CONVERTER
# ============================================

# Install required libraries:
# pip install pandas pyarrow

import pandas as pd

# ============================================
# FILE PATHS
# ============================================

events_csv = "1_Data/Raw/events.csv"
sponsors_csv = "1_Data/Raw/sponsors.csv"

# ============================================
# READ CSV FILES
# ============================================

events_df = pd.read_csv(events_csv)
sponsors_df = pd.read_csv(sponsors_csv)

# ============================================
# CONVERT events.csv → events.json
# ============================================

events_json_output = "1_Data/Raw/events.json"

events_df.to_json(
    events_json_output,
    orient="records",
    indent=4
)

print(f"\n events.csv converted to events.json")
print(f" Saved at: {events_json_output}")

# ============================================
# CONVERT sponsors.csv → sponsors.parquet
# ============================================

sponsors_parquet_output = "1_Data/Raw/sponsors.parquet"

sponsors_df.to_parquet(
    sponsors_parquet_output,
    index=False
)

print(f"\n sponsors.csv converted to sponsors.parquet")
print(f" Saved at: {sponsors_parquet_output}")

# ============================================
# DONE
# ============================================

print("\n ALL FILES CONVERTED SUCCESSFULLY!")