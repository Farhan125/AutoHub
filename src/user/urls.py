from django.urls import include, path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    # path("", views.login, name="login"),
    path("user/", include("user.urls")),
]