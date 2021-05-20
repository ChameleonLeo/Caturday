from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import CatPost
from .forms import CatPostForm


def catpost_list(request):
    catposts = CatPost.objects.filter(publication_date__lte=timezone.now()).order_by('publication_date')
    return render(request, 'catblogs/catpost_list.html', {'catposts': catposts})


def catpost_detail(request, pk):
    catpost = get_object_or_404(CatPost, pk=pk)
    return render(request, 'catblogs/catpost_detail.html', {'catpost': catpost})


def catpost_new(request):
    if request.method == "POST":
        catform = CatPostForm(request.POST)
        if catform.is_valid():
            catpost = catform.save(commit=False)
            catpost.catauthor = request.user
            catpost.publication_date = timezone.now()
            catpost.save()
            return redirect('catblogs:catpost_detail', pk=catpost.pk)
    else:
        catform = CatPostForm()
    return render(request, 'catblogs/catpost_edit.html', {'catform': catform})


def catpost_edit(request, pk):
    catpost = get_object_or_404(CatPost, pk=pk)
    if request.method == 'POST':
        catform = CatPostForm(request.POST, instance=catpost)
        if catform.is_valid():
            catpost = catform.save(commit=False)
            catpost.catauthor = request.user
            catpost.publication_date = timezone.now()
            catpost.save()
            return redirect('catblogs:catpost_detail', pk=catpost.pk)
    else:
        catform = CatPostForm(instance=catpost)
    return render(request, 'catblogs/catpost_edit.html', {'catform': catform})
