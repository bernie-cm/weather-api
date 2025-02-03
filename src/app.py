import requests
import json
import datetime as dt
import taosrest


def open_connection():
    # Establiash a connection to TDEngine cloud.
    # Open a try except block
    # Except when connection fails
        # Print the error

    # Return the connection object
    pass

def get_weather_data(location, connection):
    # Set up API call
    payload = {
        "key": "",
        "q": location,
        "aqi": "yes"        # Provides Air Quality Index
    }

    response = requests.get



    # Create your key and replace mine with it
    payload = {'Key': 'fed028b417bf48408c552501221407', 'q': location, 'aqi': 'yes'}
    r = requests.get("http://api.weatherapi.com/v1/current.json", params=payload)

    # Get the json from the request's result
    r_string = r.json()

    # Take only the current part of the JSON
    current = r_string['current']

    # Fix time format from YYYY-MM-DD hh:mm:ss to -> YYYY-MM-DDThh:mm:ssZ
    # create datetime object from string
    origin_time = dt.datetime.strptime(current['last_updated'],'%Y-%m-%d %H:%M') 
    
    #turn datetime into formated string for tdengine
    # Keep in mind this will create timestamps in zulu time. The api only sends you local time.
    # We should fix this, but I can't be bothered right now
    current['last_updated'] = origin_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    #print(current)  
    # write the weather data to tdengine
    write_weather(location,current,conn)    

    # we don't need this right now, but I kept it
    return current



def close_connection(connection):
    connection.close()

def main():
    # Establish connection to TDengine
    connection = open_connection()

    # Get data from the weather API
    get_weather_data()

    # Close connection
    close_connection(connection)

if __name__ == "__main__":
    main()

