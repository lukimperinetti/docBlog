from datetime import datetime

from django.shortcuts import render


def index(request):

    date = datetime.now()

    return render(request, 'DocBlog/index.html', context={"date": date})