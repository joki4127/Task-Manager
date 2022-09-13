from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from tasks.models import Task


# Create your views here.
class TaskCreateview(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]
    context_object_name = "taskcreate"

    def form_valid(self, form):
        item = form.save(commit=False)
        item.user = self.request.user
        item.save()
        return redirect("show_project", pk=item.pk)

    def get_queryset(self):
        return Task.objects.filter(members=self.request.user)
