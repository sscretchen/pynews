from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



def home(request):
    return render(request, 'members/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'members/signup.html', context)


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    vote_count = 0

    for story in user.stories.all():
        """We use -1 because upon creation of a story each user gets a vote from
        themselves. See Story model 'vote_count' attribute for details"""
        vote_count = vote_count + (story.vote_count - 1)

    context = {
        'user': user,
        'vote_count': vote_count,
    }
    return render(request, 'members/user_profile.html', context)


def votes(request, username):
    user = get_object_or_404(User, username=username)
    votes = user.votes.all()

    stories = []

    for vote in votes:
        stories.append(vote.story)

    context = {
        'user': user,
        'stories': stories,
    }
    return render(request, 'members/user_votes.html', context)


def submissions(request, username):
    user = get_object_or_404(User, username=username)
    stories =  user.stories.all()

    context = {
        'user': user,
        'stories': stories,
    }
    return render(request, 'members/user_submissions.html', context)
