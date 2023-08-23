from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('<int:task_id>', views.task, name='task'),
    path('sign-up', views.sign_up, name="sign_up"),
    path('create-ticket', views.create_ticket, name="create_ticket"),
    path('history-report', views.history_report, name="history_report"),
]