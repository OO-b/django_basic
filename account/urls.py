from django.urls import path

import account
from . import views


app_name = "account"

urlpatterns = [
    path('t_login/', views.t_login, name="t_login"),
    path('t_sign_up/', views.t_sign_up, name="t_sign_up"),

]