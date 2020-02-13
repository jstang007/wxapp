import requests
from urllib import parse
import utils.response as utils_response

# --------------1 start----------------
url = 'http://127.0.0.1:8000/api/v1.0/service/weather'
body = '{"cities": ["深圳", "广州"]}'
body = body.encode('utf-8')
resp = requests.post(url=url, data=body)
print(resp)
print(resp.text)


# <Response [200]>
# [{"temperature_time": "17:00", "area": "深圳", "quality": "优质", "weather": "阴", "temperature": "30"},
# {"temperature_time": "17:00", "area": "广州", "quality": "优质", "weather": "多云", "temperature": "29"}]
# ---------------1 end-----------------

# # --------------2 start----------------
# url = 'http://127.0.0.1:8000/api/v1.0/service/image?md5=fb713e12db4f62ef6fff790f0e14b920'
# resp = requests.delete(url)
# print(resp)
# print(resp.text)
# # ---------------2 end-----------------
