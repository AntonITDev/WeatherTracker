from lib.components import getWeatherByName, getWeatherById, getWeatherByCoords
from lib.config import API_KEY
import unittest

class test_getWeatherByName(unittest.IsolatedAsyncioTestCase):
	async def test_call(self):
		self.assertIsNone(await getWeatherByName(key=API_KEY, city="Moscow", country='Russian'))
		self.assertIsNone(await getWeatherById(key=API_KEY, lat=33.44, lon=-94.04))
		self.assertIsNone(await getWeatherByCoords(key=API_KEY, lat=33.44, lon=-94.04))


if __name__ == "__main__":
	unittest.main()
