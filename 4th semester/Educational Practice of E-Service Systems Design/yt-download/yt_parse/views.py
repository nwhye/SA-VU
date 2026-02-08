from django.shortcuts import render
from django.contrib import messages
from yt_parse.quickstart import *

def index(request):

    if request.method == 'POST': #triggers on a post method
        link = request.POST['link']
        main(link)
        messages.success(request, 'Success!')
        return render(request, 'index.html')

    else:
        return render(request, 'index.html')

