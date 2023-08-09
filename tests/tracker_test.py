from src import tracker

def test_main():
    assert tracker.main(2,3) == 6
    assert tracker.main(2,4) == 8