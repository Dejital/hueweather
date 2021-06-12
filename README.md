## Run

You will need a config.py file created

    HUE_ADDRESS = '192.168.1.113'
    LEFT_BULB = 'Left Bulb'
    RIGHT_BULB = 'Right Bulb'
    OWM_API_KEY = 'Open Weather Map free api key'
    LAT_LON = (123, 321) # Location address for weather forecast
    SLEEP_TIME = 900  # In seconds

The following command will build the docker container and execute the script.

    docker-compose up --build
