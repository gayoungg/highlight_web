# -*- coding:utf-8 -*-

from django.shortcuts import render,HttpResponseRedirect
from .models import ExtractedMusicList, MusicStorage
from .forms import UploadForm
from extractor.main import extraction

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

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
    uploaded_music_list = list(MusicStorage.objects.all())
    name = uploaded_music_list[-1].file.name
    filename = name[6:len(name) - 4]
    str = "C:/Users/dkswl/PycharmProjects/highlight_web/media/" + name
    extraction(str,filename, length=30, save_score=False, save_thumbnail=False, save_wav=True)
    filename+="_output.wav"
    return render(request, 'highlight/result.html', {
        'highlight_file': filename
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
    paginator = Paginator(music_list, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    musics = paginator.get_page(page)
    return render(request, 'highlight/example.html', {
        'musics': musics
    })


def loading(request):
    return render(request, 'highlight/loading.html', )