def get_weather_animation(weather_main):
    animations = {
        "Clear": "forecast/sunny.gif",    
        "Clouds": "forecast/cloudy.gif",   
        "Rain": "forecast/rainy.gif",      
        "Drizzle": "forecast/rainy.gif",   
        "Snow": "forecast/snow.gif",       
    }

    # Fallback to cloudy if weather type is unknown
    return animations.get(weather_main, "forecast/cloudy.gif")
