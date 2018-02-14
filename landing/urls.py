from django.conf.urls import url
from landing import views

app_name = "landing"

urlpatterns = [
    url(r'^$',views.DistributorsListView.as_view(),name='list'),
    url(r'^(?P<pk>\d)/$',views.DistributorsDetailView.as_view(),name ='detail'),
    url(r'^create/$', views.DistributorsCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d)/$',views.DistributorsUpdateView.as_view(),name ='update'),
    url(r'^delete/(?P<pk>\d)/$',views.DistributorsDeleteView.as_view(),name ='delete'),
]
