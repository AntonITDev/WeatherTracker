from aiogram.types import Message
from time import perf_counter
from typing import Any, Dict


class BaseModel:
	def __init__(self, data: Dict[str, Any]):
		for key in data:
			setattr(self, key, data[key])

	def __repr__(self):
		return f'{self.__class__.__name__}({self.__dict__})'

class Wind(BaseModel): 
	"""
	Wind data
	"""
	speed: float
	deg: int
	gust: float

class Clouds(BaseModel): 
	"""
	Clouds data
	"""
	all: int

class Coords(BaseModel):
	"""
	Coordinates
	"""
	lon: float
	lat: float

class Sys(BaseModel): 
	"""
	Sys data
	"""
	type: int
	id: int
	country: str
	sunrise: int
	sunset: int

class Temperature(BaseModel):
	"""
	Temperature
	"""
	temp: float
	feels_like: float
	temp_min: float
	temp_max: float
	pressure: int
	humidity: int
	sea_level: int
	grnd_level: int

class Weather(BaseModel):
	"""
	Weather
	"""
	id: int
	main: str
	description: str
	icon: str

class WeatherData(BaseModel):
	"""
	Weather data
	"""

	base: str
	visibility: int
	dt: int
	timezone: int
	name: str
	cod: int

	def __init__(self, data: Dict[str, Any]):
		super().__init__(data)

		self.weather: Weather = Weather(data['weather'][0])
		self.coord: Coords = Coords(data['coord'])
		self.wind: Wind = Wind(data['wind'])
		self.clouds: Clouds = Clouds(data['clouds'])
		self.sys: Sys = Sys(data['sys'])
		self.main: Temperature = Temperature(data['main'])