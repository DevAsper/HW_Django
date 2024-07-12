from django.urls import path
from .views import data_view, test_view, page1_view, page2_view

urlpatterns = [
    path('', data_view, name='data'),  # Убедитесь, что root URL внутри приложения правильно настроен
    path('data/', data_view, name='data'),
    path('test/', test_view, name='test'),
    path('page1/', page1_view, name='page1'),
    path('page2/', page2_view, name='page2'),
]

