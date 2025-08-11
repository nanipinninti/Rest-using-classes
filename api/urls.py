from django.urls import path
from .views import EmployeeView,EmployeeDetailsView
urlpatterns = [
    path("employees/",EmployeeView.as_view()),

    path("employees/<int:pk>/",EmployeeDetailsView.as_view())
]