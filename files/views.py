from django.http import HttpResponse, Http404
from django.shortcuts import render

data = [{'id': 1, 'name': 'file1', 'size': 100}, {'id': 2, 'name': 'file2', 'size': 200}, {'id': 3, 'name': 'file3', 'size': 300}]


def index(request):
    return render(request, 'files/index.html')

def files(request):
    return render(request, 'files/files.html', {"files": data})


def file(request, file_id):
    file = next((item for item in data if item['id'] == file_id), None)
    if file:
        return render(request, 'files/file.html', {"file": file})
    else:
        raise Http404('File not found')