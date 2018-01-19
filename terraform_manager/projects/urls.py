from django.conf.urls import url
from django.contrib import admin

from .views import (
    project_list,
    project_create,
    project_detail,
    project_update,
    project_delete,
)

urlpatterns = [
    url(r'^$', project_list),
    url(r'^create/$', project_create),
    url(r'^detail/$', project_detail),
    url(r'^update/$', project_update),
    url(r'^delete/$', project_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]

