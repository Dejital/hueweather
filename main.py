import time
from phue import Bridge
from pyowm import OWM

from config import *

xys = {}
xys["thunderstorm"] = ([0.245, 0.1403], [0.465, 0.4524])
xys["drizzle"] = ([0.215, 0.2446], [0.3626, 0.2549])
xys["rain"] = ([0.1896, 0.1533], [0.3765, 0.2862])
xys["snow"] = ([0.2038, 0.3066], [0.32, 0.331])
xys["atmosphere"] = ([0.3364, 0.2148], [0.3642, 0.4265])
xys["clear"] = ([0.4069, 0.312], [0.4044, 0.4087])
xys["clouds"] = ([0.375, 0.3873], [0.3365, 0.3521])
xys["heat"] = ([0.521, 0.318], [0.4045, 0.4088])
xys["decent"] = ([0.4398, 0.3823], [0.4045, 0.4088])
xys["cold"] = ([0.2876, 0.35], [0.4045, 0.4088])

def get_weather():
    owm = OWM(OWM_API_KEY)
    mgr = owm.weather_manager()
    obs = mgr.one_call(LAT_LON[0], LAT_LON[1])
    print('Weather is ' + obs.current.detailed_status)
    return obs.current.weather_code

def get_feelslike():
    owm = OWM(OWM_API_KEY)
    mgr = owm.weather_manager()
    obs = mgr.one_call(LAT_LON[0], LAT_LON[1])
    temp = obs.current.temperature('fahrenheit').get('feels_like')
    return temp

def get_hue():
    b = Bridge(HUE_ADDRESS)
    l = b.get_light(LEFT_BULB, 'xy')
    r = b.get_light(RIGHT_BULB, 'xy')
    print('(' + str(l) + ', ' + str(r) + ')')

def set_hue(key):
    tup = xys[key]
    b = Bridge(HUE_ADDRESS)
    b.set_light(LEFT_BULB, 'xy', value=tup[0])
    b.set_light(RIGHT_BULB, 'xy', value=tup[1])

def bulbs_are_alive():
    b = Bridge(HUE_ADDRESS)
    return b.get_light(LEFT_BULB, 'on') and b.get_light(RIGHT_BULB, 'on')

def set_hue_by_weather():
    if not bulbs_are_alive():
        print('Bulbs are not turned on')
        return
    # docs: https://openweathermap.org/weather-conditions
    wc = get_weather()
    if 200 <= wc < 300:
        set_hue('thunderstorm')
    elif 300 <= wc < 500:
        set_hue('drizzle')
    elif 500 <= wc < 600:
        set_hue('rain')
    elif 600 <= wc < 700:
        set_hue('snow')
    elif 700 <= wc < 800:
        set_hue('atmosphere')
    else:
        temp = get_feelslike()
        if temp > 75:
            set_hue('heat')
        elif temp < 55:
            set_hue('cold')
        else:
            set_hue('decent')

if __name__ == '__main__':
    while True:
        set_hue_by_weather()
        time.sleep(900) # seconds

