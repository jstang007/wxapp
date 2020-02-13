from django.urls import path
from .views import weather, menu, image, service


urlpatterns = [
    # path('weather_old', weather.weather),
    path('weather', weather.WeatherView.as_view()),
    path('menu', menu.get_menu),
    path('hello', weather.helloworld),
    path('image_old', image.image),  # # 被类视图取代前
    path('image', image.ImageView.as_view()),  # 被类视图取代后
    path('imagetext', image.image_text),
    path('image/list', image.ImageListView.as_view()),
    path('stock', service.stock),
    path('constellation', service.constellation)

]
