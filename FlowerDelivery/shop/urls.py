from django.urls import path
from . import views
from .views import logout_view


urlpatterns = [
    path('', views.index, name='home'),
    path('reg/', views.register, name='register'),
    path('cabinet', views.cabinet, name='cabinet'),
    path('new_order', views.new_order, name='new_order'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]