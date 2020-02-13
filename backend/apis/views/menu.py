import os
from backend_ch1_sec1 import settings
import yaml
import utils.response as utils_response
from django.http import JsonResponse


def init_app_data():
    date_file = os.path.join(settings.BASE_DIR, 'app.yaml')
    with open(date_file, 'r', encoding='utf-8') as f:
        apps = yaml.load(f)
        return apps


def get_menu(request):
    global_app_data = init_app_data()
    # publish_app_data = global_app_data['published']
    publish_app_data = global_app_data.get('published')
    response = utils_response.wrap_json_response(data=publish_app_data, code=utils_response.ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False, json_dumps_params={'ensure_ascii': False})



