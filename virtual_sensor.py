import random
import time
import csv

print("Smart Irrigation System")
print("-----------------------")

with open("irrigation_data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # CSV headings
    writer.writerow(["Reading", "Soil Moisture", "Pump Status"])

    for i in range(10):

        soil_moisture = random.randint(20, 80)

        if soil_moisture < 40:
            pump_status = "ON"
        else:
            pump_status = "OFF"

        print("Reading", i + 1)
        print("Soil Moisture:", soil_moisture, "%")
        print("Pump:", pump_status)

        writer.writerow([i + 1, soil_moisture, pump_status])

        print("-----------------------")

        time.sleep(2)

print("Simulation completed.")
print("Data saved to irrigation_data.csv")
