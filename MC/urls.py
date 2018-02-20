from django.conf.urls import url
from . import views
from . import views as core_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^resources/$', views.resources, name='resources'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^question/(?P<pk>\d+)/$', views.question_detail, name='question_detail'),
    url(r'^mycheckup$', views.mycheckup, name='mycheckup'),
    url(r'^statement_input/(?P<statement>\d)/(?P<edit>\d+)/$', views.statement_input, name='statement_input'),
    url(r'^statement_help/(?P<state>\d)/(?P<edits>\d+)/$',views.statement_help,name='statement_help'),
    url(r'^score$', views.score, name='score'),
    url(r'^scoresheet/(?P<pk>\d+)/$', views.scoresheet, name='scoresheet'),
]
