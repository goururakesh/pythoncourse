import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}"
    
    # Make a GET request to the API
    response = requests.get(complete_url)
    
    # Check the status code of the response
    if response.status_code == 200:
        data = response.json()
        
        # Extracting data
        main = data['main']
        weather = data['weather'][0]
        
        # Getting temperature, pressure, humidity, and weather description
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        weather_description = weather['description']
        
        # Print the results
        print(f"Temperature: {temperature}K")
        print(f"Pressure: {pressure}hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {weather_description}")
    else:
        print("City not found!")

# Example usage
api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
city = "London"
get_weather(api_key, city)
