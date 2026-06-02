import json
import random
from datetime import datetime
import os

# =========================================
# FILE PATHS
# =========================================
INPUT_FILE = r"C:\DEA Project\1_Data\Raw\events.json"
OUTPUT_FILE = r"C:\DEA Project\1_Data\New Raw\events.json"

# Create folder if not exists
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

# =========================================
# LOAD JSON DATA
# =========================================
with open(INPUT_FILE, "r") as f:
    events = json.load(f)

# =========================================
# DIFFERENT DATE FORMATS
# =========================================
date_formats = [
    "%d-%m-%Y",      # 11-04-2026
    "%Y/%m/%d",      # 2026/04/11
    "%d/%m/%Y",      # 11/04/2026
    "%B %d, %Y",     # April 11, 2026
    "%d %B %Y",      # 11 April 2026
    "%m-%d-%Y",      # 04-11-2026
    "%Y.%m.%d",      # 2026.04.11
    "%b %d %Y",      # Apr 11 2026
]

# =========================================
# CHANGE DATE FORMATS RANDOMLY
# =========================================
for event in events:

    # Convert string to datetime object
    original_date = datetime.strptime(
        event["event_date"],
        "%Y-%m-%d"
    )

    # Select random format
    random_format = random.choice(date_formats)

    # Apply format
    event["event_date"] = original_date.strftime(random_format)

# =========================================
# SAVE UPDATED JSON
# =========================================
with open(OUTPUT_FILE, "w") as f:
    json.dump(events, f, indent=4)

# =========================================
# SUCCESS MESSAGE
# =========================================
print("✅ events.json updated successfully!")
print("✅ Different date formats applied.")
print("✅ File saved at:")
print(OUTPUT_FILE)