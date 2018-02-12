from django.conf.urls import url
from . import views
from . import views as core_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^new_question/$', views.new_question, name='new_question'),
    url(r'^question/(?P<pk>\d+)/$', views.question_detail, name='question_detail'),
    url(r'^all_questions$', views.all_questions, name='all_questions'),
    url(r'^delete_question$', views.delete_question, name='delete_question'),
    url(r'^statement_input/(?P<statement>\d)/$', views.statement_input, name='statement_input'),
    url(r'^score$', views.score, name='score'),
    url(r'^scoresheet/(?P<pk>\d+)/$', views.scoresheet, name='scoresheet'),
]
