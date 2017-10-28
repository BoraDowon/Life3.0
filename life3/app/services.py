from typing import List
from datetime import datetime
import pytz

from .models import LifeCard

# TODO: do we need to consider class based?


def create_event(data: dict) -> bool:
    """ create log event

    :param data: dict data to be created
    :return: True if succeed
    """
    # TODO: validation, applying timezone from front
    timezone = pytz.timezone('Asia/Seoul')
    lifecard = LifeCard()
    lifecard.title = data['title']
    lifecard.type = data['type']
    lifecard.timestamp = datetime.fromtimestamp(data['timestamp'], tz=timezone)
    lifecard.save()
    return True


def remove_event():
    pass


def modify_event():
    pass


def read_events() -> List[dict]:
    """ Return all events.

    :return: list of events
    """
    lifecards = LifeCard.objects.all().values('title', 'status', 'type', 'timestamp')
    return list(lifecards)
