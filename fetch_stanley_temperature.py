import requests
import time
from datetime import datetime

def get_today_date():
    # return datetime.now().strftime('%Y%m%d')
    return '20240616'

def get_current_temperature_data(station_code, date):
    url = 'https://data.weather.gov.hk/weatherAPI/opendata/opendata.php'
    params = {
        'dataType': 'RYES',
        'date': date,
        'lang': 'en',
        'station': station_code
    }

    response = requests.get(url, params=params)
    try:
        data = response.json()
        if 'StanleyLocationName' in data and 'StanleyMaxTemp' in data and 'StanleyMinTemp' in data and 'ReportTimeInfoDate' in data:
            return {
                'ReportTimeInfoDate': data['ReportTimeInfoDate'],
                'StanleyLocationName': data['StanleyLocationName'],
                'StanleyMaxTemp': data['StanleyMaxTemp'],
                'StanleyMinTemp': data['StanleyMinTemp']
            }
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
    
    return None

def main():
    last_data = None
    
    while True:
        today_date = get_today_date()
        current_data = get_current_temperature_data('STY', today_date)
        
        if current_data is not None:
            if last_data is None:
                print(f"Current temperature: 'StationName: {current_data['StanleyLocationName']}', Date: {current_data['ReportTimeInfoDate']}, MaxTemp: {current_data['StanleyMaxTemp']}, MinTemp: {current_data['StanleyMinTemp']}")
            elif current_data != last_data:
                print(f"Current temperature: 'StationName: {current_data['StanleyLocationName']}', Date: {current_data['ReportTimeInfoDate']}, MaxTemp: {current_data['StanleyMaxTemp']}, MinTemp: {current_data['StanleyMinTemp']}")
            
            last_data = current_data
        
        time.sleep(3600)

if __name__ == "__main__":
    main()
