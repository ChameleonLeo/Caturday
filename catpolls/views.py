from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Catuestion, Cachoice


class IndexView(generic.ListView):
    template_name = 'catpolls/index.html'
    context_object_name = 'latest_catuestion_list'

    def get_queryset(self):
        return Catuestion.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Catuestion
    template_name = 'catpolls/detail.html'


class ResultsView(generic.DetailView):
    model = Catuestion
    tamplate_name = 'catpolls/results.html'


def vote(request, catuestion_id):
    p = get_object_or_404(Catuestion, pk=catuestion_id)
    try:
        selected_cachoice = p.cachoice_set.get(pk=request.POST['choice'])
    except (KeyError, Cachoice.DoesNotExist):
        return render(request, 'catpolls/detail.html', {
            'catuestion': p,
            'error_message': "You did not select a choice.",
            })
    else:
        selected_cachoice.cavotes += 1
        selected_cachoice.save()
    return HttpResponseRedirect(reverse('catpolls:results', args=(p.id,)))
