from django.urls import path
from product import views
urlpatterns = [
    path('',views.home,name='home'),
    path('category/<slug:slug>/',views.shop,name='by_category'),
    path('details/<int:pk>/',views.product_details.as_view(),name='details'),
    path('shop/',views.shop,name='shop'),
    path('add_comment/<int:pk>/',views.add_comment.as_view(),name='add_comment'),
]
