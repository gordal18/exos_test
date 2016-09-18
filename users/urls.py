from django.conf.urls import url
from users import views

urlpatterns = [
  url(r'^$', views.UserList.as_view(), name='user_list'),
  url(r'^new$', views.UserCreate.as_view(), name='user_new'),
  url(r'^(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user_detail'),
  url(r'^(?P<pk>[0-9]+)/edit/$', views.UserUpdate.as_view(), name='user_edit'),
  url(r'^(?P<pk>[0-9]+)/delete/$', views.UserDelete.as_view(), name='user_delete'),
  url(r'^download$', views.download, name='download_list'),
]