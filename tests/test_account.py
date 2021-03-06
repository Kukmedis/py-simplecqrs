import unittest
from unittest import TestCase
from simple_accounting.account import *


class TestAccount(TestCase):

    def test_emits_debited_event(self):
        account = Account("id")
        events = account.withdraw(10)
        self.assertEqual(len(events), 1)
        self.assertEqual(type(events[0]), AccountDebited)
        self.assertEqual(events[0].amount, 10)
        self.assertEqual(events[0].balance, -10)
        self.assertEqual(events[0].account_id, "id")

    def test_emits_credited_event(self):
        account = Account("id")
        events = account.deposit(10)
        self.assertEqual(len(events), 1)
        self.assertEqual(type(events[0]), AccountCredited)
        self.assertEqual(events[0].amount, 10)
        self.assertEqual(events[0].balance, 10)
        self.assertEqual(events[0].account_id, "id")

    def test_calculates_balance(self):
        account = Account("any_id")
        account.deposit(100)
        account.withdraw(60)
        events = account.deposit(30)
        self.assertEqual(len(events), 1)
        self.assertEqual(type(events[0]), AccountCredited)
        self.assertEqual(events[0].amount, 30)
        self.assertEqual(events[0].balance, 70)

if __name__ == '__main__':
    unittest.main()
