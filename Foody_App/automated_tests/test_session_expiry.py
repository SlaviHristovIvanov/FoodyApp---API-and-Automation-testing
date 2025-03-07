import pytest


session_data = [
    (10, False),
    (22, False),
    (29, False),
    (30, True)
]

@pytest.mark.parametrize('inactive_duration, expected_result', session_data)
def test_session_expiry(inactive_duration, expected_result):
    session_timeout = 30
    if inactive_duration >= session_timeout:
        assert expected_result == True
    else:
        assert expected_result == False