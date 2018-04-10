from django.shortcuts import render

# Create your views here.

from affitti.models import ContrattoLocazione, Immobile


def index(request):
    """
    View function for home page of site.
    """
    num_contratti = ContrattoLocazione.objects.all().count()
    num_immobili = Immobile.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_contratti': num_contratti, 'num_immobili': num_immobili}
    )
