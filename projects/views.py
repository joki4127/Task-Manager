from django.views.generic.list import ListView

from projects.models import Project


# Create your views here.
class ProjectListview(ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "projectlist"
