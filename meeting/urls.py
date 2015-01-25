from django.conf.urls import patterns, url

from meeting import views

urlpatterns = patterns('', 
  url(r'^index/', views.index, name='index'),
  url(r'^start/', views.meeting_start, name='start'),
  url(r'^content/', views.index, name='record'),
  url(r'^end/', views.index, name='end'),
  url(r'^content-sync/', views.index, name='content_synch'),
)
