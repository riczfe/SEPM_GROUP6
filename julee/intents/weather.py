import requests


def get_weather(city_name):
    api_key = "8ef61edcf1c576d65d836254e11ea420"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404" and x["cod"] != "400":
        y = x["main"]
        current_temperature = int(
            y["temp"]) - 273  # round the temperature in Kelvin, then convert to Celcius
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        result = "It's currently " + str(weather_description) + ", with the temperature of " + str(current_temperature) + " degree and the humidity is " + str(current_humidiy) + " percent"

        return result
    else:
        return "City is not found."
