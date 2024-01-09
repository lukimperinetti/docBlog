from django.shortcuts import render

def index(request):
    return render(request, 'Blog/index.html')


def article(request, numero_article):

    if numero_article in ['01', '02', '03']:
        return render(request, f"Blog/article-{numero_article}.html")
    return render(request, 'Blog/404.html')