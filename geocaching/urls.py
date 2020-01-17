from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.index, name='index'),
        path('accounts/', include('django.contrib.auth.urls')),
        path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    ]
