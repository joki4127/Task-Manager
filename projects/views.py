from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task

from projects.models import Project


# Create your views here.
class ProjectListview(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "projectlist"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailview(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "projects/detail.html"
    context_object_name = "projectdetail"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)
