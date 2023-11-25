from django.contrib import admin
from django.urls import path, include
from .views import homeView, aboutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('about/', aboutView, name='about'),
    path('books/', include('books.urls'))
]
