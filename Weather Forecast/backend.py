import requests

def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid=e7b2bd866fe8c3d87d296c651954a113"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    
    return filtered_data



if __name__ == "__main__":
    print(get_data("Tokyo",3))