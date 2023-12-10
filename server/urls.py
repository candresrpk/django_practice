from django.contrib import admin
from django.urls import path, include
from .views import homeView, aboutView
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('about/', aboutView, name='about'),
    path('books/', include('books.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
