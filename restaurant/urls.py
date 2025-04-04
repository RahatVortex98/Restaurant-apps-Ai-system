from .views import index,order,order_details,user_login,user_logout

from django.urls import path
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',index,name="index"),
    path('order/<int:pk>/',order,name='order'),
    path('details/',order_details, name='details'),
    path('login/',user_login, name='login'),
    path('logout/',user_logout, name='logout'),

    


    
]



