import sqlite3
import csv

# Connect to database
connection = sqlite3.connect("irrigation.db")
cursor = connection.cursor()

# Create database table
cursor.execute("""
CREATE TABLE IF NOT EXISTS irrigation (
    reading INTEGER,
    soil_moisture INTEGER,
    pump_status TEXT
)
""")

# Read data from CSV file
with open("irrigation_data.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute(
            "INSERT INTO irrigation VALUES (?, ?, ?)",
            (
                int(row["Reading"]),
                int(row["Soil Moisture"]),
                row["Pump Status"]
            )
        )

# Save changes
connection.commit()

# Display saved data
cursor.execute("SELECT * FROM irrigation")
rows = cursor.fetchall()

print("Smart Irrigation Database")
print("-------------------------")

for row in rows:
    print(row)

connection.close()

print("Data saved successfully!")