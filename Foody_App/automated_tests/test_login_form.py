import pytest

login_data = [
    ("testuser@example.com", "Test@1234", True),   #email, password
    ("wronguser@example.com", "Test@1234", False),
    ("testuser@example.com", "wrongpass", False),
    ("", "Test@1234", False),
    ("testuser@example.com", "", False)
]


@pytest.mark.parametrize("email, password, expected_result", login_data)
def test_user_login(email, password, expected_result):
    valid_email = "testuser@example.com"
    valid_password = "Test@1234"

    if email == valid_email and password == valid_password:
        assert expected_result == True
    else:
        assert expected_result == False