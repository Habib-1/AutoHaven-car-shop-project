from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register.as_view(),name="register"),
    path('logout/',views.logout,name='logout'),
    path('login/',views.login.as_view(),name='login'),
    path('profile/',views.profile.as_view(),name='profile'),
    path('edit_profile/<int:pk>/',views.edit_profile.as_view(),name='edit_profile'),
    path('password_change/',views.change_pass.as_view(),name='change_pass'),
    path('product_purchase/<int:pk>/',views.buy_now,name='buy_now'),
]