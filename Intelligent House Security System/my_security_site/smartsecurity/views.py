from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, DetailView,ListView
################
from .models import UserRegistration
from .forms import UserForm
#####################

# Create your views here.
class Home(TemplateView):
    template_name = 'screen_live.html'

class CreatUserForm(CreateView):
    model = UserRegistration
    template_name = 'new_user_registration.html'
    form_class= UserForm

    def post(self,request,*args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('users_listview')

class UserListView(ListView):
    model = UserRegistration
    template_name = 'users_listview.html'


class UserDetailView(DetailView):
    model = UserRegistration
    template_name = 'users_data_details.html'
