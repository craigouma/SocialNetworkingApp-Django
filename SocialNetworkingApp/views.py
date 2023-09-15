from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Post
from .forms import UserProfileForm


# View for the home page
def home(request):
    # Retrieve posts from the database
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'SocialNetworkingApp/home.html', {'posts': posts})


# View for the user profile page
@login_required
def profile(request):
    # Retrieve user's profile information
    user_profile: UserProfile = UserProfile.objects.get(user=request.user)
    if request.method != 'POST':
        profile_form = UserProfileForm(instance=user_profile)
    else:
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')

    return render(request, 'SocialNetworkingApp/profile.html',
                  {'user_profile': user_profile, 'profile_form': profile_form})


# View for user registration (signup page)
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# View for user login (login page)
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    return render(request, 'registration/login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
