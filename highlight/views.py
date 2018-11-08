from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'highlight/index.html', {})
def extract(request):
    return render(request, 'highlight/extract.html', {})
def result(request):
    return render(request, 'highlight/result.html', {})
def example(request):
    return render(request, 'highlight/example.html', {})