from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Catuestion, Cachoice


class IndexView(generic.ListView):
    template_name = 'catpolls/index.html'
    context_object_name = 'latest_catuestion_list'

    def get_queryset(self):
        return Catuestion.objects.filter(
            publication_date__lte=timezone.now()
        ).order_by('-publication_date')[:5]


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
