from django.utils import timezone
from affitti.models import ContrattoLocazione


class ContrattoListView():
    def get_queryset(self):
        now = timezone.now()
        upcoming = ContrattoLocazione.objects.filter()