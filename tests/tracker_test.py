from src import tracker

def test_login():
    instance = tracker.Tracker()
    assert instance.login is True
