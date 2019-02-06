from django.conf.urls import url
from group import views

app_name = 'group'

urlpatterns = [
    url(r'^groups/$', views.GroupList.as_view(), name='group_list'),
    url(r'^group/add/$', views.GroupCreate.as_view(), name='create_group'),
    url(r'^group/(?P<slug>[-\w]+)/update/$',views.GroupUpdate.as_view(), name='group_update'),
    url(r'^group/(?P<slug>[-\w]+)/delete/$',views.GroupDelete.as_view(), name='group_delete'),
    url(r'^group/(?P<slug>[-\w]+)/detail/$',views.GroupDetail.as_view(), name='group_detail'),

    url(r'^join/(?P<slug>[-\w]+)/$', views.JoinGroup.as_view(),name='join_group'),
    url(r'^left/(?P<slug>[-\w]+)/$', views.LeaveGroup.as_view(),name='left_group')
]
