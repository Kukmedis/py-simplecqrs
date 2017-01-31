import unittest
from unittest import TestCase
from unittest.mock import *
from simple_accounting.account_handler import *
from simple_accounting.account import *


class TestAccountHandler(TestCase):

    @patch('simple_accounting.event_store.EventStore')
    def test_saves_account_debited_on_withdrawal(self, event_store):
        event_store.get_stream.side_effect = self.get_events_side_effect
        account_handler = AccountHandler(event_store)
        account_handler.withdraw_from_account("id", 10)
        self.assertTrue(event_store.save_stream.called)
        event = event_store.save_stream.call_args_list[0][0][0][0]
        self.assertEqual(event.amount, 10)
        self.assertEqual(event.account_id, "id")
        self.assertEqual(type(event), AccountDebited)

    @patch('simple_accounting.event_store.EventStore')
    def test_saves_account_credited_on_deposit(self, event_store):
        event_store.get_stream.side_effect = self.get_events_side_effect
        account_handler = AccountHandler(event_store)
        account_handler.deposit_to_account("id", 20)
        self.assertTrue(event_store.save_stream.called)
        event = event_store.save_stream.call_args_list[0][0][0][0]
        self.assertEqual(event.amount, 20)
        self.assertEqual(event.account_id, "id")
        self.assertEqual(type(event), AccountCredited)

    def get_events_side_effect(*args, **kwargs):
        if args[0] == "id":
            return [AccountCredited("id", 10)]

if __name__ == '__main__':
    unittest.main()