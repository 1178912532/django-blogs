from django.shortcuts import render, redirect
from django.http import HttpResponse
from users import models
import datetime


# Create your views here.
def register(request):
    return render(request, 'register.html')


def index(request):
    queryset = models.Text.objects.all()
    return render(request, 'index.html', {'text_list': queryset})


def text(request):
    id = request.GET.get('id')
    queryset = models.Text.objects.filter(id=id)
    return render(request, 'text.html', {'text': queryset})


def admin(request):
    queryset = models.Text.objects.all()
    return render(request, 'blogadm.html', {'text_list': queryset})


def add_blog(request):
    if request.method == 'GET':
        return render(request, 'addblog.html')
    if request.method == 'POST':
        title = request.POST['title']
        tag = request.POST['tags']
        content = request.POST['content']
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        models.Text.objects.create(title=title, tags=tag, content=content, date=date)
        return redirect('/blogadm/')


def editblog(request):
    id = request.GET.get('id')
    # if id:
    if request.method == 'GET':
        print(id)
        queryset = models.Text.objects.filter(id=id)
        return render(request, 'editblog.html', {'text': queryset})
    if request.method == 'POST':
        id = request.POST['id']
        title = request.POST['title']
        tag = request.POST['tags']
        content = request.POST['content']
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        new = models.Text.objects.filter(id=id)[0]
        new.title = title
        new.tags = tag
        new.content = content
        new.date = date
        new.save()
        return redirect('/blogadm/')
    # else:
    #     redirect('/blogadm/')
