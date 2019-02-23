from django.conf.urls import url,include

from . import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'api/posts', views.PostViewSet)
router.register(r'api/comments', views.CommentViewSet)
router.register(r'api/likes', views.LikeViewSet)

app_name = 'post'

urlpatterns = [
    url(r'^posts/$', views.PostList.as_view(), name='post_list'),
    url(r'^group/(?P<slug>[-\w]+)/add/new_post$',
        views.CreatePost.as_view(), name='add_post'),
    url(r'^post/(?P<pk>[0-9]+)/$',
        views.PostDetail.as_view(), name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/update/$',
        views.UpdatePost.as_view(), name='post_update'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$',
        views.DeletePost.as_view(), name='post_delete'),
    url(r'^post/(?P<pk>[0-9]+)/like/$', views.LikePost, name='like_post'),
    url(r'^post/(?P<pk>[0-9]+)/dislike/$',
        views.disLikePost, name='dislike_post'),
    url(r'^post/(?P<pk>[0-9]+)/add/comment/$',
        views.CommentCreate.as_view(), name='create_comment'),
    url(r'^comment/(?P<pk>[0-9]+)/update/$',
        views.CommentUpdate.as_view(), name='update_comment'),
    url(r'^comment/(?P<pk>[0-9]+)/delete/$',
        views.CommentDelete, name='delete_comment'),

    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
