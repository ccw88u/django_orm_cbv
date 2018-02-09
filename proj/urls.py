# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from proj import views

urlpatterns = [
    ## old way
    #url(r'^$', views.index, name='index')
    ## cbv way
    url(r'^$', views.CBView.as_view()),
    url(r'^viewone$', views.CBV_viewone.as_view()),
    url(r'^go_to_google$', RedirectView.as_view(url='http://www.google.com.tw'), name='go_to_google'),

    ## CBV {S}
    url(r'^companylist$',views.companyListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.companyDetailView.as_view(),name='detail'),
    url(r'^create/$',views.companyCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.companyUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.companyDeleteView.as_view(),name='delete')
    ## CBV {E}
]