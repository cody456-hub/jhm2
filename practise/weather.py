import requests
import matplotlib.pyplot as plt

api_key = '65e48f988ae30c4af07ee29855ec28f7'
base_url = 'https://api.openweathermap.org/data/2.5/weather'

def display_menu(city_name):
    input("Enter you city name: ")

def get_weather_data(city_name):
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  
    }
    response = requests.get(base_url, params=params)
    return response.json()


def plot_weather_data(weather_data):
    fig, ax = plt.subplots()
    ax.set_title('Weather parameters Visualization')
    
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    weather_condition = weather_data['weather'][0]['description']
    uv_index = weather_data['uv_index']


    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Weather Condition: {weather_condition}")
    print(f"UV Index: {uv_index}")
    
    
    ax.plot([temperature], label='Temperature (°C)')
    ax.plot([humidity], label='Humidity (%)')
    ax.plot([wind_speed], label='Wind Speed (m/s)')
    ax.plot(uv_index, label='UV Index')
    
    ax.legend()
    plt.show()

    def main(): print() 
    if __name__ == "__main__": 
        main()