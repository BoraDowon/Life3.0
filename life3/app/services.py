from typing import List
from datetime import datetime
import pytz

from .models import LifeLog

# TODO: do we need to consider class based?


def create_event(data: dict) -> bool:
    """ create log event

    :param data: dict data to be created
    :return: True if succeed
    """
    # TODO: validation, applying timezone from front
    timezone = pytz.timezone('Asia/Seoul')
    life_log = LifeLog()
    life_log.title = data['title']
    life_log.type = data['type']
    life_log.timestamp = datetime.fromtimestamp(data['timestamp'], tz=timezone)
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
