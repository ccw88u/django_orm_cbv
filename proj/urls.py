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
]