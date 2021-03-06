from typing import List
from datetime import datetime
import pytz

from django.core.exceptions import ObjectDoesNotExist

from .models import LifeCard

# TODO: do we need to consider class based?


class LifeCardService:

    @staticmethod
    def _validate_card(data: dict) -> bool:
        """ validate requested card
        :param data: card data
        :return: True if validation pass
        """
        return len(list(filter(lambda t: t[0] == data['type'], LifeCard.TYPE_INFO))) > 0

    @staticmethod
    def _deco_time_to_display(life_card: dict) -> dict:
        """ Decorate 'time_to_display' and remove 'timestamp'
        """
        life_card['time_to_display'] = int(life_card['timestamp'].timestamp())
        del life_card['timestamp']
        del life_card['status']
        return life_card

    def read_cards(self) -> List[dict]:
        """ Return all events.

        :return: list of events
        """
        # TODO: in future, the function will get a information of timezone
        query = LifeCard.objects.all().values('id', 'title', 'type', 'status', 'timestamp')
        active_lifecard = [item for item in list(query) if item['status'] == '0']
        return list(map(self._deco_time_to_display, active_lifecard))

    def read_card(self, pk) -> dict:
        pass

    def create_card(self, data: dict) -> bool:
        """ create log event

            :param data: dict data to be created
            :return: True if succeed
            """
        # TODO: applying timezone from front
        if not self._validate_card(data):
            return False

        life_card = LifeCard()
        life_card.type = data['type']
        life_card.title = data['title']
        life_card.status = '0'
        life_card.timestamp = datetime.fromtimestamp(data['timestamp'], tz=pytz.timezone('UTC'))
        life_card.save()
        return True

    def modify_card(self, data: dict) -> bool:
        '''
        try:
            lifecard = LifeCard.objects.get(pk=data['id'])
        except ObjectDoesNotExist:
            return False

        type_info = LifeCard.TYPE_INFO
        type_validation = [i for i, v in enumerate(type_info) if v[0] == data['type']]
        if type_validation:
            lifecard.type = data['type']
        else:
            return False

        lifecard.title = data['title']
        lifecard.save()
        return True
        '''
        pass

    def remove_card(self, pk) -> bool:
        '''
        try:
            lifecard = LifeCard.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return False

        lifecard.status = '1'
        lifecard.save()
        return True
        '''
        pass


def create_event(data: dict) -> bool:
    """ create log event

    :param data: dict data to be created
    :return: True if succeed
    """
    # TODO: applying timezone from front
    if not _validate_card(data):
        return False

    life_card = LifeCard()
    life_card.type = data['type']
    life_card.title = data['title']
    life_card.status = '0'
    life_card.timestamp = datetime.fromtimestamp(data['timestamp'], tz=pytz.timezone('UTC'))
    life_card.save()
    return True


def _validate_card(data: dict) -> bool:
    """ validate requested card
    :param data: card data
    :return: True if validation pass
    """
    return len(list(filter(lambda t: t[0] == data['type'], LifeCard.TYPE_INFO))) > 0


def remove_event(pk) -> bool:
    '''
    try:
        lifecard = LifeCard.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return False

    lifecard.status = '1'
    lifecard.save()
    return True
    '''
    pass


def modify_event(data: dict) -> bool:
    '''
    try:
        lifecard = LifeCard.objects.get(pk=data['id'])
    except ObjectDoesNotExist:
        return False

    type_info = LifeCard.TYPE_INFO
    type_validation = [i for i, v in enumerate(type_info) if v[0] == data['type']]
    if type_validation:
        lifecard.type = data['type']
    else:
        return False

    lifecard.title = data['title']
    lifecard.save()
    return True
    '''
    pass


def read_events() -> List[dict]:
    """ Return all events.

    :return: list of events
    """
    # TODO: in future, the function will get a information of timezone
    query = LifeCard.objects.all().values('id', 'title', 'type', 'status', 'timestamp')
    active_lifecard = [item for item in list(query) if item['status'] == '0']
    return list(map(_deco_time_to_display, active_lifecard))


def _deco_time_to_display(life_card: dict) -> dict:
    """ Decorate 'time_to_display' and remove 'timestamp'
    """
    life_card['time_to_display'] = int(life_card['timestamp'].timestamp())
    del life_card['timestamp']
    del life_card['status']
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


