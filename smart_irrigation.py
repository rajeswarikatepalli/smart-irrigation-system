import random
import time
import csv

soil_moisture = random.randint(20, 60)
threshold = 40

print("Smart Irrigation System")
print("-----------------------")

with open("irrigation_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Reading", "Soil Moisture", "Pump Status"])

    for i in range(10):

        print("Reading:", i + 1)
        print("Soil Moisture:", soil_moisture, "%")

        if soil_moisture < threshold:
            pump_status = "ON"
            soil_moisture = min(soil_moisture + 10, 100)
            print("Pump: ON - Watering plants")
        else:
            pump_status = "OFF"
            print("Pump: OFF - Soil moisture sufficient")

        writer.writerow([i + 1, soil_moisture, pump_status])

        print("-----------------------")
        time.sleep(1)

        # Soil gradually dries when pump is OFF
        if pump_status == "OFF":
            soil_moisture = max(soil_moisture - 3, 0)

print("Simulation completed.")
print("Data saved to irrigation_data.csv")