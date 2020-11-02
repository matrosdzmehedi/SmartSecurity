from django.urls import path
from .views import Home, CreatUserForm, UserListView, UserDetailView

#from .views import Home,CvDetailView,CvCreateView,CvListView,CvDeleteView,ChartData,ChartDataAge

urlpatterns = [

    path('',Home.as_view(),name='home'),
    path('user-create/',CreatUserForm.as_view(),name='createuser'),
    path('user-list/',UserListView.as_view(),name='users_listview'),
    path('users_details/<str:slug>/', UserDetailView.as_view(), name='users_data_details'),
]
