from django.shortcuts import render, get_object_or_404
from editor.models import QuillPost


# Create your views here.

def show_posts(request):
    quill_posts = QuillPost.objects.all().order_by('-id')
    return render(request, 'content/show_posts.html', {'quill_posts': quill_posts})

def home(request):
    quill_posts = QuillPost.objects.all().order_by('-id')
    return render(request, 'content/home.html', {'quill_posts': quill_posts})

def quillpost_detail(request, quillpost_id):
    quillpost = get_object_or_404(QuillPost, pk=quillpost_id)
    quill_content_html = quillpost.content.html
    return render(request, 'content/detail.html', {'quill_content_html': quill_content_html, 'quillpost': quillpost})
