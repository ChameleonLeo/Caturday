from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Catuestion, Cachoice


def index(request):
    latest_catuestion_list = Catuestion.objects.order_by('-publication_date')[:5]
    context = {"latest_catquestion_list": latest_catuestion_list}
    return render(request, "catpolls/index.html", context)


def detail(request, catuestion_id):
    catuestion = get_object_or_404(Catuestion, pk=catuestion_id)
    return render(request, 'catpolls/detail.html', {'catuestion': catuestion})


def results(request, catuestion_id):
    catuestion = get_object_or_404(Catuestion, pk=catuestion_id)
    return render(request, 'catpolls/results.html', {'catuestion': catuestion})


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
