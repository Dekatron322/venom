from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
	path("", views.IndexView, name="index"),
	path("result/<str:domain_name>/", views.ResultView, name="result"),
	path("buy/<str:domain_name>/", views.BuyView, name="buy"),
	path("registered/", views.RegisteredView, name="registered"),
	path("manage/<str:domain_name>/", views.ManageView, name="manage"),
	path("transfer/<str:domain_name>/<str:domain_namek>/finish/", views.Transfer2View, name="transfer2"),
]