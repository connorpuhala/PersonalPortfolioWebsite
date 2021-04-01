from django.shortcuts import render
from projects.models import Project, Experience

def project_index(request):
    projects = Project.objects.all().order_by('id') 
    experiences = Experience.objects.all().order_by('id') 
    context = {
        'projects': projects,
        'experiences': experiences
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def experience_detail(request, pk):
    experience = Experience.objects.get(pk=pk)
    context = {
        'experience': experience
    }
    return render(request, 'experience_detail.html', context)

def about_page(request):
    return render(request, 'about_page.html')

def story(request):
    return render(request, 'story.html')
