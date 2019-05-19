from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import include, url
from dejavu.views import DayApiView
from dejavu.api.routers import HybridRouter


api_router = HybridRouter()
api_router.add_api_view(
    'days',
    url(r'^days/$', DayApiView.as_view(), name='days')
)

api_urls = [
    url(r'^api/login\/?$', obtain_auth_token),
    url(
        r'^api/auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    url(r'^api/', include(api_router.urls)),
]
