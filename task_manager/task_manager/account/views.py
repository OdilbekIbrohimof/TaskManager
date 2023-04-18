from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView, TemplateView, View
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.views import LoginView
from .models import User
from .forms import SimpleUserCreationForm, ProfileEditForm


def register(request):
    form = SimpleUserCreationForm()
    if request.method == 'POST':
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            u = form.save()
            authenticate(u)
            login(request, u)
            return redirect("/")
        else:
            message = "Incorrect username or password!"
            messages.add_message(request, messages.ERROR, message)
            return render(request, "account/register.html", {"form": form})
    return render(request, "account/register.html", {"form": form})


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'img', 'birthday', 'phone_number', 'telegram_link', 'instagram_link', 'facebook_link']
    success_url = '/account/profile/'
    template_name = 'account/profile_edit.html'
