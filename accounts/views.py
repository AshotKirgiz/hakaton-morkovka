from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import LoginUserForm, RegisterUserForm
from .utils import DataMixin


def me(request):
    return render(request, "lk.html")

def me_admin(request):
    return render(request, "lkadmin.html")

def redirect_login(request):
    return render(request, "loginlogin.html")

def themes(request):
    return render(request, "themes.html")

def bids_detail(request):
    return render(request, "bids-details.html")

def bids_mark(request):
    return render(request, "bids-mark.html")

def printed_editions(request):
    return render(request, "bids-print.html")

def information_publications(request):
    return render(request, "bids-info.html")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'zayavka.html'
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
        return reverse_lazy('account')

class logout_user(LogoutView):
    def logout_user(self, request):
        logout(request)
        return redirect('logout')

