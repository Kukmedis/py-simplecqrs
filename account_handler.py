from account import Account


class AccountHandler():

    event_store = {}

    def deposit_to_account(self, account_id, amount):
        stored_events = self.event_store[account_id]
        account = Account(account_id).replay_changes(stored_events)
        new_events = account.deposit(amount)
        self.event_store[account_id] = stored_events + new_events

    def withdraw_from_account(self, account_id, amount):
        stored_events = self.event_store[account_id]
        account = Account(account_id).replay_changes(stored_events)
        new_events = account.deposit(amount)
        self.event_store[account_id] = stored_events + new_events
