from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/', views.user_page, name='user_page'),
    url(r'^create/', views.create, name='create'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login_user, name='login_user'),
    url(r'^logout/', views.logout_user, name='logout_user')
]
