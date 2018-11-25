from django.shortcuts import render
from .models import ExtractedMusicList
from .forms import UploadForm


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


def example(request):
    music_list = ExtractedMusicList.objects.all()
    if len(music_list) > 5:
        music_list = music_list[len(music_list)-5:len(music_list)]
        music_list.reverse()
    return render(request, 'highlight/example.html', {
        'music_list': music_list
    })


def loading(request):
    return render(request, 'highlight/loading.html', {})
