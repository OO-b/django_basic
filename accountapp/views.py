from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

@login_required
def hello_world(request):

    # if request.user.is_authenticated: #로그인 되어있는경우

        if request.method == "POST":

            temp = request.POST.get('hello_world_input')

            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            hello_world_list = HelloWorld.objects.all()
            return HttpResponseRedirect(reverse('accountapp:hello_world'))

        else:

            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/helloworld.html', context={'hello_world_list': hello_world_list})

    # else: #로그인이 안되어 있는 경우
    #     return HttpResponseRedirect(reverse('accountapp:login'))


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #성공 후 어느경로로 재 연결?
    # reverse / reverse_lazy
    # reverse는 클래스에서 사용할 수 없음
    template_name = 'accountapp/create.html' #회원가입시 보여줄 form 어느 html 파일을 통해 보여줄지


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
# 일반 function에 사용하는 decorator를 method에 사용하도록 하는 decorator
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'

    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'