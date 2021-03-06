from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from quickstart import views


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_rest_tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('snippets.urls')),
    # url(r'^auth/', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls',
    #                            namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
