from django.contrib import admin
from django.urls import path
import lottoapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lottoapp.views.index, name = 'index'),
    path('result', lottoapp.views.result, name = 'result'),
]
