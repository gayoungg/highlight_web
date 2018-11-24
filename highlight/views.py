from django.shortcuts import render
from django.http import HttpResponseRedirect
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
    return render(request, 'highlight/example.html', {})
def loading(request):
    return render(request, 'highlight/loading.html', {})

