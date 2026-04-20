import csv
import random
from datetime import datetime, timedelta
import os

# Absolute safe path (works from anywhere)
BASE_PATH = os.path.join(os.path.dirname(__file__), "../1_Data/raw/")
BASE_PATH = os.path.abspath(BASE_PATH)

print(" Saving files to:", BASE_PATH)

os.makedirs(BASE_PATH, exist_ok=True)

names = ["Aarav", "Vivaan", "Aditya", "Krishna", "Ishaan", "Riya", "Ananya", "Diya", "Meera", "Sara"]
surnames = ["Sharma", "Verma", "Singh", "Gupta", "Mehta"]
departments = ["CSE", "ECE", "ME", "CE", "EE"]
genders = ["Male", "Female"]

events = [
    ("E01","Football","Team Sport","2026-04-11"),
    ("E02","Basketball","Team Sport","2026-04-13"),
    ("E03","Cricket","Team Sport","2026-04-12"),
    ("E04","Badminton","Individual","2026-04-13"),
    ("E05","Table Tennis","Individual","2026-04-12"),
    ("E06","Chess","Indoor","2026-04-11"),
    ("E07","Athletics","Outdoor","2026-04-13"),
    ("E08","Swimming","Water","2026-04-12"),
    ("E09","Volleyball","Team Sport","2026-04-12"),
    ("E10","Tennis","Individual","2026-04-11")
]

event_names = [e[1] for e in events]

# ---------------- EVENTS ----------------
with open(os.path.join(BASE_PATH, "events.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["event_id","event_name","category","event_date"])
    for e in events:
        writer.writerow(e)

# ---------------- REGISTRATIONS ----------------
with open(os.path.join(BASE_PATH, "registrations.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["student_id","name","department","gender","event_name","registration_time","payment_amount"])
    
    for i in range(1, 501):
        student_id = f"S{i:03d}"
        name = random.choice(names) + " " + random.choice(surnames)
        dept = random.choice(departments)
        gender = random.choice(genders)
        event = random.choice(event_names)
        reg_time = datetime(2026, 2, 1) + timedelta(minutes=random.randint(0, 20000))
        payment = random.choice([100, 200, 300])
        
        writer.writerow([student_id, name, dept, gender, event, reg_time, payment])

# ---------------- ATTENDANCE ----------------
with open(os.path.join(BASE_PATH, "attendance.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["student_id","event_name","attendance_status"])
    
    for i in range(1, 501):
        student_id = f"S{i:03d}"
        event = random.choice(event_names)
        status = random.choice(["Present", "Absent"])
        
        writer.writerow([student_id, event, status])

# ---------------- SPONSORS ----------------
sponsors = ["Nike","Adidas","Puma","RedBull","Pepsi","CocaCola","Reliance","Tata","Infosys","Wipro"]

with open(os.path.join(BASE_PATH, "sponsors.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sponsor_name","event_name","sponsorship_amount"])
    
    for i in range(20):
        sponsor = random.choice(sponsors)
        event = random.choice(event_names)
        amount = random.randint(5000, 50000)
        
        writer.writerow([sponsor, event, amount])

print("All datasets generated successfully in 1_Data/raw/")