import unittest
from unittest import TestCase
from simple_accounting.event_store import EventStore
from datetime import datetime


class TestEventStore(TestCase):

    def test_should_save_events(self):
        event_store = EventStore()
        event_store.save_stream(
            "id", [MockEvent("one"), MockEvent("two"), MockEvent("three")])
        self.assertEqual(
            event_store.get_stream("id"),
            [MockEvent("three"), MockEvent("two"), MockEvent("one")])

    def test_should_provide_with_events(self):
        event_store = EventStore()
        event_store.save_stream(
            "id",
            [MockEvent("yes"), AnotherMockEvent("nope"), MockEvent("ofc")])
        event_store.save_stream("other_id", [MockEvent("yesyes")])
        self.assertCountEqual(
            event_store.pull_events(MockEvent, datetime.min),
            [MockEvent("yesyes"), MockEvent("ofc"), MockEvent("yes")])

    def test_should_provide_with_recent_events(self):
        event_store = EventStore()
        event_store.save_stream("id", [MockEvent("no")])
        since = datetime.now()
        event_store.save_stream("id", [MockEvent("yes")])
        self.assertCountEqual(
            event_store.pull_events(MockEvent, since), [MockEvent("yes")])

    def test_should_provide_empty_stream(self):
        event_store = EventStore()
        self.assertEqual(event_store.get_stream("non_existent"), [])

if __name__ == '__main__':
    unittest.main()


class MockEvent:

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return type(self) == type(other) and self.value == other.value

    def __hash__(self):
        return self.value


class AnotherMockEvent:

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return type(self) == type(other) and self.value == other.value

    def __hash__(self):
        return self.value
