import os
from django.http import FileResponse, Http404
from django.shortcuts import render

# Create your views here.

def index(request, **kwargs):
    # return render(request, 'index.html')
    try:
        return FileResponse(open('./static_dir/pdf/Resume 2 - José Nascimento.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
