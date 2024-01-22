from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='home'),
    path("short/",views.shortid,name='short_id'),
    path("add_url/",views.add_url,name='add_url'),
    path("redirect/",views.redirect_url,name='redirect_url'),


    path("login/",views.login_view,name='login'),
    path("signup/",views.register_view,name='register'),
    path("logout/",views.logout_view,name='logout')
    

]