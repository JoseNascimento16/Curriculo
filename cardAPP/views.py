import os
from django.http import FileResponse, Http404
from django.shortcuts import render

# Create your views here.

def index(request):
    # return render(request, 'index.html')

    try:
        return FileResponse(open('./static_dir/pdf/Resume-Jose-Nascimento.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
