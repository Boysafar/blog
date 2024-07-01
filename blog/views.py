from django.shortcuts import render
from .models import BlogSetting, Article, Resume


def home(request):
    return render(request, 'home.html')


def blogs(request):
    articles = Article.objects.all()
    return render(request, 'blogs.html', {'articles': articles})


def resume(request):
    resumes = Resume.objects.all()
    return render(request, 'resume.html', {'resumes': resumes})
