from .models import UserInfo
from .forms import UserInfoForm
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, DetailView, ListView


class Home(TemplateView):
    template_name = 'screen_live.html'


class UserFormView(CreateView):
    model = UserInfo
    template_name = 'new_user_registration.html'
    form_class = UserInfoForm

    def post(self, request, *args, **kwargs):
        form = UserInfoForm(request.POST)
        if form.is_valid():
            data = form.save()
            data.save()
            return redirect('home')


class UserListView(ListView):
    model = UserInfo
    template_name = 'users_listview.html'


class UserDetailView(DetailView):
    model = UserInfo
    template_name = 'users_data_details.html'
