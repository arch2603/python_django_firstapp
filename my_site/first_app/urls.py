from django.urls import path
from . import views

urlpatterns = [
    path('<int:num_page>', views.num_page_view),
    path('simple_view', views.simple_view),
    # path('<str:topic>/', views.news_view),
    path('<int:num1>/<int:num2>', views.add_view),
    path('<str:topic>/', views.news_view, name='topic-page')
    # path('sports/', views.sports_view),
    # path('finance/', views.finance_view)
]