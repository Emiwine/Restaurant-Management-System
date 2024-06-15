import requests
import json
import pyttsx3

def initialize_tts_engine():
    """Initialize and return the text-to-speech engine."""
    return pyttsx3.init()

def get_city_name():
    """Prompt the user to enter the city name and return it."""
    return input("Enter the city name: ")

def fetch_weather_data(city):
    """Fetch weather data for the given city from WeatherAPI."""
    api_key = "62dca1fdab1246ad8e052113241506"
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return json.loads(response.text)

def extract_weather_details(weather_data):
    """Extract and return relevant weather details from the weather data."""
    location = weather_data["location"]
    current = weather_data["current"]
    
    details = {
        "name": location["name"],
        "region": location["region"],
        "country": location["country"],
        "local_time": location["localtime"],
        "temperature_c": current["temp_c"],
        "temperature_f": current["temp_f"],
        "condition": current["condition"]["text"],
        "humidity": current["humidity"]
    }
    return details

def format_weather_details(details):
    """Format and return weather details into a readable string."""
    return (
        f"Location: {details['name']}, {details['region']}, {details['country']}\n"
        f"Local Time: {details['local_time']}\n"
        f"Temperature: {details['temperature_c']}°C ({details['temperature_f']}°F)\n"
        f"Condition: {details['condition']}\n"
        f"Humidity: {details['humidity']}%"
    )

def speak_weather_details(engine, details):
    """Use the text-to-speech engine to speak the weather details."""
    engine.say(details)
    engine.runAndWait()

def main():
    """Main function to execute the weather fetching and speaking process."""
    try:
        # Initialize the text-to-speech engine
        tts_engine = initialize_tts_engine()
        
        # Get the city name from the user
        city = get_city_name()
        
        # Fetch and parse the weather data
        weather_data = fetch_weather_data(city)
        
        # Extract and format weather details
        weather_details = extract_weather_details(weather_data)
        formatted_details = format_weather_details(weather_details)
        
        # Print and speak the weather details
        print(formatted_details)
        speak_weather_details(tts_engine, formatted_details)
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError as e:
        print(f"Error parsing weather data: Missing key {e}")

if __name__ == "__main__":
    main()
