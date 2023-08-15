from django.urls import path
from .views import user_registration, user_login

app_name = 'user'

urlpatterns = [
    path('', user_registration, name='Task_View'),
    path('login/', user_login, name="login")
    # path('task/<int:pk>/', TaskRetriveUpdateDeleteView.as_view(), name='Task_Views')
]

