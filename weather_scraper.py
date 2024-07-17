"""
Weather scraper using OpenWeatherMap API key

Program takes longitude and lattitude as command line input parameters
and produces temperature, wind and rain metrics of the last hour

to execute:
python3 weather_scraper.py <logitude> <latitude>

"""
import requests
import sys


# Function to retrieve weather status from OpenWeatherMap
def get_weather(longitude, latitude, api_key):
    # Define the API endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Response Text: {response.text}")
        return None


# Function to extract and print weather information
def print_weather_info(weather):
    if weather:
        print("Weather as of the last hour:")
        print()

        # temperature data
        temp = weather['main']['temp']
        temp_min = weather['main']['temp_min']
        temp_max = weather['main']['temp_max']
        print(f"Current Temperature: {temp}°C")
        print(f"Min Temperature: {temp_min}°C")
        print(f"Max Temperature: {temp_max}°C")
        print()
        
        # wind data
        wind_speed = weather['wind']['speed']
        wind_deg = weather['wind']['deg']
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Wind Direction: {wind_deg}°")
        print()
        
        # rain data
        rain_1h = weather.get('rain', {}).get('1h', 'No data')
        if rain_1h == 'No data' :
            print(f"Rain Volume (last 1 hour): 0 mm")
        else: 
            print(f"Rain Volume (last 1 hour): {rain_1h} mm")
        print()

        # general weather description
        weather_description = weather['weather'][0]['description']
        print(f"Weather Description: {weather_description}")

    else:
        print("Failed to retrieve weather data")



def main():
    # read cmd args for lon, lat
    if len(sys.argv) == 3:
        longitude = sys.argv[1]     # Durbanville: 18.647499
        latitude = 	sys.argv[2]     # -33.832500
    else: 
        print("Please enter valid Longitude, Latitude arguments")
        sys.exit()

    api_key = "b21fc0b0e6006ec6b0c62372da738631"  #OpenWeatherMap API key

    weather = get_weather(longitude, latitude, api_key)
    print_weather_info(weather)

if __name__ == "__main__":
    main()
