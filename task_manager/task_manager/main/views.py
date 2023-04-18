from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View, DetailView
from . models import Group

class HomePageView(TemplateView):
  template_name = 'main/index.html'
  
  
class GroupsView(ListView):
  model = Group
  context_object_name = 'groups'
  template_name = 'main/groups.html'