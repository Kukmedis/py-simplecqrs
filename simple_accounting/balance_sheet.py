from datetime import datetime

from simple_accounting.account import AccountDebited, AccountCredited


class BalanceSheet():

    __document_store = {}

    __time_last_pulled = datetime.min

    def __init__(self, event_store):
        self.event_store = event_store

    def update_balance(self, event):
        self.__document_store[event.account_id] = [event.balance]

    def check_for_events(self):
        pull_time = datetime.now()
        debited_events = self.event_store.pull_events(AccountDebited, self.__time_last_pulled)
        credited_events = self.event_store.pull_events(AccountCredited, self.__time_last_pulled)
        all_events = sorted(debited_events + credited_events, key = lambda event: event.timestamp)
        self.update_balance(all_events[-1])
        self.__time_last_pulled = pull_time
