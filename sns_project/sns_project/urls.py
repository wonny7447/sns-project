from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showmain, name="showmain"),
    path('history/', views.history, name="history"),
    path('like/', views.like, name="like"),
]