import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Irrigation Dashboard", layout="wide")

st.title("🌱 Smart Agriculture & Automated Irrigation System")
st.write("Virtual soil moisture monitoring and automated pump control")

try:
    data = pd.read_csv(
        r"C:\Users\rajes\OneDrive\Desktop\Smart_Irrigation\irrigation_data.csv"
    )

    if data.empty:
        st.warning("No sensor readings available.")

    else:
        average = data["Soil Moisture"].mean()
        latest = data.iloc[-1]["Soil Moisture"]
        latest_pump = data.iloc[-1]["Pump Status"]
        pump_on = (data["Pump Status"] == "ON").sum()
        pump_off = (data["Pump Status"] == "OFF").sum()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Average Moisture", f"{average:.1f}%")
        col2.metric("Latest Moisture", f"{latest}%")
        col3.metric("Pump ON Readings", int(pump_on))
        col4.metric("Pump OFF Readings", int(pump_off))

        st.subheader("Latest Pump Status")

        if latest_pump == "ON":
            st.warning("Pump ON — Watering plants")
        else:
            st.success("Pump OFF — Soil moisture sufficient")

        st.subheader("Soil Moisture Graph")

        fig, ax = plt.subplots()
        ax.plot(
            data["Reading"],
            data["Soil Moisture"],
            marker="o",
            label="Soil Moisture"
        )
        ax.axhline(
            y=40,
            linestyle="--",
            label="Threshold (40%)"
        )

        ax.set_xlabel("Reading Number")
        ax.set_ylabel("Soil Moisture (%)")
        ax.set_title("Soil Moisture Monitoring")
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)

        st.subheader("Sensor Readings")
        st.dataframe(data, width="stretch")

except FileNotFoundError:
    st.error("irrigation_data.csv not found. Run the simulation first.")