from django.contrib import admin
from django.urls import path, include
from myapp.views import data_view, test_view, page1_view, page2_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', data_view, name='data'),
    path('', data_view, name='home'),  # Это перенаправляет корневой URL на data_view
    path('test/', test_view, name='test'),
    path('page1/', page1_view, name='page1'),
    path('page2/', page2_view, name='page2'),
    path('news/', include('news.urls'))
]
