
# Create your views here.
from django.shortcuts import render
from .forms import CategoryForm,PageForm
from .models import Category,Page

def home(request):
    return render(request,'prob/index.html')
def category(request):
    form1 = CategoryForm()
    form = CategoryForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        nov = form.cleaned_data["numberOfVisits"]
        nol = form.cleaned_data["numberOfLikes"]
        Category.objects.create(name=name,numberOfVisits=nov,numberOfLikes=nol)
    return render(request,'prob/first.html',{'form':form1})
def page(request):
    form1=PageForm()
    form=PageForm(request.POST)
    if form.is_valid():
        category=form.cleaned_data['category']
        title=form.cleaned_data['title']
        url=form.cleaned_data['url']
        view=form.cleaned_data['view']
        Page.objects.create(category=category,title=title,url=url,view=view)
    return render(request,'prob/second.html',{'form':form1})
def display(request):
    pages = Page.objects.all()
    categories = Category.object.all()
    return render(request,'prob/third.html',{"pages":pages,"categories":categories})
