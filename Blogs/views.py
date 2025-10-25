from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . models import Blog
from . models import Comment

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        posts = Blog.objects.all().order_by('-created_at')
    else:
        posts = None

    return render(request, 'index.html', {"posts": posts}) 

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pwd1 = request.POST.get('password1')
        pwd2 = request.POST.get('password2')

        if pwd1 == pwd2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=pwd1)
                messages.success(request, 'Account created successfully! Please login.')
                return redirect('login')
        else:
            messages.info(request, 'Passwords are not same!')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')

        user = auth.authenticate(username=username, password=pwd)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'User Logged In Successfully')
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required
def logout(request):
    auth.logout(request)
    messages.info(request, 'User Logged Out Successfully')
    return redirect('/')

def viewpost(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    blog = get_object_or_404(Blog, id=pk)
    total = blog.comments.count()
    
    return render(request, 'viewpost.html', {'post': post, 'total': total})

@login_required
def newpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')

        if not title:
            messages.error(request, 'Title is required!')
            return redirect('newpost')
        
        if not body:
            messages.error(request, 'Content is required!')
            return redirect('newpost')

        try:
            blog = Blog (
                title = title,
                body = body,
                author = request.user,
            )
            blog.save()

            messages.info(request, "Your post has been created Successfully!")
            return redirect('/')
        
        except Exception as e:
            messages.error(request, f'An error occured: {str(e)}')
            return redirect('newpost/')
        
    else:
        return render(request, 'newpost.html')

@login_required
def deletepost(request, pk):
    post = get_object_or_404(Blog, id = pk, author = request.user)
    if request.method == 'POST':
        post.delete()
        messages.info(request, f"Post {post.title} Deleted Successfully")
        return redirect('/')

    else:
        return render(request, 'deletepost.html', {'post': post})
    
def comment(request, pk):
    blog = get_object_or_404(Blog, id=pk)

    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            new_comment = Comment(
                blog=blog,
                author=request.user,
                text=text
            )
            new_comment.save()
            messages.info(request, "Comment created successfully!")
            return redirect('comment', pk=blog.id)
        else:
            messages.info(request, "Please write something for comment!")
            return redirect('comment', pk=blog.id)

    comments = blog.comments.all()
    return render(request, "comment.html", {
        "blog": blog,
        "comments": comments
    })

@login_required
def editpost(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        edit_title = request.POST.get('title')
        edit_body = request.POST.get('body')

        if edit_title and edit_body:
            post.title=edit_title
            post.body=edit_body
            post.save()
            messages.success(request, "Post updated successfully!")
            return redirect('viewpost', pk=post.pk)
        else:
            messages.error(request, "Please fill in the form")

    else:
        return render(request, 'editpost.html', {'post': post})