from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuillPostForm
from .models import QuillPost




# Create your views here.

def model_form_view(request):
    return render(request, 'editor_view.html', {'form': QuillPostForm()})

def show_all_post(request):
    quill_posts = QuillPost.objects.all().order_by('-id')
    return render(request, 'content/show_all_posts.html', {'quill_posts': quill_posts})


def quillpost_detail(request, quillpost_id):
    quillpost = get_object_or_404(QuillPost, pk=quillpost_id)
    quill_content_html = quillpost.content.html
    return render(request, 'content/detail.html', {'quill_content_html': quill_content_html, 'quillpost': quillpost})
