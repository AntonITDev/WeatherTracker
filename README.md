# WeatherTracker
Module for tracking weather on Python.

-------------------------------------------------------------------------------------------------------------------

Using API: "https://api.openweathermap.org" methodds: "/data/2.5/weather".

For work with the module, you need to register in the service and create your own API key.

If need search exact city, we can use "https://openweathermap.org/find?q=", after "q" need write title of the city.

-------------------------------------------------------------------------------------------------------------------

Current weather and forecasts:
  minute forecast for 1 hour
  hourly forecast for 48 hours
  daily forecast for 8 days

Supporting the following languages. To select one, you can use the corresponding language code:
  af Afrikaans
  al Albanian
  ar Arabic
  az Azerbaijani
  bg Bulgarian
  ca Catalan
  cz Czech
  da Danish
  de German
  el Greek
  en English
  eu Basque
  fa Persian (Farsi)
  fi Finnish
  fr French
  gl Galician
  he Hebrew
  hi Hindi
  hr Croatian
  hu Hungarian
  id Indonesian
  it Italian
  ja Japanese
  kr Korean
  la Latvian
  lt Lithuanian
  mk Macedonian
  no Norwegian
  nl Dutch
  pl Polish
  pt Portuguese
  pt_br Português Brasil
  ro Romanian
  ru Russian
  sv, se Swedish
  sk Slovak
  sl Slovenian
  sp, es Spanish
  sr Serbian
  th Thai
  tr Turkish
  ua, uk Ukrainian
  vi Vietnamese
  zh_cn Chinese Simplified
  zh_tw Chinese Traditional
  zu Zulu

-------------------------------------------------------------------------------------------------------------------

Documentation:

getWeatherByName(
		token: int | str, --> API_KEY
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

 def getWeatherById(
		token: int | str, --> API_KEY
		city_id: str,
		units: str = 'metric',
		exclude: str = 'current',
		tz: str = '+03:00',
		date: str = date.today().strftime("%Y-%m-%d"),
		lang:str = 'en') -> Any:
	
	'''Weather city by id
	
	units: ['metric', 'standard', 'imperial']
	exclude: ['current','minutely','hourly', 'daily','alert']
	
	'''

-------------------------------------------------------------------------------------------------------------------

Errors list:
