from fake_useragent import UserAgent

BASE_URL = 'https://api.openweathermap.org'
API_URL = '/data/2.5/weather?'
API_KEY = '4f313a6985d5a650375336a5afbcdb0e'
HEADERS = {'User-Agent': UserAgent().chrome}