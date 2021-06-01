from main.models import Post
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

def showmain(request):
    return render(request, 'main/mainpage.html')

def history(request):
    return render(request, 'main/history.html')

def like(request):
    return render(request, 'main/like.html')

def qna(request):
    qna = Post.objects.all()
    return render(request, 'main/qna.html', {'qna':qna})

def detail(request, id):
    qna = get_object_or_404(Post, pk=id)
    return render(request, 'main/qna_detail.html', {'qna':qna})

def new(request):
    return render(request, 'main/new_qna.html')

def create(request):
	new_qna = Post()
	new_qna.title = request.POST['title']
	new_qna.writer = request.POST['writer']
	new_qna.reg_date = timezone.now()
	new_qna.body = request.POST['body']
	new_qna.image = request.FILES.get('image')
	new_qna.save()
	return redirect('main:detail', new_qna.id)

def edit(request, id):
    edit_qna = Post.objects.get(id=id)
    return render(request, 'main/edit_qna.html', {'qna':edit_qna})


def update(request, id):
	update_qna = Post.objects.get(id=id)
	update_qna.title = request.POST['title']
	update_qna.writer = request.POST['writer']
	update_qna.reg_date = timezone.now()
	update_qna.body = request.POST['body']
	update_qna.save()
	return redirect('main:detail', update_qna.id)

def delete(request, id):
    delete_qna = Post.objects.get(id=id)
    delete_qna.delete()
    return redirect('main:qna')