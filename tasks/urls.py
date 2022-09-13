from django.urls import path

from tasks.views import (
    TaskCreateview,
    TaskListview,
)


urlpatterns = [
    path("create/", TaskCreateview.as_view(), name="create_task"),
    path("mine/", TaskListview.as_view(), name="show_my_tasks"),
]
