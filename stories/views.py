from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StoryForm, CommentForm
from .models import Story, Vote, Comment
import datetime



def frontpage(request):
    # Popular Stories
    stories = Story.objects.all().order_by('-vote_count')[:5]
    # Recent stories
    new_stories = Story.objects.all().order_by('-published_date')[:50]
    context = {
        'stories': stories,
        'new_stories': new_stories,
    }
    return render(request, 'stories/frontpage.html', context)


def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        stories = Story.objects.filter(title__icontains=query)
    else:
        stories = []

    context = {
        'query': query,
        'stories': stories,
    }
    return render(request, 'stories/search.html', context)


@login_required
def vote(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    next_page = request.GET.get('next_page', '')
    if story.author != request.user and not Vote.objects.filter(author=request.user, story=story):
        vote = Vote.objects.create(story=story, author=request.user)
    if next_page == 'story_detail':
        return redirect('story_detail', story_id=story_id)
    else:
        return redirect('frontpage')


def story_detail(request, story_id):
    story = get_object_or_404(Story, pk=story_id)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.author = request.user
            comment.save()
            return redirect('story_detail', story_id=story_id)
    else:
        form = CommentForm()

    context = {
        'form': form,
        'story': story,
    }
    return render(request, 'stories/detail.html', context)


@login_required
def submit_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.save()
            return redirect('frontpage')
    else:
        form = StoryForm()

    context = {
        'form': form,
    }
    return render(request, 'stories/submit_story.html', context)
