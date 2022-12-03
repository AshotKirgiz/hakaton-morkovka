from urllib import request

from django.urls import path
from django.views.generic import RedirectView

from . import views
from .views import *

urlpatterns = [
    path('account/', views.me, name="account"),
    path('account-admin/', views.me_admin, name="account"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user.as_view(), name="logout"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('login/login', views.redirect_login, name="redirect_login"),
    path('bids/', views.themes, name="themes"),
    path('bids/bids-detail', views.bids_detail, name="bidsdv"),
    path('bids/bids-mark', views.bids_mark, name="bidsmk"),
    path('bids/bids-mark/printed-editions', views.printed_editions, name="print"),
    path('bids/bids-mark/information_publications', views.information_publications, name="info")
]

