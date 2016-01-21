from django.conf.urls import url, patterns
from register import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^add_category/$', views.add_category, name='add_category'),)
