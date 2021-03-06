from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Todo


# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "main/index.html"
    context_object_name = "todos"

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by("-added_date")


@login_required
def add_todo(request):
    if request.POST:
        pub_date = timezone.now()
        content = request.POST.get("todo")
        Todo.objects.create(added_date=pub_date, text=content, user=request.user)
    return HttpResponseRedirect(reverse("main:home"))


@login_required
def delete_todo(request, todo_id):
    if request.POST:
        Todo.objects.get(pk=todo_id).delete()
    return HttpResponseRedirect(reverse("main:home"))
