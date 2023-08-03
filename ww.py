

import requests
api_key = '9cc9bba0b04c2c60e49346cc51ab0f53'
city = input(" Please Enter city name: 🏙️")

while True:
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("0. Exit")
    userip = int(input("Enter your choice: "))

    if userip == 1:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']

           # print("Weather:", weather," ☁️")
            print("Temperature: ", temperature ,"°C 🌡️")
            print(f"Humidity: {humidity}%")
        else:
            print("Failed to fetch weather data. Please check your city name and API key.")

    elif userip == 2:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            wind_speed = data['wind']['speed']

            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("Failed to fetch weather data 😐 Please check your city name and API key.")

    elif userip == 0:
        print("Exiting 🙈 ")
        break

    else:
        print("Invalid choice. Please try again. 🌐")

