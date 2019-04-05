from django.conf.urls import include, url
from django.contrib import admin
from courses.views import IndexView, AddressAPI

urlpatterns = [
    # Examples:
    # url(r'^$', 'imooc_orm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^address/(\d+)$', AddressAPI.as_view(), name='address'),
]
