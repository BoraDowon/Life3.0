from django.http import JsonResponse

from .models import LifeLog
from .data import LifeLogDto

# TODO: do we need to consider class based?


def create_event(data: LifeLogDto):
    # TODO: validation
    life_log = LifeLog()
    life_log.title = data.title
    life_log.status = data.status
    life_log.type = data.type
    life_log.save()


def remove_event():
    pass


def modify_event():
    pass


def read_events():
    """ Return all events.

    :return: JSON styled events list
    """
    life_logs = LifeLog.objects.all().values('title', 'status', 'type', 'timestamp')
    return JsonResponse({'events': list(life_logs)})
