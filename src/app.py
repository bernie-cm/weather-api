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

