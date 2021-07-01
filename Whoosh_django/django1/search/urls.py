from . import views
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'), #  = http://127.0.0.1:8000/
    path('search_result/', views.search_result, name='search_result'),
    path('search_result/detail/', views.detail, name='detail')

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#<int:pk>