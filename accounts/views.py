from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import LoginUserForm, RegisterUserForm
from .utils import DataMixin
from .models import CustomUser

def me_user(request):
    users = CustomUser.objects.all()
    return render(request, 'lk.html', context={'users': users})

def me_admin(request):
    return render(request, "lkadmin.html")

def lower_criteria(request):
    return render(request, "kriterii3.html")

def themes(request):
    return render(request, "scroll.html")

def bids_detail(request):
    return render(request, "ozenka.html")

def bids_mark(request):
    return render(request, "bids-mark.html")

def printed_editions(request):
    return render(request, "kriterii.html")

def information_publications(request):
    return render(request, "kriterii2.html")

def end(request):
    return render(request, "finish.html")

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'zayavka1.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login1.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('account_user')

class logout_user(LogoutView):
    def logout_user(self, request):
        logout(request)
        return redirect('logout')

