# weather detection ----
import requests
city = input("Enter the name of the city: ")
unit = input ("In which unit do you want the Temperature? (Celsius -- C / Fahrenheit -- F ) :")
if unit== "F":
    unit = "imperial"
else:
    unit = "metric"
res = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=af07f77740b3d99be88add81f929ca25&units={unit}"
unit_symbol = "°F" if unit == "imperial" else "°C"
try:
    response = requests.get(res)
    if response.status_code == 200:
    # parse JSON and display weather info
        data = response.json()
        print("City:", data.get("name"))
        print("Temperature:", data.get("main", {}).get("temp"), unit_symbol)
        print("Condition:",data.get("weather", [{}])[0].get("description") .title())
        print("Humidity:", data.get("main", {}).get("humidity"), "%")
        print("Wind Speed:", data.get("wind", {}).get("speed"), "m/s")
    else:
        print("❌ City not found. Please check the name and try again.")

except requests.exceptions.RequestException:
    print("❌ Network error. Please check your internet connection.")
