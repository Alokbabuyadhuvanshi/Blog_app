from django.shortcuts import render ,get_object_or_404 ,redirect
from .models import Blog 
from .forms import blogForm , UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login

def home(request):
    all_blogs = Blog.objects.all()
    return render(request,'home.html',{'all_blogs':all_blogs})

def show_blog(request ,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'show_blog.html', {'blog': blog})

@login_required
def create_blog(request):
    if request.method == "POST":
        form =blogForm(request.POST, request.FILES)
        if form.is_valid():
            blog =form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('home')

    else:
        form = blogForm()
    return render(request,'create_blog.html',{'form':form})

@login_required
def edit_blog(request , blog_id):
    blog = get_object_or_404(Blog ,pk = blog_id , user = request.user)
    if request.method == "POST":
        form = blogForm(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            blog = form.save(commit = false) # type: ignore
            blog.user = request.user
            blog.save()
            return redirect('show_blog',blog_id=blog.id)
    else:
        form = blogForm(instance = blog)
    return render(request,create_blog.html,{'form':form})


@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id,user =request.user)
    if request.method == "POST":
        blog.delete()
        return redirect('show_blog')
    return render(request,'blog_conform_delete.html',{'blog':blog})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})
