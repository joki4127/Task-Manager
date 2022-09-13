from django.urls import path

from tasks.views import (
    TaskCreateview,
)


urlpatterns = [
    path("create/", TaskCreateview.as_view(), name="create_task"),
]
