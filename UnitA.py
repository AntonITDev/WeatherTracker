from WeatherTracker import *

def test():
	API_KEY = 'Enter_api_key_from_openweathermap'
	city_name = 'Enter_city_title'
	country = list_countries['Enter_Country_title']
	print(getWeatherByName(API_KEY, city_name, country))


if __name__ == "__main__":
	test()
