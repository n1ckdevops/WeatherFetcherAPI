import datetime
import requests

API_KEY = "9e8977f254762afd56c18f1199caaef0"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

now = datetime.datetime.now()

date_string = now.strftime("%dth %B")

time_string = now.strftime("%H:%M")
print()
print(f"Welcome to Weather Forecast with Nick!\n"
      f"\nToday is {date_string} and it's {time_string}.")
print()
city = input("Enter a city: ")
req_inf = input("""What sort of information would you like to know?
❖ General (Press "1")
❖ Detailed (Press "2")
___________
Enter: """)

if req_inf == "1":
    print()
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    country = data["sys"]["country"]
    city = data["name"]
    temperature = round(data["main"]["temp"])
    temp_feels_like = round(data["main"]["feels_like"])
    weather = data["weather"][0]['description']
    general_information = f"Your city: {city}\nWeather: {weather}\nTemperature: {temperature}˚C"
    detailed_information = f"Your country: {country}\n{general_information}\nFeels like: {temp_feels_like}˚C"
    if req_inf == "1":
        print(general_information)
    elif req_inf == "2":
        print(detailed_information)
    else:
        print("You had to think before you pressed, bye.")
else:
    print("An error occurred.")
