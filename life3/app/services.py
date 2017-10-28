from typing import List

from .models import LifeLog

# TODO: do we need to consider class based?


def create_event(data: dict) -> bool:
    """ create log event

    :param data: dict data to be created
    :return: True if succeed
    """
    # TODO: validation
    life_log = LifeLog(title=data['title'], status=data['status'], type=data['type'])
    life_log.save()
    return True


def remove_event():
    pass


def modify_event():
    pass


def read_events() -> List[dict]:
    """ Return all events.

    :return: list of events
    """
    life_logs = LifeLog.objects.all().values('title', 'status', 'type', 'timestamp')
    return list(life_logs)
