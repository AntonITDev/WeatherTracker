from requests import get
from fake_useragent import UserAgent
from datetime import date
from typing import Any

headers = {'User-Agent': UserAgent().chrome}

def getWeatherByName(
		token: int | str, 
		city: str, 
		country: str,
		units: str = 'metric',
		exclude: str = 'current',
		date: str = date.today().strftime("%Y-%m-%d"),
		tz: str = '+03:00',
		lang:str = 'en')-> Any:
	
	'''Weather city by name
	
	units: ['metric', 'standard', 'imperial']
	exclude: ['current','minutely','hourly', 'daily','alert']

	'''
	url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units={units}&exclude={exclude}$date={date}&tz={tz}&lang={lang}&appid={token}'
	return get(url, headers=headers).json()

def getWeatherById(
		token: int | str, 
		city_id: str,
		units: str = 'metric',
		exclude: str = 'current',
		tz: str = '+03:00',
		date: str = date.today().strftime("%Y-%m-%d"),
		lang:str = 'en') -> Any:
	
	'''Weather city by name
	
	units: ['metric', 'standard', 'imperial']
	exclude: ['current','minutely','hourly', 'daily','alert']
	
	'''

	url = f'https://api.openweathermap.org/data/2.5/weather?id={city_id}&units={units}&exclude={exclude}$date={date}&tz={tz}&lang={lang}&appid={token}'
	return get(url, headers=headers).json()
