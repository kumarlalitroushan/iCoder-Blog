from django.contrib import admin
from django.urls import path,include
from corona import views
urlpatterns = [
    path('',views.cindex,name="cindex")
]