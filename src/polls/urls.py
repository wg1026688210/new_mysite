'''
Created on 2015-10-28

@author: Administrator
'''
from django.conf.urls import url
from . import views
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^query/$', views.QueryView.as_view(), name='query'), 
    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<question_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<question_id>[0-9]+)/selectone/$', views.selectone, name='selectone'),
    url(r'^update/$', views.update, name='update'),
    url(r'^chart/$', views.chart, name='chart'),
    url(r'^tddiv/$', views.tddiv, name='tddiv'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login1/$', views.login1, name='login1'),
    url(r'^tddiv1/$', views.tddiv1, name='tddiv1'),
]