from django.urls import path
from . import views

urlpatterns = [
    path('simple_view', views.simple_view),
    path('<topic>/', views.news_view)
    # path('sports/', views.sports_view),
    # path('finance/', views.finance_view)
]