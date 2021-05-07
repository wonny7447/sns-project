from django.shortcuts import render

def showmain(request):
    return render(request, 'main/mainpage.html')

def history(request):
    return render(request, 'main/history.html')

def like(request):
    return render(request, 'main/like.html')