from datetime import datetime


class EventStore():

    def __init__(self):
        self.__event_store = {}

    def save_stream(self, id_, events):
        for event in events:
            event.timestamp = datetime.now()
        old_events = self.__event_store.get(id, [])
        self.__event_store[id_] = old_events + events

    def get_stream(self, id_):
        return self.__event_store.get(id_, [])

    def pull_events(self, since, event_type):
        return [event for events in self.__event_store.values() for event in events
                if type(event) is event_type and event.timestamp >= since]