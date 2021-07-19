from django.conf.urls import url, include
from users.views import dashboard, register, run_model

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^run_model/", run_model, name="run_model"),
    url(r"^register/", register, name="register"),

]
