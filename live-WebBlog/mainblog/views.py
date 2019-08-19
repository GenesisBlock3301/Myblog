from django.shortcuts import render,get_object_or_404,redirect
from .models import  *
from .forms import CommentForm,ProblemForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    posts_list = Post.objects.all()
    catagories = Catagory.objects.all()
    latest_post = Post.objects.all().order_by('-pub_date')[0:1]
    page = request.GET.get('page',1)
    paginator = Paginator(posts_list,3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'index.html',{'posts':posts,'catagories':catagories,'latest_post':latest_post})


def summery(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    catagories = Catagory.objects.all()
    latest_post = Post.objects.all().order_by('-pub_date')[0:1]
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', post_id)
    else:
        form = CommentForm()
    return render(request, 'single-blog.html', {'post': post, "form": form,'catagories':catagories,'latest_post':latest_post})

def detail(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    catagories = Catagory.objects.all()
    latest_post = Post.objects.all().order_by('-pub_date')[0:1]
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', post_id)
    else:
        form = CommentForm()
    return render(request, 'single-blog-detail.html', {'post': post, "form": form,'catagories':catagories,'latest_post':latest_post})


def catagory(request,cat_name):
    catagory_post = Catagory.objects.get(catagory_name=cat_name)
    cats = catagory_post.catagories.all()
    latest_post = Post.objects.all().order_by('-pub_date')[0:1]
    catagories2 = Catagory.objects.all() #home's catagory
    page = request.GET.get('page', 1)
    paginator = Paginator(cats, 3)
    try:
        cats = paginator.page(page)
    except PageNotAnInteger:
        cats = paginator.page(1)
    except EmptyPage:
        cats = paginator.page(paginator.num_pages)
    return render(request,'category.html',{'catagories':cats,'latest_post':latest_post,'catagories2':catagories2})

def about(request):
    catagories = Catagory.objects.all()
    return render(request,'about.html',{'catagories':catagories})

def problem(request):
    catagories = Catagory.objects.all()
    if request.method == "POST":
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('problem-list')
    else:
        form = ProblemForm()
    return render(request,'problem.html',{'form':form,'catagories':catagories})

def problem_list(request):
    catagories = Catagory.objects.all()
    problems = Problem.objects.all()
    return render(request,'problem-list.html',{'problems':problems,'catagories':catagories})
