from datetime import datetime


class EventStore():

    __event_store = {}

    def save(self, id_, events):
        for event in events:
            event.timestamp = datetime.now()
        self.__event_store[id_] += events

    def get(self, id_):
        return self.__event_store[id_]

    def pull_events(self, event_type, since):
        return [event for i in self.__event_store.values() for event in i
                if type(event) is event_type and event.timestamp >= since]