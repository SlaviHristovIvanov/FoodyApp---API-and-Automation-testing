import pytest

email_data = [
    ('some.email@gmail.com', True),
    ('invalid-email.com', False),
    ('@invalid.com', False),
    ('some.email@com', False)
]

@pytest.mark.parametrize('email, expected_result', email_data)

def test_email_validation(email, expected_result):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        assert expected_result == True
    else:
        assert expected_result == False