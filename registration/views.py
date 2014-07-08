from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from registration.forms import PlayerForm
from registration.models import Player


def index(request):
    return render(request, 'registration/index.html')

def register(request):
    if request.method == 'POST': #
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = Player()

            # add form fields to player object
            for k,v in form.cleaned_data.items():
                print k,v
                setattr(player, k, v)

            player.save()
            return HttpResponseRedirect('frisbee/thanks')
    else:
        form = PlayerForm()

    return render(request, 'registration/register.html', {
        'form': form,
    })

def thanks(request):
    return render(request, 'registration/thanks.html')
