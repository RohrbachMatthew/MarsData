import requests
import mysql.connector
from datetime import datetime

# NASA API info
API_KEY = "***********"  # Replace with your personal NASA API key
url = f"https://api.nasa.gov/insight_weather/?api_key={API_KEY}&feedtype=json&ver=1.0"

# Fetch data
response = requests.get(url)
data = response.json()

# Get latest sol
latest_sol = data['sol_keys'][-1]
sol_data = data[latest_sol]

# Prepare values
earth_date = sol_data['First_UTC'].split("T")[0]
time_now = datetime.utcnow().strftime("%H:%M:%S")

temperature_min = sol_data.get("AT", {}).get("mn")
temperature_max = sol_data.get("AT", {}).get("mx")
pressure = sol_data.get("PRE", {}).get("av")
radiation = sol_data.get("RAD", {}).get("av")  # This is often missing – will default to None

connection = mysql.connector.connect(
    host='',
    user='',
    password='',
    database=''
)

