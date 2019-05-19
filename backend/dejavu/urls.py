from django.contrib import admin
from django.conf.urls import include, url
from dejavu.api.urls import api_urls


urlpatterns = api_urls + [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
]
