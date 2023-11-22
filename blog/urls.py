from django.urls import path
from . import views
from . import views2
from . import views3

urlpatterns = [
    path('hello/', views.helloView),
    path('now_date/', views2.nowdate_view),
    path('goodby/', views3.goodbyView),
]