# -*- coding:utf-8 -*-

from django.shortcuts import render,HttpResponseRedirect
from .models import ExtractedMusicList, MusicStorage
from .forms import UploadForm
from extractor.main import extraction

def index(request):
    return render(request, 'highlight/index.html', {})


def extract(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../loading')
    else:
        form = UploadForm()
        return render(request, 'highlight/extract.html', {
           'form': form
        })


def result(request):
    return render(request, 'highlight/result.html', {})


def result_detail(request, pk):
    highlight = ExtractedMusicList.objects.get(pk=pk)
    return render(request, 'highlight/result.html',
                  {
                      'highlight': highlight
                  })

def example(request):
    music_list = ExtractedMusicList.objects.all()

    music_list.reverse()
    return render(request, 'highlight/example.html', {
        'music_list': music_list
    })


def loading(request):
    uploaded_music_list=list(MusicStorage.objects.all())
    print(uploaded_music_list[-1].file.name)
    str = "C:/Users/dkswl/PycharmProjects/highlight_web/media/" + uploaded_music_list[-1].file.name
    extraction([str, ], length=30, save_score=True, save_thumbnail=True, save_wav=True)
    return render(request, 'highlight/result.html', {
    })
