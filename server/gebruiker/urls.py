from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('gebruiker/checkUser/',views.checkUser),
    path('gebruiker/changePSW/<int:id>',views.changePSW),
    path('admin/getAll/',views.getAll),
    path('admin/addUser/',views.addUser),
    path('admin/delUser/<int:id>',views.delUser),
    path('admin/updateUser/<int:id>',views.updateUser),
]
