from django.conf.urls import url,include
from group import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'api/groups', views.GroupViewSet)
router.register(r'api/memberships', views.MembershipViewSet)


app_name = 'group'

urlpatterns = [
    url(r'^groups/$', views.GroupList.as_view(), name='group_list'),
    url(r'^group/add/$', views.GroupCreate.as_view(), name='create_group'),
    url(r'^group/(?P<slug>[-\w]+)/update/$',views.GroupUpdate.as_view(), name='group_update'),
    url(r'^group/(?P<slug>[-\w]+)/delete/$',views.GroupDelete.as_view(), name='group_delete'),
    url(r'^group/(?P<slug>[-\w]+)/detail/$',views.GroupDetail.as_view(), name='group_detail'),

    url(r'^join/(?P<slug>[-\w]+)/$', views.JoinGroup.as_view(),name='join_group'),
    url(r'^left/(?P<slug>[-\w]+)/$', views.LeaveGroup.as_view(),name='left_group'),

    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
