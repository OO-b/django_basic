from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import connection
import datetime

# Create your views here.
from django.urls import reverse


def t_login(request):
    if request.method == 'POST':

        return render(request, 't_home.html')
    else:

        return render(request, 't_login.html')


def t_sign_up(request):

    if request.method == 'POST':

        user_id = request.POST['user']
        password = request.POST['password']
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_tel = request.POST['user_tel']
        now = datetime.datetime.now()

        cursor = connection.cursor()
        sql = "insert into m_user (user, password, user_name, user_email, user_tel, user_typ, regi_typ, permit_yn, regi_dt) value (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (user_id, password, user_name, user_email, user_tel, 'U', 'H', 'Y', now))
        cursor.close()

        return render(request, 't_login.html', context={'result':'success'})

    else:
        return render(request, 't_sign_up.html')



