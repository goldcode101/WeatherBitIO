import requests
import json
import sys
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv('WEATHERBIT_API_KEY')
DEFAULT_LAT = os.getenv('DEFAULT_LAT', '39.670814')
DEFAULT_LON = os.getenv('DEFAULT_LON', '-86.151560')


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    # Debug: Print environment variables (safely)
    print("=== Debug Information ===")
    print(f"API Key exists: {bool(API_KEY)}")
    print(f"API Key starts with: {API_KEY[:5] if API_KEY else 'None'}")
    print(f"Using latitude: {DEFAULT_LAT}")
    print(f"Using longitude: {DEFAULT_LON}")

    payload = {
        'key': API_KEY,
        'lat': DEFAULT_LAT,
        'lon': DEFAULT_LON,
    }

    print("\n=== Request Information ===")
    print(f"Making request to: https://api.weatherbit.io/v2.0/current")
    print(f"With payload (excluding key): lat={DEFAULT_LAT}, lon={DEFAULT_LON}")

    try:
        r = requests.get("https://api.weatherbit.io/v2.0/current", payload)
        r.raise_for_status() # Raise an exception for bad status codes

        wxData = r.json()
        print(f"Apparent Temp (F): {celsius_to_fahrenheit(wxData['data'][0]['app_temp']):.1f}")
        print(f"Actual Temp(F): {celsius_to_fahrenheit(wxData['data'][0]['temp']):.1f}")
        print(f"Dewpoint(F): {celsius_to_fahrenheit(wxData['data'][0]['dewpt']):.1f}")
        print(f"Wind Direction: {wxData['data'][0]['wind_cdir_full']}")
        print(f"Wind Speed: {wxData['data'][0]['wind_spd']:.1f}")
    except requests.exceptions.RequestException as e:
        print(f"\n=== Error Information ===")
        print(f"Error processing weather data: {e}")
        print(f"Response status code: {r.status_code if 'r' in locals() else 'N/A'}")
        print(f"Response text: {r.text if 'r' in locals() else 'N/A'}")
        sys.exit(1)

if __name__ == '__main__':
    main()
