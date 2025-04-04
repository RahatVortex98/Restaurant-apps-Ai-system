from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.http import HttpResponse
from django.urls import path,include
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('restaurant.urls')),
    path('',include('contact.urls')),


    path('robots.txt', serve, {'path': 'robots.txt', 'document_root': settings.STATIC_ROOT}),


    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'restaurant.views.error_404_view'