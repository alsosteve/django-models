from django.urls import path, include
from .views import SnackListView

urlpatterns = [
  # empty sub-path handled by SnackListView using as_view()
    path('', SnackListView.as_view(), name="snack_list"),
]