import requests

LOCATIONS = ['London', 'Sheremetievo', 'Cherepovets']


def check_weather(location):
    weather_param = {
        'nTqu': '',
        'lang': 'ru',
        'Kum': ''
    }
    response = requests.get(url=f'http://wttr.dvmn.org/{location}',
                            params=weather_param)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    for locate in LOCATIONS:
        print(check_weather(locate))
