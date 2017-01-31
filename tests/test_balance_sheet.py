import unittest
from datetime import datetime
from unittest import TestCase
from unittest.mock import *
from simple_accounting.balance_sheet import BalanceSheet
from simple_accounting.account import AccountDebited, AccountCredited


class TestBalanceSheet(TestCase):

    @patch('simple_accounting.event_store.EventStore')
    def test_should_provide_aggregated_balances(self, event_store):
        balance_sheet = BalanceSheet(event_store)
        event_store.pull_events.side_effect = self.pull_different_events_side_effect
        balance_sheet.check_for_events()
        self.assertEqual({"1": 5, "2": 40}, balance_sheet.get_balances())

    @patch('simple_accounting.event_store.EventStore')
    def test_should_update_with_new_events(self, event_store):
        balance_sheet = BalanceSheet(event_store)
        event_store.pull_events.side_effect = self.pull_update_with_recent_events_side_effect
        balance_sheet.check_for_events()
        self.assertEqual({"id": 30}, balance_sheet.get_balances())

    def pull_different_events_side_effect(*args, **kwargs):
        if args[1] == AccountDebited:
            return [create_debited_event("1", 10, 5), create_debited_event("2", 10, 20)]
        elif args[1] == AccountCredited:
            return [create_credited_event("2", 20, 40), create_credited_event("1", 5, 15, datetime(2010, 5, 24))]

    def pull_update_with_recent_events_side_effect(*args, **kwargs):
        if args[2] > datetime.now():
            return []
        else:
            return [create_debited_event("id", 20, 20), create_credited_event("id", 10, 30)]


def create_debited_event(id_, amount, balance, timestamp=datetime.now()):
    event = AccountDebited(id_, amount)
    event.balance = balance
    event.timestamp = timestamp
    return event


def create_credited_event(id_, amount, balance, timestamp=datetime.now()):
    event = AccountCredited(id_, amount)
    event.balance = balance
    event.timestamp = timestamp
    return event

if __name__ == '__main__':
    unittest.main()