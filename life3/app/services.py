import json

from .models import LifeLog
from .data import  LifeLogDto

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
    # FIXME: implement logic and serializer
    query_set = LifeLog.objects.all()
    fields = ['title', 'status', 'type']
    query_list = list()
    for query_item in query_set:
        item = dict()
        for key in fields:
            if getattr(query_item, key):
                item[key] = getattr(query_item, key)
        query_list.append(item)
    json_data = json.dumps(query_list)
    return json_data
