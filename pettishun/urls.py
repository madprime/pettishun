from django.conf.urls import include, url
from django.contrib import admin

from .views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^/?$', HomeView.as_view(), name='home'),
]
