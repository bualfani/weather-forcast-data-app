import requests

api_key = "cb30fc9a023abb0b29a499da5d26be92"


def get_data(location, days, kind):
    url = f"api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filter_data = data['list']
    values = 8 * days
    filter_data = filter_data[:values]

    if kind == 'Graph':
        filter_data = [dict['main']['temp'] for dict in filter_data]
    if kind == 'Sky':
        filter_data = [dict['weather'][0]['main'] for dict in filter_data]

    return filter_data


if __name__ == "__main__":
    get_data()