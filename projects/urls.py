from django.urls import path

from projects.views import (
    ProjectCreateview,
    ProjectListview,
    ProjectDetailview,
)

urlpatterns = [
    path("", ProjectListview.as_view(), name="list_projects"),
    path("<int:pk>/", ProjectDetailview.as_view(), name="show_project"),
    path("create/", ProjectCreateview.as_view(), name="create_project"),
]
