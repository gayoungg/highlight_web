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
    return render(request, 'highlight/result.html', {
    })


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
    render(request, 'highlight/loading.html')
    uploaded_music_list=list(MusicStorage.objects.all())
    name = uploaded_music_list[-1].file.name
    fname = name[6:len(name)-4]
    print(fname)
    str = "C:/Users/dkswl/PycharmProjects/highlight_web/media/" + name
    extraction(str, fname, length=30, save_score=False, save_thumbnail=False, save_wav=True)
    filename = fname + '_output.wav'

    return render(request, 'highlight/result.html', {
        'highlight_file': filename
    })