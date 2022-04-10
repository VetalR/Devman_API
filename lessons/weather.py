import requests
from requests_body import Weather

LOCATIONS = ['San-francisco', 'Sheremetievo', 'Cherepovets']


def _weather(loc, param):
    response = requests.get(url=f'http://wttr.dvmn.org/{loc}', params=param)
    response.raise_for_status()
    return response.text


def main():
    for location in LOCATIONS:
        print(_weather(location, Weather.weather_param))


if __name__ == '__main__':
    main()
