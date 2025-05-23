import requests

def get_weather_data(city_name, api_key):
    """
    Fetch weather data from OpenWeatherMap API for a given city.
    
    Args:
        city_name (str): Name of the city to fetch weather data for.
        api_key (str): Your OpenWeatherMap API key.
    
    Returns:
        dict: Parsed JSON response containing weather data.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use metric units for temperature in Celsius
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather_info(weather_data):
    """
    Display weather information based on the retrieved data.
    
    Args:
        weather_data (dict): Weather data retrieved from the API.
    """
    if weather_data:
        city = weather_data.get("name", "Unknown location")
        main = weather_data.get("main", {})
        weather = weather_data.get("weather", [{}])[0]
        
        temperature = main.get("temp", "N/A")
        humidity = main.get("humidity", "N/A")
        condition = weather.get("description", "N/A")
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition.capitalize()}")
    else:
        print("No weather data to display.")

if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual OpenWeatherMap API key
    API_KEY = "your_api_key_here"
    city = input("Enter the city name: ")
    
    weather_data = get_weather_data(city, "bd5e378503939ddaee76f12ad7a97608")
    display_weather_info(weather_data)