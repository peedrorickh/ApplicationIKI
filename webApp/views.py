from django.shortcuts import render

# Create your views here.
def usuario(request):
    return render(request, 'webApp/index.html', {})