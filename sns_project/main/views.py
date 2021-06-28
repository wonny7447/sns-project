from main.models import Post, Comment
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
    all_comment = qna.comments.all().order_by('-created_at')
    return render(request, 'main/qna_detail.html', {'qna':qna, 'comments':all_comment})

def new(request):
    return render(request, 'main/new_qna.html')

def create(request):
	new_qna = Post()
	new_qna.title = request.POST['title']
	new_qna.writer = request.user
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
	update_qna.writer = request.user
	update_qna.reg_date = timezone.now()
	update_qna.body = request.POST['body']
	update_qna.save()
	return redirect('main:detail', update_qna.id)

def delete(request, id):
    delete_qna = Post.objects.get(id=id)
    delete_qna.delete()
    return redirect('main:qna')


def create_comment(request, id):
	if request.method == "POST":
		post = get_object_or_404(Post, pk=id)
		current_user = request.user
		comment_content = request.POST.get('content')
		Comment.objects.create(content=comment_content, writer=current_user, post=post)
	return redirect('main:detail', id)


def edit_comment(request, qna_id, comment_id):
    edit_comment = Comment.objects.get(id=comment_id)
    return render(request, 'main/edit_comment.html', {'qna_id':qna_id, 'comment':edit_comment})


def update_comment(request, qna_id, comment_id):
	update_comment = Comment.objects.get(id=comment_id)
	update_comment.content = request.POST['content']
	update_comment.updated_at = timezone.now()
	update_comment.save()
	return redirect('main:detail', qna_id)


def delete_comment(request, qna_id, comment_id):
    delete_comment = Comment.objects.get(id=comment_id)
    delete_comment.delete()
    return redirect('main:detail', qna_id)


