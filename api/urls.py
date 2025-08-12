from django.urls import path,include
# from .views import EmployeeView,EmployeeDetailsView,EmployeeViewUSingGenerics,EmployeeDetailsUsingGenerics
from .views import EmployeeViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("employees",EmployeeViewset,basename="employee")
urlpatterns = [
    # path("employees/",EmployeeView.as_view()),

    # path("employees/<int:pk>/",EmployeeDetailsView.as_view()),
    # path("employees/generics/",EmployeeViewUSingGenerics.as_view()),
    # path("employees/generics/<int:pk>",EmployeeDetailsUsingGenerics.as_view()),
    path("",include(router.urls))
]