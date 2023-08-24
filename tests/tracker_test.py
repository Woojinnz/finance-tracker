from src import tracker

def test_login():
    instance = tracker.Tracker()
    assert instance.login_successful is True
    print("Login is succesful!")
