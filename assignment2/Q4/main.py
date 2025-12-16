import requests
api_key = "4e07795837ca664d22c8356fc2fca206"
city = input ("Enter City : ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
print("status:", response.status_code)
weather = response.json()
print("Temperature: ", weather["main"]["temp"])
print("Humidity: ", weather["main"]["humidity"])
print("Wind Speed: ", weather["wind"]["speed"])