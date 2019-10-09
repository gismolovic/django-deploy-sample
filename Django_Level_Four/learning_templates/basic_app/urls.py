from django.urls import path
from basic_app import views

# Temaplte Tagging
app_name = 'basic_app_test'

urlpatterns = [
    path('relative/', views.relative,name='relative'),
    path('other/', views.other,name='other'),
]
