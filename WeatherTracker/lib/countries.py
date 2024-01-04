from json import load

with open(r'WeatherTracker\assets\countries.json', 'r') as file:
	list_countries: dict = load(file)
