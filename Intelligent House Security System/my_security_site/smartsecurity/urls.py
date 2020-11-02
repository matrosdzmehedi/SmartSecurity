from django.urls import path
from .views import Home, UserFormView, UserListView, UserDetailView

#from .views import Home,CvDetailView,CvCreateView,CvListView,CvDeleteView,ChartData,ChartDataAge

urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('user-create/', UserFormView.as_view(), name='create_user'),
    path('user-list/', UserListView.as_view(), name='users_listview'),
    path('users_details/<str:slug>/',
         UserDetailView.as_view(), name='users_data_details'),
]
