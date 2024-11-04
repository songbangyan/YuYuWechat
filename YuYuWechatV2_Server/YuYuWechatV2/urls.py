

from django.contrib import admin
from django.urls import path, include
from wechat_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('wechat/', include('wechat_app.urls')),
    path('', views.home, name='home'),

]