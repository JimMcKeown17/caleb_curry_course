from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("Hello, World!")

def files(request):
    data = [{'name': 'file1', 'size': 100}, {'name': 'file2', 'size': 200}]
    return render(request, 'files/files.html', {"files": data})