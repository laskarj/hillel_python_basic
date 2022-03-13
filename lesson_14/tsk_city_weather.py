import requests
"""
1. создать функцию(ии) для  определения погоды по данным(Город).
2. Вынести некоторрые данные в константу(ы).
3. Для запуска функции использовать if __name__ == '__main__': запуск!
4. Создать файл test.py  внутри создать Класс для тестирования функции, с помощью unittest.
"""


def decor_data_func(func):
    """I decided to do it through the decorator"""
    def city_weather():
        data: dict = func()
        if data["cod"] != "404":  # If not error in data, Processing data
            y: dict = data['main']
            current_t: float = y['temp']
            current_p: int = y["pressure"]
            current_h: int = y["humidity"]
            z: list = data["weather"]
            weather_description: str = z[0]["description"]
            c: dict = data["sys"]
            country: str = c['country']
            celsius: int = round(current_t - 273.15)
            return f'City temperature:{celsius} degrees Celsius \nPressure:{current_p} Pa\n'\
                   f'Weather description: {weather_description} \nHumidity:{current_h}%\nCountry: {country}'
        else:
            return 'City not found!'
    return city_weather


@decor_data_func
def city_data():
    city_name = input('Please fill up your city:')
    base_url: str = 'http://api.openweathermap.org/data/2.5/weather?'
    api_kye: str = 'd82759ebf4a4a5ed987117c4027b9dfa'
    complete_url: str = base_url + "appid=" + api_kye + "&q=" + city_name
    response: requests.models.Response = requests.get(complete_url)
    r_data: dict = response.json()
    return r_data


if __name__ == "__main__":
    print(city_data())
