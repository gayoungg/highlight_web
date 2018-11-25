from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .models import ExtractedMusicList
from .forms import UploadForm
import os


def index(request):
    return render(request, 'highlight/index.html', {})


def extract(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'highlight/loading.html')
    else:
        form = UploadForm()
    return render(request, 'highlight/extract.html', {
        'form': form
    })


def result(request):
    return render(request, 'highlight/result.html', {})

def resultDetail(request, pk):
    highlight = ExtractedMusicList.objects.get(pk=pk)
    return render(request, 'highlight/result.html',
                  {
                      'highlight':highlight
                  })

def example(request):
    music_list = ExtractedMusicList.objects.all()
    music_list = music_list[0:len(music_list)]

    music_list.reverse()
    return render(request, 'highlight/example.html', {
        'music_list': music_list
    })


def loading(request):
    return render(request, 'highlight/loading.html', {})
