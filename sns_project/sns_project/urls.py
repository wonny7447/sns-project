from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showmain, name="showmain"),
    path('history/', views.history, name="history"),
    path('like/', views.like, name="like"),
    path('qna/', views.qna, name="qna"),
    path('<str:id>', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
]