import pandas as pd
import json
import os

# =========================================
# BASE FOLDER
# =========================================
BASE_PATH = r"C:\DEA Project\1_Data"

RAW_PATH = os.path.join(BASE_PATH, "Raw")
NEW_RAW_PATH = os.path.join(BASE_PATH, "New Raw")

# Create "New Raw" folder if it doesn't exist
os.makedirs(NEW_RAW_PATH, exist_ok=True)

# =========================================
# LOAD CSV FILES
# =========================================
attendance_df = pd.read_csv(
    os.path.join(RAW_PATH, "attendance.csv")
)

registrations_df = pd.read_csv(
    os.path.join(RAW_PATH, "registrations.csv")
)

sponsors_df = pd.read_csv(
    os.path.join(RAW_PATH, "sponsors.csv")
)

# =========================================
# LOAD JSON FILE
# =========================================
with open(os.path.join(RAW_PATH, "events.json"), "r") as f:
    events_data = json.load(f)

events_df = pd.DataFrame(events_data)

# =========================================
# CREATE EVENT NAME -> EVENT ID MAPPING
# =========================================
event_mapping = dict(
    zip(
        events_df["event_name"].str.strip().str.lower(),
        events_df["event_id"]
    )
)

# =========================================
# FUNCTION TO ADD EVENT_ID
# =========================================
def add_event_id(df):

    # Find column containing event name
    possible_columns = [
        "event_name",
        "Event_Name",
        "event",
        "Event"
    ]

    event_col = None

    for col in possible_columns:
        if col in df.columns:
            event_col = col
            break

    if event_col is None:
        print("❌ Event name column not found.")
        print("Columns are:", df.columns)
        return df

    # Create event_id column
    df["event_id"] = (
        df[event_col]
        .astype(str)
        .str.strip()
        .str.lower()
        .map(event_mapping)
    )

    return df

# =========================================
# ADD EVENT_ID TO FILES
# =========================================
attendance_df = add_event_id(attendance_df)
registrations_df = add_event_id(registrations_df)
sponsors_df = add_event_id(sponsors_df)

# =========================================
# SAVE UPDATED FILES IN "New Raw"
# =========================================
attendance_df.to_csv(
    os.path.join(NEW_RAW_PATH, "attendance.csv"),
    index=False
)

registrations_df.to_csv(
    os.path.join(NEW_RAW_PATH, "registrations.csv"),
    index=False
)

sponsors_df.to_csv(
    os.path.join(NEW_RAW_PATH, "sponsors.csv"),
    index=False
)

# =========================================
# CREATE sponsors.parquet
# =========================================
sponsors_df.to_parquet(
    os.path.join(NEW_RAW_PATH, "sponsors.parquet"),
    index=False
)

# =========================================
# COPY events.json TO "New Raw"
# =========================================
with open(os.path.join(NEW_RAW_PATH, "events.json"), "w") as f:
    json.dump(events_data, f, indent=4)

# =========================================
# SUCCESS MESSAGE
# =========================================
print("\n✅ All files processed successfully!")
print("✅ Files saved in:", NEW_RAW_PATH)

print("\nGenerated Files:")
print("1. attendance.csv")
print("2. registrations.csv")
print("3. sponsors.csv")
print("4. sponsors.parquet")
print("5. events.json")