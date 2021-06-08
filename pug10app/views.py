from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pug10app/index.html')