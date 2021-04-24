from requests import get

api_key = "169b613e6ee116a4e0b22d48ffee53f6"


class IncorrectAPIKey(Exception):
    def __init__(self, *args):
        if len(args) != 0:
            self.attrs = args
        else:
            self.attrs = None

    def __str__(self):
        if self.attrs is None:
            return "API key can't be None"
        elif self.attrs[0] == "":
            return "API key can't be empty"
        elif self.attrs[0] == "<Response [401]>":
            return f"incorrect API key '{self.attrs[1]}'"
        elif len(self.attrs[0]) == 0:
            return f"incorrect city name '{self.attrs[1]}'"
        else:
            return "something go wrong"


def get_city_id(city: str, _api_key=api_key):
    if _api_key == "":
        raise IncorrectAPIKey(_api_key)
    res = get("http://api.openweathermap.org/data/2.5/find",
              params={'q': city, 'type': 'like', 'units': 'metric', 'APPID': _api_key})
    if res.__str__() == "<Response [401]>":
        raise IncorrectAPIKey(res.__str__(), _api_key)
    data = res.json()
    if len(data["list"]) == 0:
        raise IncorrectAPIKey(data["list"], city)
    return data['list'][0]['id']


def get_weather_info(city_id, _api_key=api_key):
    res = get(
        "http://api.openweathermap.org/data/2.5/weather",
        params={'id': city_id, 'units': 'metric', 'lang': 'en', 'APPID': _api_key})
    data = res.json()
    if len(data['weather'][0]['description'].capitalize()) > len("Clear sky"):
        description = f"{data['weather'][0]['description'].capitalize().split()[0]}" \
                      f"\n{data['weather'][0]['description'].capitalize().split()[1]}"
        cur_speed = f"{str(data['wind']['speed'])} m/s"
    else:
        description = data['weather'][0]['description'].capitalize()
        cur_speed = f"{str(data['wind']['speed'])} m/s\n"
    if data['main']['temp'] > 0:
        cur_temp = f"+{str(round(data['main']['temp']))} °C"
    else:
        cur_temp = f"{str(round(data['main']['temp']))} °C"
    cur_weather = f"{description}\n {cur_temp}\n{cur_speed}"
    return cur_weather
