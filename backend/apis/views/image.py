import os
import hashlib
from django.http import Http404, HttpResponse, FileResponse, JsonResponse
from backend_ch1_sec1 import settings
from utils.response import CommonResponseMixin, ReturnCode
from django.views import View


# 被类视图取代前
def image(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        if not os.path.exists(imgfile):
            # return Http404
            response = CommonResponseMixin.wrap_json_response(code=ReturnCode.RESOURCE_NOT_EXISTS)
            return JsonResponse(data=response, safe=False)
        else:
            # data = open(imgfile, 'rb').read()
            # return HttpResponse(content=data, content_type='image/jpg')  # 这两种均可
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')


# 被类视图取代后
class ImageView(View, CommonResponseMixin):
    def get(self, request):
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        if not os.path.exists(imgfile):
            # return Http404()
            response = CommonResponseMixin.wrap_json_response(code=ReturnCode.RESOURCE_NOT_EXISTS)
            return JsonResponse(data=response, safe=False)
        else:
            data = open(imgfile, 'rb').read()
            # return HttpResponse(content=data, content_type='image/jpg')  # 这两种均可
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')

    def post(self, request):
        # files = request.FILES.getlist('test')
        files = request.FILES
        response = []
        print('***' * 30)
        print(files)
        for key, value in files.items():
            content = value.read()
            md5 = hashlib.md5(content).hexdigest()
            path = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
            with open(path, 'wb') as f:
                f.write(content)
            response.append({'name': key, 'md5': md5})
        message = 'post method success.'
        response = self.wrap_json_response(data=response, code=ReturnCode.SUCCESS, message=message)
        return JsonResponse(data=response, safe=False)

    def put(self, request):
        message = 'put method success.'
        # response = utils_response.wrap_json_response(message=message)
        return JsonResponse(data=self.wrap_json_response(message=message), safe=False)

    def delete(self, request):
        md5 = request.GET.get('md5')
        img_name = md5 + '.jpg'
        path = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        if os.path.exists(path):
            os.remove(path)
            message = 'remove success.'
            code = ReturnCode.SUCCESS
        else:
            message = 'file(%s) not found.' % img_name
            code = ReturnCode.RESOURCE_NOT_EXISTS
        response = self.wrap_json_response(code=code, message=message)
        return JsonResponse(data=response, safe=False)


class ImageListView(View, CommonResponseMixin):
    def get(self, request):
        image_files = os.listdir(settings.IMAGES_DIR)
        response_data = []
        for image_file in image_files:
            response_data.append({
                "name": image_file,
                "md5": image_file[:-4]
            })
        response_data = self.wrap_json_response(data=response_data)
        return JsonResponse(data=response_data, safe=False)


def image_text(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        if not os.path.exists(imgfile):
            response = CommonResponseMixin.wrap_json_response(code=ReturnCode.RESOURCE_NOT_EXISTS)
            return JsonResponse(data=response, safe=False)
        else:
            response_data = {}
            response_data['name'] = md5 + '.jpg'
            response_data['url'] = '/service/image?md5=%s' % md5
            response = CommonResponseMixin.wrap_json_response(data=response_data)
            return JsonResponse(data=response, safe=False)

