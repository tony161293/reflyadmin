from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'refly_admin.views.home', name='home'),
    url(r'^', include('dashboard.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
