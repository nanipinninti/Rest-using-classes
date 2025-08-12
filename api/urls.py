from django.urls import path
from .views import EmployeeView,EmployeeDetailsView,EmployeeViewUSingGenerics,EmployeeDetailsUsingGenerics
urlpatterns = [
    path("employees/",EmployeeView.as_view()),

    path("employees/<int:pk>/",EmployeeDetailsView.as_view()),
    path("employees/generics/",EmployeeViewUSingGenerics.as_view()),
    path("employees/generics/<int:pk>",EmployeeDetailsUsingGenerics.as_view()),
]