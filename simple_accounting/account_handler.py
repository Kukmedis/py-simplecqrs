from simple_accounting.account import Account


class AccountHandler():

    def __init__(self, event_store):
        self.event_store = event_store

    def deposit_to_account(self, account_id, amount):
        stored_events = self.event_store.get_stream(account_id)
        account = Account(account_id, stored_events)
        new_events = account.deposit(amount)
        self.event_store.save_stream(account_id, new_events)

    def withdraw_from_account(self, account_id, amount):
        stored_events = self.event_store.get_stream(account_id)
        account = Account(account_id, stored_events)
        new_events = account.withdraw(amount)
        self.event_store.save_stream(account_id, new_events)

