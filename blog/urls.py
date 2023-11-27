from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.helloView),
    path('now_date/', views.nowdate_view),
    path('goodby/', views.goodbyView),
]