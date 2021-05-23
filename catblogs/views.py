from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
import datetime
from django.utils import timezone
from django.views import generic
from .models import CatPost
from .forms import CatPostForm


"""def catpost_list(request):
    catposts = CatPost.objects.filter(
        publication_date__lte=timezone.now()
        ).order_by('publication_date')
    return render(request, 'catblogs/catpost_list.html', 
                  {'catposts': catposts})"""


class PostListView(generic.ListView):
    template_name = 'catblogs/catpost_list.html'
    context_object_name = 'catposts'
    model = CatPost
    paginate_by = 3

    def get_queryset(self):
        return CatPost.objects.filter(
            publication_date__lte=timezone.now()
        ).order_by('publication_date')


class RecentPostListView(generic.ListView):
    template_name = 'catblogs/catpost_list.html'
    context_object_name = 'catposts'

    def get_queryset(self):
        return CatPost.objects.filter(
            publication_date__gte=timezone.now() - datetime.timedelta(days=30)
        ).order_by('publication_date')


class ArchivePostListView(generic.ListView):
    template_name = 'catblogs/catpost_list.html'
    context_object_name = 'catposts'
    model = CatPost
    paginate_by = 3

    def get_queryset(self):
        return CatPost.objects.filter(
            publication_date__lte=timezone.now() - datetime.timedelta(days=365)
        ).order_by('publication_date')


class ShortPostListView(generic.ListView):
    template_name = 'catblogs/catpost_list.html'
    context_object_name = 'catposts'

    def get_queryset(self):
        return CatPost.objects.extra(
            where=["LENGTH(catext) < 300"]
        ).order_by('publication_date')


class ArticlePostListView(generic.ListView):
    template_name = 'catblogs/catpost_list.html'
    context_object_name = 'catposts'
    model = CatPost
    paginate_by = 3

    def get_queryset(self):
        return CatPost.objects.filter(
            catext__contains='article'
        ).order_by('publication_date')


class MyPostListView(generic.ListView):
    template_name = 'catblogs/catpost_list.html'
    context_object_name = 'catposts'
    model = CatPost
    paginate_by = 3

    def get_queryset(self):
        return CatPost.objects.filter(
            catauthor=self.request.user
        ).order_by('publication_date')


def catpost_detail(request, pk):
    catpost = get_object_or_404(CatPost, pk=pk)
    return render(request, 'catblogs/catpost_detail.html', {'catpost': catpost})


@login_required
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
