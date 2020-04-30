from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Match
from .forms import ProfileForm, MatchForm

# Create your views here.

def index (request):
    return render(request, 'index.html')

def make_team(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user.get_username()
            profile.save()
            return redirect('detail_team', profile.pk)
    else:
        form = ProfileForm()
    return render(request, 'make_team.html',{"form":form})

def detail_team(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    return render(request, 'detail_team.html', {"profile": profile})

def make_match(request):
    if request.method == "POST":
        form = MatchForm(request.POST, request.FILES)
        if form.is_valid():
            match = form.save(commit=False)
            match.user = request.user.get_username()
            match.save()
            return redirect('detail_match', match.pk)
    else:
        form = MatchForm()
    return render(request, 'make_match.html',{"form":form})

def detail_match(request, match_pk):
    match = get_object_or_404(Match, pk=match_pk)
    return render(request, 'detail_match.html', {"match": match})