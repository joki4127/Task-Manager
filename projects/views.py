from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from projects.models import Project


# Create your views here.
class ProjectListview(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "projectlist"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)
