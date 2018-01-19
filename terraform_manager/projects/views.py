from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
from .models import Project


def project_create(request):
    return HttpResponse("<h1>Create<h1>")

def project_detail(request): #retrieve
    #instance = Post.objects.get(id=9999)
    instance = get_object_or_404(Post, id=1)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "project_detail.html", context)

def project_list(request): #list items
    queryset = Project.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My User List"
    #     }
    # else:
    #     context = {
    #         "title": "List"
    #     }
    return render(request, "index.html", context)

def project_update(request):
    return HttpResponse("<h1>Update<h1>")

def project_delete(request):
    return HttpResponse("<h1>Delete<h1>")

