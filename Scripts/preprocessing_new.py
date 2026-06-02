import pandas as pd
import json
import os
from datetime import datetime

# =====================================================
# PATHS
# =====================================================
BASE_PATH = r"C:\DEA Project\1_Data"

RAW_PATH = os.path.join(BASE_PATH, "New Raw")
PROCESSED_PATH = os.path.join(BASE_PATH, "New Processed")

# Create output folder
os.makedirs(PROCESSED_PATH, exist_ok=True)

# =====================================================
# HELPER FUNCTION FOR CSV CLEANING
# =====================================================
def clean_csv(df, file_name):

    print(f"\n📄 Processing: {file_name}")

    # ---------------------------------
    # REMOVE DUPLICATES
    # ---------------------------------
    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(f"✅ Removed {before - after} duplicate rows")

    # ---------------------------------
    # HANDLE MISSING VALUES
    # ---------------------------------
    for col in df.columns:

        # Numeric columns
        if df[col].dtype in ["int64", "float64"]:

            median_value = df[col].median()

            df[col] = df[col].fillna(median_value)

        # Object/String columns
        else:

            mode_value = df[col].mode()

            if len(mode_value) > 0:
                df[col] = df[col].fillna(mode_value[0])
            else:
                df[col] = df[col].fillna("Unknown")

    print("✅ Missing values handled")

    return df

# =====================================================
# PROCESS attendance.csv
# =====================================================
attendance_path = os.path.join(RAW_PATH, "attendance.csv")

attendance_df = pd.read_csv(attendance_path)

attendance_df = clean_csv(
    attendance_df,
    "attendance.csv"
)

attendance_df.to_csv(
    os.path.join(PROCESSED_PATH, "attendance.csv"),
    index=False
)

# =====================================================
# PROCESS registrations.csv
# =====================================================
registrations_path = os.path.join(
    RAW_PATH,
    "registrations.csv"
)

registrations_df = pd.read_csv(registrations_path)

registrations_df = clean_csv(
    registrations_df,
    "registrations.csv"
)

registrations_df.to_csv(
    os.path.join(PROCESSED_PATH, "registrations.csv"),
    index=False
)

# =====================================================
# PROCESS sponsors.csv
# =====================================================
sponsors_path = os.path.join(
    RAW_PATH,
    "sponsors.csv"
)

sponsors_df = pd.read_csv(sponsors_path)

sponsors_df = clean_csv(
    sponsors_df,
    "sponsors.csv"
)

# Save CSV
sponsors_df.to_csv(
    os.path.join(PROCESSED_PATH, "sponsors.csv"),
    index=False
)

# Save Parquet
sponsors_df.to_parquet(
    os.path.join(PROCESSED_PATH, "sponsors.parquet"),
    index=False
)

# =====================================================
# PROCESS events.json
# =====================================================
events_path = os.path.join(
    RAW_PATH,
    "events.json"
)

with open(events_path, "r") as f:
    events_data = json.load(f)

events_df = pd.DataFrame(events_data)

events_df = clean_csv(
    events_df,
    "events.json"
)

# =====================================================
# STANDARDIZE DATE FORMAT
# =====================================================
possible_formats = [
    "%d-%m-%Y",
    "%Y/%m/%d",
    "%d/%m/%Y",
    "%B %d, %Y",
    "%d %B %Y",
    "%m-%d-%Y",
    "%Y.%m.%d",
    "%b %d %Y",
    "%Y-%m-%d"
]

def parse_date(date_str):

    for fmt in possible_formats:

        try:
            return datetime.strptime(
                str(date_str),
                fmt
            ).strftime("%Y-%m-%d")

        except:
            continue

    return None

# Apply date conversion
events_df["event_date"] = (
    events_df["event_date"]
    .apply(parse_date)
)

# Fill failed dates
events_df["event_date"] = (
    events_df["event_date"]
    .fillna("2026-01-01")
)

# =====================================================
# SAVE CLEANED JSON
# =====================================================
clean_events = events_df.to_dict(
    orient="records"
)

with open(
    os.path.join(PROCESSED_PATH, "events.json"),
    "w"
) as f:

    json.dump(
        clean_events,
        f,
        indent=4
    )

# =====================================================
# SUCCESS MESSAGE
# =====================================================
print("\n===================================")
print("🎉 DATA PREPROCESSING COMPLETED")
print("===================================")

print("\n✅ Files saved in:")
print(PROCESSED_PATH)

print("\nGenerated Files:")
print("1. attendance.csv")
print("2. registrations.csv")
print("3. sponsors.csv")
print("4. sponsors.parquet")
print("5. events.json")