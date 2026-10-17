import pandas as pd

data = pd.read_csv("irrigation_data.csv")

print("Smart Irrigation Data")
print("---------------------")

print(data)

print("\nAverage Soil Moisture:")
print(data["Soil Moisture"].mean())

print("\nPump ON Count:")
print((data["Pump Status"] == "ON").sum())

print("\nPump OFF Count:")
print((data["Pump Status"] == "OFF").sum())