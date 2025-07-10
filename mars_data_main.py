import requests
import mysql.connector
from datetime import datetime, UTC

# NASA API info
API_KEY = "ZH3DSfIjxyiFemcVLaoS81uLVKrVfN1Nkqjjgcec"
url = f"https://api.nasa.gov/insight_weather/?api_key={API_KEY}&feedtype=json&ver=1.0"

# Fetch data
response = requests.get(url)
data = response.json()

# Connect to database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Password1',
    database='mars',
    port='3307'
)
cursor = connection.cursor()
inserted_count = 0
# Loop through all sols available in the feed
for sol in data['sol_keys']:
    sol_data = data[sol]

    # Extract values
    earth_date = sol_data['First_UTC'].split("T")[0]
    time_now = datetime.now(UTC).time().strftime("%H:%M:%S")
    temperature_min = sol_data.get("AT", {}).get("mn")
    temperature_max = sol_data.get("AT", {}).get("mx")
    pressure = sol_data.get("PRE", {}).get("av")
    radiation = sol_data.get("RAD", {}).get("av")

    #  Check if sol already exists
    cursor.execute("SELECT COUNT(*) FROM mars_data WHERE date = %s", (earth_date,))
    exists = cursor.fetchone()[0]

    #  Insert only if it's not already in the table
    if exists == 0:
        cursor.execute("""
            INSERT INTO mars_data (date, time, max_temp, pressure, radiation, min_temp)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (earth_date, time_now, temperature_max, pressure, radiation, temperature_min))
        connection.commit()
        print(f"Inserted data for sol {sol} ({earth_date})")
    else:
        print(f"Skipped sol {sol} ({earth_date}) — already exists.")

if inserted_count == 0:
    print("No New Data Today")

connection.close()