from lib.components import getWeatherByName, getWeatherById, getWeatherByCoords
from lib.config import API_KEY
import unittest

class test_getWeatherByName(unittest.IsolatedAsyncioTestCase):
	async def test_call(self):
		self.assertTrue(await getWeatherByName(key=API_KEY, city="Moscow", country='Russian'))
		self.assertTrue(await getWeatherById(key=API_KEY, city_id="524901"))
		self.assertTrue(await getWeatherByCoords(key=API_KEY, lat=33.44, lon=-94.04))
	
	async def test_call_int(self):
		self.assertTrue(await getWeatherById(key=API_KEY, city_id=524901))


if __name__ == "__main__":
	unittest.main()
