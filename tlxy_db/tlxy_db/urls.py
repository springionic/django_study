from django.conf.urls import include, url
from django.contrib import admin
from rlt import views as v

urlpatterns = [
    # Examples:
    # url(r'^$', 'tlxy_db.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^one/', v.one),
    url(r'^two/', v.two),
    url(r'^three/', v.three),
    url(r'^four/', v.four),
    url(r'five/', v.five),
    url(r'five_post/', v.five_post),
]
