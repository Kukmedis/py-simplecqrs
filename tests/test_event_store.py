import unittest
from unittest import TestCase
from simple_accounting.event_store import EventStore
from datetime import datetime


class TestEventStore(TestCase):

    def test_should_save_events(self):
        event_store = EventStore()
        event_store.save_stream("id", [MockEvent("one"), MockEvent("two"), MockEvent("three")])
        self.assertEqual([MockEvent("one"), MockEvent("two"), MockEvent("three")], event_store.get_stream("id"))

    def test_should_provide_with_events(self):
        event_store = EventStore()
        event_store.save_stream("id", [MockEvent("yes"), AnotherMockEvent("nope"), MockEvent("ofc")])
        event_store.save_stream("other_id",[ MockEvent("yesyes")])
        self.assertEqual([MockEvent("yes"), MockEvent("ofc"), MockEvent("yesyes")],
                         event_store.pull_events(MockEvent, datetime.min))

    def test_should_provide_with_recent_events(self):
        event_store = EventStore()
        event_store.save_stream("id", [MockEvent("no")])
        since = datetime.now()
        event_store.save_stream("id", [MockEvent("yes")])
        self.assertEqual([MockEvent("yes")], event_store.pull_events(MockEvent, since))


if __name__ == '__main__':
    unittest.main()


class MockEvent:

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


class AnotherMockEvent:

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value