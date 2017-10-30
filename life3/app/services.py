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
    timezone = pytz.timezone('UTC')
    lifecard = LifeCard()
    type_info = LifeCard.TYPE_INFO
    type_validation = [i for i, v in enumerate(type_info) if v[0] == data['type']]
    if type_validation:
        lifecard.type = data['type']
    else:
        return False
    lifecard.title = data['title']
    lifecard.status = '0'
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
    # TODO: in future, the function will get a information of timezone
    query = LifeCard.objects.all().values('id', 'title', 'type', 'timestamp')
    return list(map(_deco_time_to_display, list(query)))


def _deco_time_to_display(life_card: dict) -> dict:
    """ Decorate 'time_to_display' and remove 'timestamp'
    """
    timezone = pytz.timezone('Asia/Seoul')
    life_card['time_to_display'] = life_card['timestamp'].astimezone(tz=timezone).strftime('%Y-%m-%d %H:%M')
    del life_card['timestamp']
    return life_card


def read_statistics():
    query = LifeCard.objects.all().values('id', 'type', 'timestamp')
    work_count = 0
    play_count = 0
    rest_count = 0
    for item in query:
        if item['type'] == 'R':
            rest_count += 1
        if item['type'] == 'W':
            work_count += 1
        if item['type'] == 'P':
            play_count += 1

    work_dict = {'title': '일', 'type': 'W', 'count': work_count}
    play_dict = {'title': '놀이', 'type': 'P', 'count': play_count}
    rest_dict = {'title': '휴식', 'type': 'R', 'count': rest_count}

    return [work_dict, play_dict, rest_dict]


