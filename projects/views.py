from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from projects.models import Project


# Create your views here.
class ProjectListview(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "projectlist"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailview(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/detail.html"
    context_object_name = "projectdetail"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectCreateview(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/create.html"
    fields = ["name", "description", "members"]
    context_object_name = "projectcreate"

    def form_valid(self, form):
        item = form.save(commit=False)
        item.user = self.request.user
        item.save()
        return redirect("show_project", pk=item.pk)

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)
