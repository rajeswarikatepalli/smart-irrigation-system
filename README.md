\# Smart Agriculture \& Automated Irrigation System Using Python



\## Project Overview

This project simulates a smart irrigation system using Python. It monitors virtual soil moisture readings and automatically determines whether the water pump should be ON or OFF based on a 40% moisture threshold.



\## Features

\- Virtual soil moisture sensor simulation

\- Automatic pump ON/OFF decision

\- Sensor data stored in a CSV file

\- Data analysis using Pandas

\- Soil moisture visualization using Matplotlib

\- Data storage using SQLite

\- Interactive dashboard using Streamlit



\## Technologies Used

\- Python

\- Pandas

\- Matplotlib

\- SQLite

\- Streamlit

\- CSV



\## Pump Control Logic

\- If soil moisture is below 40%, the pump turns ON.

\- If soil moisture is 40% or above, the pump remains OFF.



\## How to Run

1\. Install the required packages:

&#x20;  `python -m pip install pandas matplotlib streamlit`

2\. Run the irrigation simulation:

&#x20;  `python smart\_irrigation.py`

3\. Run the dashboard:

&#x20;  `python -m streamlit run dashboard.py`



\## Project Type

Software-based IoT simulation using Python. No physical hardware is required.

