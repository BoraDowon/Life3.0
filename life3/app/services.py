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
    #lifecards = LifeCard.objects.order_by('timestamp').reverse().values('id', 'title', 'status', 'type', 'timestamp')
    # TODO: in fureture, the function will get a information of timezone
    tz = pytz.timezone('Asia/Seoul')
    query_lifecards = LifeCard.objects.order_by('timestamp').reverse().values('id', 'title', 'status', 'type', 'timestamp')

    for lifecard in list(query_lifecards):
        utc_to_local = lifecard['timestamp'].astimezone(tz=tz)
        utc_to_local_str = utc_to_local.strftime('%Y-%m-%d %H:%M')
        lifecard.update({'time_to_display': utc_to_local_str})
    return list(query_lifecards)
