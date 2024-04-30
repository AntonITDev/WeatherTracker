from datetime import datetime
from typing import Awaitable
from .models import WeatherData
from .config import Configuration
from typing import Union
from .languages import Languages
import aiohttp

class WeatherTracker:
	def __init__(self, api_key: Union[str, int]) -> None:
		self.configure: Configuration = Configuration()
		self.configure.API_KEY = api_key


	async def __request(self, query: Union[str]) -> Awaitable:
		try:
			async with aiohttp.ClientSession(base_url=self.configure.BASE_URL, headers=self.configure.HEADERS) as session:
				async with session.get(self.configure.API_URL+query) as response:
					return await response.json()
		except BaseException as e:
			print('[Error]:', e)

			
	async def getWeatherByName(
			self,
			*,
			city: Union[str], 
			country: Union[str] = None,
			units: Union[str] = None,
			exclude: Union[str] = None,
			date: Union[str | datetime] = None,
			tz: Union[str] = None,
			lang: Union[str] = Languages.English)-> WeatherData:
		
		"""Get weather by city name"""

		if units is None:
			units = self.configure.units

		if tz is None:
			tz = '+00:00'

		if date is None:
			date = datetime.now().strftime("%Y-%m-%d")

		if exclude is None:
			exclude = self.configure.exclude

		return WeatherData(
			await self.__request(
				f'q={city},{country}&units={units}&exclude={exclude}&date={date}&tz={tz}&lang={lang}&appid={self.configure.API_KEY}'))


	async def getWeatherById(
			self,
			*,
			city_id: Union[str] | int,
			units: Union[str] = None,
			exclude: Union[str] = None,
			date: Union[str | datetime] = None,
			tz: Union[str] = None,
			lang: Union[str] = Languages.English) -> WeatherData:
		
		"""Get weather data by city id"""
		
		if units is None:
			units = self.configure.units

		if tz is None:
			tz = '+00:00'

		if date is None:
			date = datetime.now().strftime("%Y-%m-%d")

		if exclude is None:
			exclude = self.configure.exclude

		return WeatherData(
			await self.__request(
				f'id={city_id}&units={units}&exclude={exclude}&date={date}&tz={tz}&lang={lang} &appid={self.configure.API_KEY}'))
	

	async def getWeatherByCoords(
			self,
			*,
			lat: Union[float] | Union[str],
			lon: Union[float] | Union[str],
			units: Union[str] = None,
			exclude: Union[str] = None,
			date: Union[str | datetime] = None,
			tz: Union[str] = None,
			lang: Union[str] = Languages.English) -> WeatherData:
		
		"""Get weather data by city coords"""
		
		if units is None:
			units = self.configure.units

		if tz is None:
			tz = '+00:00'

		if date is None:
			date = datetime.now().strftime("%Y-%m-%d")

		if exclude is None:
			exclude = self.configure.exclude

		return WeatherData(
			await self.__request(
				f'lat={lat}&lon={lon}&units={units}&exclude={exclude}&date={date}&tz={tz}&lang={lang}&appid={self.configure.API_KEY}'))