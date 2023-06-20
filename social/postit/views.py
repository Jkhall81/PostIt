from django.shortcuts import render, redirect
from .models import Profile, Post
from django.contrib import messages
from .forms import PostForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request, 'Your post was successfuly!')
                return redirect('home')

        posts = Post.objects.all().order_by('-created_at')
        return render(request, 'home.html', {'posts': posts, 'form': form})
    else:
        posts = Post.objects.all().order_by('-created_at')
        return render(request, 'home.html', {'posts': posts})


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {'profiles': profiles})
    else:
        messages.success(request, 'You must be logged in to view this page!')
        return redirect('home')


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        posts = Post.objects.filter(user_id=pk).order_by('-created_at')

        # post form logic
        if request.method == 'POST':
            # get current user
            current_user_profile = request.user.profile
            # get form data
            action = request.POST['follow']
            # decide to follow or unfollow
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            elif action == 'follow':
                current_user_profile.follows.add(profile)
            # save the profile
            current_user_profile.save()

        return render(request, 'profile.html', {'profile': profile, 'posts': posts})
    else:
        messages.success(request, 'You must be logged in to view this page!')
        return redirect('home')


def login_user(request):
    if request.method == 'POST':
        # must match name given in input element on form

        username = request.POST['username']
        password = request.POST['password']
        # find out which user is logging in

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in successfully!')
            return redirect('home')
        else:
            messages.success(request, 'Login failure, Please try again!')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')
