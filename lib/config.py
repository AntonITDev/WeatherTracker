from typing import Dict, Union


class Configuration:
	"""Configuration class for WeatherTracker"""

	
	def __init__(self):
		self.__BASE_URL = 'https://api.openweathermap.org'
		self.__API_URL = '/data/2.5/weather?'
		self.__API_KEY = None
		self.__HEADERS = {
			'User-Agent': 
				'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Config/92.2.2788.20'}
		self.__units = 'metric'
		self.exclude = 'current'


	@classmethod
	def validate(cls, value, *args) -> bool:
		if value is None:
			raise ValueError

		if not isinstance(value, (str, int)):
			raise TypeError

		if args:
			if value not in args:
				raise ValueError

		return value


	@property
	def API_KEY(self):
		return self.__API_KEY
	

	@API_KEY.setter
	def API_KEY(self, value):
		self.validate(value)
		self.__API_KEY = value


	@property
	def API_URL(self):
		return self.__API_URL
	

	@property
	def HEADERS(self):
		return self.__HEADERS
	

	@HEADERS.setter
	def HEADERS(self, headers: Dict[str, str]):
		self.__HEADERS = headers
	

	@property
	def BASE_URL(self):
		return self.__BASE_URL
	

	@property
	def units(self):
		return self.__units


	@units.setter
	def units(self, value: str):
		self.validate(value, *['metric', 'standard', 'imperial'])
		self.__units = value


	@property
	def exclude(self):
		return self.__exclude


	@exclude.setter
	def exclude(self, value: str):
		self.validate(value, *['current','minutely','hourly', 'daily','alert'])
		self.__exclude = value


	def __repr__(self) -> str:
		return str(self.__dict__)
