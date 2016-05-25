from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', 'blog.views.post_detail', name='post_detail'),
]