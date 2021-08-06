from django.conf.urls import url
from .views import authenticate_user, users_list, user_detail

urlpatterns = [
    url(r'^users/obtain_token$', authenticate_user),
    url(r'^users/$', users_list),
    url(r'^users/(?P<pk>[0-9]+)$', user_detail)
]