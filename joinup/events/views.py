from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from slugify import slugify

from .forms import GroupForm
from .models import Group, Event, Comment, Tag

# Create your views here.
def welcome(request):
    tags = Tag.objects.all()
    groups = Group.objects.all()
    return render(request, 'events/welcome.html', {
        'page_title': 'Discover',
        'tags': tags,
        'groups': groups,
    })

def group_view(request, group_name):
    group = get_object_or_404(Group, name_url=group_name)
    events = Event.objects.filter(group=group)
    return  render(request, 'events/group_view.html', {
        'page_title': group.name + ' group',
        'group': group,
        'events': events,
    })


def event_detail(request, group_name, event_name):
    group = get_object_or_404(Group, name_url=group_name)
    print("Group")
    event = get_object_or_404(Event, group=group.id, name_url=event_name)
    return render(request, 'events/event_detail.html', {
        'page_title': event.name,
        'group': group,
        'event': event,
    })

def tag_view(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    groups = Group.objects.filter(tags=tag)
    return  render(request, 'events/tag_view.html', {
        'page_title': tag_name,
        'tag': tag,
        'groups': groups,
    })


@login_required
def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)

            name = first_upper_case(group.name)
            group.name = name
            group.name_url = first_upper_case(slugify(name))

            #group.created_date = timezone.now()
            group.save()
            group.members.add(request.user)

            return redirect('group_view', group_name=group.name_url)

    else:
        form = GroupForm()
    return render(request, 'events/create_group.html', {
        'page_title': 'Create group',
        'form': form,
    })

@login_required
def create_event(request, group_name):
    group = get_object_or_404(Group, name_url=group_name)
    return render(request, 'events/welcome.html', {
        'page_title': 'Create event',
        'group': group,
    })

def first_upper_case(name):
    first_letter = name[0].upper()
    return first_letter + name[1:]
