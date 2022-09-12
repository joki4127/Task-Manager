from django.urls import path

from projects.views import (
    ProjectListview,
    ProjectDetailview,
)

urlpatterns = [
    path("", ProjectListview.as_view(), name="list_projects"),
    path("<int:pk>/", ProjectDetailview.as_view(), name="show_project"),
]
