import requests
import json
import datetime as dt
import taosrest


def open_connection():
    # Establish a connection to TDEngine cloud
    # Use the token and URL provided in the instance
    try:
        connection = taosrest.connect(url="https://gw.us-west-2.aws.cloud.tdengine.com", token="fd76c35cada42f1d0ac0001b91f2959c883cbcd6")
    except Exception as e:
        print(str(e))
    return connection

def get_weather_data(location, connection):
    # Set up API call
    payload = {
        "key": "",
        "q": location,
        "aqi": "yes"        # Provides Air Quality Index
    }
    api_url = "http://api.weatherapi.com/v1/current.json"
    response = requests.get(api_url, params=payload)

    # Extract the JSON from the response variable
    response_string = response.json()

    # Take only the current part of the JSON
    current = response_string['current']

    # Fix time format from YYYY-MM-DD hh:mm:ss to -> YYYY-MM-DDThh:mm:ssZ
    origin_time = dt.datetime.strptime(current['last_updated'],'%Y-%m-%d %H:%M') 
    
    #turn datetime into formated string for tdengine
    current['last_updated'] = origin_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Call write_weather to write data to TDEngine
    TODO: write_weather(location, current, connection)

def close_connection(connection):
    connection.close()

def main():
    # Establish connection to TDengine
    connection = open_connection()

    # Get data from the weather API
    # Use Brisbane as the location
    get_weather_data('Brisbane', connection)

    # Close connection
    close_connection(connection)

if __name__ == "__main__":
    main()

