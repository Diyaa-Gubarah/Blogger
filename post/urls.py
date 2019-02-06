from django.conf.urls import url
from . import views

app_name = 'post'

urlpatterns = [
    url(r'^posts/$', views.PostList.as_view(), name='post_list'),
    url(r'^group/(?P<slug>[-\w]+)/add/new_post$', views.CreatePost.as_view(), name='add_post'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.PostDetail.as_view(), name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/update/$',views.UpdatePost.as_view(), name='post_update'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$',views.DeletePost.as_view(), name='post_delete'),
    url(r'^post/(?P<pk>[0-9]+)/like/$',views.LikePost, name='like_post'),
    url(r'^post/(?P<pk>[0-9]+)/dislike/$',views.disLikePost, name='dislike_post'),

]
