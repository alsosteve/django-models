from django.urls import path, include
from .views import SnackListview

urlpatterns = [
  # empty sub-path handled by SnackListView using as_view()
    path('', SnackListview.as_view(), name="snack_list"),
]