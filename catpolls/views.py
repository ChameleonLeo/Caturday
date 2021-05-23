from django.db.models import Sum
from django.db.models import Max
from random import randint

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Catuestion, Cachoice


class IndexView(generic.ListView):
    template_name = 'catpolls/list.html'
    context_object_name = 'latest_catuestion_list'
    model = Catuestion
    paginate_by = 3

    def get_queryset(self):
        return Catuestion.objects.filter(
            publication_date__lte=timezone.now()
        ).order_by('-publication_date')


class PopularView(generic.ListView):
    template_name = 'catpolls/popular.html'
    context_object_name = 'popular_catuestion_list'

    def get_queryset(self):
        return Catuestion.objects.annotate(
            sum_votes=Sum('cachoice__cavotes')
        ).order_by('-sum_votes')[:5]


def rand_tip():
    max_id = Catuestion.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = randint(1, max_id)
        if Catuestion.objects.filter(pk=pk):
            return pk


def RandomView(request):
    catuestion = get_object_or_404(Catuestion, pk=rand_tip())
    return render(request, 'catpolls/detail.html', {'catuestion': catuestion})


class DetailView(generic.DetailView):
    model = Catuestion
    template_name = 'catpolls/detail.html'

    def get_queryset(self):
        return Catuestion.objects.filter(publication_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Catuestion
    template_name = 'catpolls/results.html'


def vote(request, catuestion_id):
    question = get_object_or_404(Catuestion, pk=catuestion_id)
    try:
        selected_cachoice = question.cachoice_set.get(pk=request.POST['cachoice'])
    except (KeyError, Cachoice.DoesNotExist):
        return render(request, 'catpolls/detail.html', {
            'catuestion': question,
            'error_message': "You did not select a choice.",
            })
    else:
        selected_cachoice.cavotes += 1
        selected_cachoice.save()
    return HttpResponseRedirect(reverse('catpolls:results', args=(question.id,)))
