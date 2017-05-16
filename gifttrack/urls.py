from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/', views.user_page, name='user_page'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login_user, name='login_user'),
    url(r'^logout/', views.logout_user, name='logout_user'),
    url(r'^list/(?P<list_id>[0-9]+)/$', views.gift_listing, name='gift_listing')
]
