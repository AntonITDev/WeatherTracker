import aiohttp
from datetime import date
from typing import Awaitable
from lib.config import BASE_URL, API_URL, HEADERS
from lib.models import WeatherData

async def request(query: str) -> Awaitable:
	async with aiohttp.ClientSession(base_url=BASE_URL, headers=HEADERS) as session:
		async with session.get(API_URL+query) as response:
			if response.status != 200:
				raise aiohttp.ClientConnectionError('API error')
			return await response.json()
		

"""
	units: ['metric', 'standard', 'imperial']
	exclude: ['current','minutely','hourly', 'daily','alert']
"""
async def getWeatherByName(
		*,
		key: int | str, 
		city: str, 
		country: str = None,
		units: str = 'metric',
		exclude: str = 'current',
		date: str = date.today().strftime("%Y-%m-%d"),
		tz: str = '+03:00',
		lang: str = 'en')-> WeatherData:
	
	"""Get weather by city name"""

	return WeatherData(await request(f'q={city},{country}&units={units}&exclude={exclude}$date={date}&tz={tz}&lang={lang}&appid={key}'))

async def getWeatherById(
		*,
		key: int | str, 
		city_id: str,
		units: str = 'metric',
		exclude: str = 'current',
		tz: str = '+03:00',
		date: str = date.today().strftime("%Y-%m-%d"),
		lang:str = 'en') -> WeatherData:
	
	"""Get weather data by city id"""
	return WeatherData(await request(f'id={city_id}&units={units}&exclude={exclude}$date={date}&tz={tz}&lang={lang}&appid={key}'))

async def getWeatherByCoords(
		*,
		key: int | str, 
		lat: float | str,
		lon: float | str,
		units: str = 'metric',
		exclude: str = 'current',
		tz: str = '+03:00',
		date: str = date.today().strftime("%Y-%m-%d"),
		lang:str = 'en') -> WeatherData:
	
	"""Get weather data by city coords"""
	return WeatherData(await request(f'lat={lat}&lon={lon}&units={units}&exclude={exclude}$date={date}&tz={tz}&lang={lang}&appid={key}'))