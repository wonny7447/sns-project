from django.shortcuts import render, get_object_or_404, redirect
from .models import QNA
from django.utils import timezone

def showmain(request):
    return render(request, 'main/mainpage.html')

def history(request):
    return render(request, 'main/history.html')

def like(request):
    return render(request, 'main/like.html')

def qna(request):
    qna = QNA.objects.all()
    return render(request, 'main/qna.html', {'qna':qna})

def detail(request, id):
    qna = get_object_or_404(QNA, pk=id)
    return render(request, 'main/qna_detail.html', {'qna':qna})

def new(request):
    return render(request, 'main/new_qna.html')

def create(request):
	new_qna = QNA()
	new_qna.title = request.POST['title']
	new_qna.writer = request.POST['writer']
	new_qna.reg_date = timezone.now()
	new_qna.body = request.POST['body']
	new_qna.save()
	return redirect('detail', new_qna.id)