class EventStore():

    __event_store = {}

    def save(self, id_, events):
        self.__event_store[id_] += events

    def get(self, id_):
        return self.__event_store[id_]