# Phillips Hue Weather Indicator for Two Bulbs

## Introduction

This service indicates the current weather conditions and/or temperature on two Phillips Hue 
color light bulbs. This is accomplished via integration of the Phillips Hue API (`phue` package) 
and Open Weather Map API (`pyowm` package).

At this point this is not particularly portable, and is specific to my use case and my color preferences. 
However it can easily be repurposed to your own implementation.

This project is inspired by [friedmud/hue_weather](https://github.com/friedmud/hue_weather).

## Requirements

- Phillips Hue bridge and two light bulbs
- A machine/server to host this service on your local network
- A free API key from Open Weather Map
- Docker
- Python 3

## Running

This application runs in a Docker container on my home server. It must be on the same local network as the
Phillips Hue bridge.

To configure the service, create a `config.py` file containing the following settings.

    HUE_ADDRESS = '192.168.1.113'
    LEFT_BULB = 'Left Bulb'
    RIGHT_BULB = 'Right Bulb'
    OWM_API_KEY = 'Open Weather Map free api key'
    LAT_LON = (123, 321) # Location address for weather forecast
    SLEEP_TIME = 900  # In seconds

To allow the service to authenticate with the Phillips Hue bridge in your home, 
you need to generate a `.python_hue` file using the `phue` package. It's really simple.
Please see the docs for `phue` for more information.

The following command will build the docker container and execute the script.

    docker-compose up --build
