from django.urls import path

from tasks.views import (
    TaskCreateview,
    TaskListview,
    TaskUpdateview,
)


urlpatterns = [
    path("create/", TaskCreateview.as_view(), name="create_task"),
    path("mine/", TaskListview.as_view(), name="show_my_tasks"),
    path("<int:pk>/complete/", TaskUpdateview.as_view(), name="complete_task"),
]
