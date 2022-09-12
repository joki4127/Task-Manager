from django.urls import path

from projects.views import (
    ProjectListview,
)

urlpatterns = [
    path("", ProjectListview.as_view(), name="list_projects"),
]
