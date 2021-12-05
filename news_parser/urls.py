from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('news.urls')),
    path('admin/', admin.site.urls),
    path('contact/', include("contact.urls")),
    path('newsletter/', include('newsletter.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
