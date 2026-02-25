import requests # Import the requests library to make HTTP requests

city = input("Enter city name: ")

api_key = "openweathermap_api_key"  # Replace with your OpenWeatherMap API key
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}" 

response = requests.get(url)  # Make a GET request to the OpenWeatherMap API with the specified city and API key
data = response.json()    # to convert the response from JSON format to dict format

print("Temperature:", data["main"]["temp"])
print ("Weather description:", data["weather"][0]["description"])
print("Humidity:", data["main"]["humidity"])