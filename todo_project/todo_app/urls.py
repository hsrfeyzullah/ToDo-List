#genel url den buaya istek yapıcam buraya gelen istekleri de gerekli yere yönlendireceğim
from django.urls import path, include
from .import views
urlpatterns = [
    path('index/', views.index, name="index"),
    path('', views.login_view, name="login"),   
    path('about/', views.about, name="about"),
    path('create/', views.create, name="create"),
    path('delete/<ToDos_id>', views.delete, name="delete"),
    path('update/<ToDos_id>', views.update, name="update"),
    path('yes_finish/<ToDos_id>', views.yes_finish, name="yes_finish"),
    path('no_finish<ToDos_id>', views.no_finish, name="no_finish"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    
]
