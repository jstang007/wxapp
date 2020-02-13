import requests
from urllib import parse
import json


def weather(cityname):
    host = 'https://ali-weather.showapi.com'
    path = '/area-to-weather'
    appcode = '1a2a9d56ff584bb78423d5f4090e56a8'
    qs = parse.urlencode({'area': cityname})
    querys = qs + '&need3HourForcast=0&needAlarm=0&needHourData=0&needIndex=0&needMoreDay=0'
    url = host + path + '?' + querys

    headers = {
        'Authorization': 'APPCODE ' + appcode
    }
    request = requests.get(url, headers=headers)
    request.encoding = 'utf-8'
    response = request.text
    json_data = json.loads(response)
    apidetail = json_data['showapi_res_body']['now']['aqiDetail']
    nodes = json_data['showapi_res_body']['now']
    result = dict()
    result['temperature_time'] = nodes['temperature_time']
    result['area'] = apidetail['area']
    result['quality'] = apidetail['quality']
    result['weather'] = nodes['weather']
    result['temperature'] = nodes['temperature']
    return result
#
# # #
# if __name__ == '__main__':
#     data = weather('深圳')
#     print(data)



