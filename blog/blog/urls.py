from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index16/', index16),
    path('index17/', index17),
    path('index18/', index18),
    path('index19/', index19),
    path('index20/', index20),
    path('index21/', index21),
    path('index22/', index22),
    path('index23/', index23),
    path('index24/', index24),
    path('index25/', index25),
    path('index50/', index50),
    path('index51/', index51),
    path('index52/', index52),
    path('index53/', index53),
    path('index54/', index54),
    path('index55/', index55)
]
