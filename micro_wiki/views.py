from django.shortcuts import render

def index(request):
    return render(request, 'micro_wiki/index.html', title='Wiki')