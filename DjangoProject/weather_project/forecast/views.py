import requests
from django.shortcuts import render

def home(request):
    api_key = "f5582ac2f5b165bb70619f415d41d87f"
    cities = ["London", "Johannesburg"]

    # Map weather condition keywords to GIF URLs
    gifs = {
        'clear': 'forecast/clear.gif',
        'clouds': 'forecast/cloudy.gif',
        'rain': 'forecast/rainy.gif',
        'snow': 'forecast/snow.gif',
        'sunny': 'forecast/sunny.gif',
    }

    # Map city to flag
    flags = {
        'London': '🇬🇧',
        'Johannesburg': '🇿🇦'
    }

    # Map condition to emoji and tip
    condition_info = {
        'Clear': {'emoji': '🌞', 'tip': 'Wear sunglasses 😎'},
        'Sunny': {'emoji': '🌞', 'tip': 'Drink water 💧'},
        'Clouds': {'emoji': '☁️', 'tip': 'Light jacket recommended 🧥'},
        'Rain': {'emoji': '🌧️', 'tip': 'Bring a raincoat ☔'},
        'Snow': {'emoji': '❄️', 'tip': 'Wear warm clothes 🧣🧤'}
    }

    weather_list = []

    for city in cities:
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            data = requests.get(url).json()
            condition_raw = data['weather'][0]['main']

            # Normalize condition for GIF
            condition_lower = condition_raw.lower()
            if 'clear' in condition_lower or 'sun' in condition_lower:
                key = 'sunny'
            elif 'cloud' in condition_lower:
                key = 'clouds'
            elif 'rain' in condition_lower or 'drizzle' in condition_lower:
                key = 'rain'
            elif 'snow' in condition_lower:
                key = 'snow'
            else:
                key = 'sunny'

            # Get condition emoji and tip
            info = condition_info.get(condition_raw, {'emoji': '🌤️', 'tip': ''})

            # Determine temperature emoji
            temp = data['main']['temp']
            if temp < 10:
                temp_emoji = '❄️'
            elif temp <= 25:
                temp_emoji = '🌤️'
            else:
                temp_emoji = '☀️'

            # Main weather info
            city_weather = {
                'city': city,
                'flag': flags.get(city, ''),
                'condition': condition_raw,
                'temp': temp,
                'tip': info['tip'],
                'gif_url': gifs[key],
                'temp_emoji': temp_emoji,
                'condition_emoji': info['emoji']
            }

            # Daily forecast mock (Morning, Afternoon, Evening, Night)
            times_of_day = ['Morning', 'Afternoon', 'Evening', 'Night']
            daily_forecast = []
            for time in times_of_day:
                daily_forecast.append({
                    'time': time,
                    'temp': temp,  # same temp for now; replace with real forecast if desired
                    'condition': condition_raw,
                    'tip': info['tip'],
                    'condition_emoji': info['emoji']
                })
            city_weather['daily_forecast'] = daily_forecast

            weather_list.append(city_weather)

        except Exception as e:
            # Fallback in case API fails
            weather_list.append({
                'city': city,
                'flag': flags.get(city, ''),
                'condition': 'Unknown',
                'temp': 'N/A',
                'tip': '',
                'gif_url': gifs['sunny'],
                'temp_emoji': '🌤️',
                'condition_emoji': '🌤️',
                'daily_forecast': []
            })

    context = {'weather_list': weather_list}
    return render(request, 'forecast/home.html', context)
