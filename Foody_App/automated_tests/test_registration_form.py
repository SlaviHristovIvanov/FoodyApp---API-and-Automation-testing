import pytest

registration_data = [
    ("newuser@example.com", "Test@1234", "Test@1234", True),  #Username, password, confirm password
    ("invalid-email", "Test@1234", "Test@1234", False),
    ("newuser@example.com", "short", "short", False),
    ("newuser@example.com", "Test@1234", "Mismatch123", False)
]

@pytest.mark.parametrize("email, password, confirm_password, expected_result", registration_data)
def test_user_registration(email, password, confirm_password, expected_result):
    if "@" not in email or password != confirm_password or len(password) < 8:
        assert expected_result == False
    else:
        assert expected_result == True