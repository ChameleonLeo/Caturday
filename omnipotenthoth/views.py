from random import randint
from django.db.models import Max

from django.shortcuts import render, get_object_or_404
from omnipotenthoth.models import Tip


def tip_start(request):
    return render(request, 'omnipotenthoth/thoth_start.html')


def rand_tip():
    max_id = Tip.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = randint(1, max_id)
        if Tip.objects.filter(pk=pk):
            return pk


def tip_next(request):
    tip = get_object_or_404(Tip, pk=rand_tip())
    question = False
    if '?' in tip.tip_text:
        question = True
    return render(request, 'omnipotenthoth/thoth_face.html', {'tip': tip, 'question': question})
