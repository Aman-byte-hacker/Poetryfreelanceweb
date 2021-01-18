from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Contact
from django.contrib import messages

def index(request):
    return render(request,"index.html")

def poetry(request):
    blogs=Blog.objects.all()
    content={
        'blogs':blogs
    }
    return render(request,"poetry.html",content)    

    
def search(request):
    query=request.GET['query']
    if len(query)>40:
        return HttpResponse("We Don't Support a Lot of words to Search It Is Beyond Our Security Purposes!🤐")
    blogs=Blog.objects.filter(name__icontains=query)
    content={
        'blogs':blogs
    }
    return render(request,"search.html",content)    
        
def contact(request):
    if request.method == "POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        con=Contact(firstname=firstname,lastname=lastname,email=email,subject=subject)
        con.save()
        messages.success(request,"Your Message has been sent successfully will reply in 24 Hours..")
        
    return render(request,"contact.html")        