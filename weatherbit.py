import requests
import json
import sys

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    k = "e16d19d7d9d64ae29a53de24c6f6a73f"
    lat = "39.670814"
    lon = "-86.151560"
    #req = "https://api.weatherbit.io/v2.0/current?lat=" + lat + "&lon=" + lon + "&key=" + k

    payload = {"lat": lat, "lon": lon, "key": k}

    r = requests.get("https://api.weatherbit.io/v2.0/current", payload)

    print(r.content)

    wxData = json.loads(r.content)
    print("Apparent Temp (F): ")
    print(celsius_to_fahrenheit(wxData['data'][0]['app_temp']))
    print("Actual Temp(F): ")
    print(celsius_to_fahrenheit(wxData['data'][0]['temp']))
    print("Dewpoint(F): ")
    print(celsius_to_fahrenheit(wxData['data'][0]['dewpt']))
    print("Wind Direction: ")
    print(wxData['data'][0]['wind_cdir_full'])
    print("Wind Speed: ")
    print(wxData['data'][0]['wind_spd'])

if __name__ == '__main__':
    main()
