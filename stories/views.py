from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StoryForm
from .models import Story
import datetime



def frontpage(request):
    recent_date = datetime.datetime.now() - datetime.timedelta(days=1)
    stories = Story.objects.filter(published_date__gte=recent_date).order_by('-vote_count')

    context = {
        'stories': stories,
    }
    return render(request, 'stories/frontpage.html', context)


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
