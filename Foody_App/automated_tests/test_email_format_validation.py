import pytest
import re

email_data = [
    ('some.email@gmail.com', True),        # Valid email
    ('invalid-email.com', False),          # Invalid email (no '@')
    ('@invalid.com', False),               # Invalid email (no username before '@')
    ('some.email@com', False),             # Invalid email (no top-level domain)
    ('some.email@subdomain.domain.com', True),  # Valid email with subdomain
    ('another.valid.email@domain.co.uk', True), # Valid email with multiple TLD parts
    ('test@domain', False),                # Invalid email (no TLD)
    ('test@.com', False),                  # Invalid email (TLD starts with a dot)
]

email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

@pytest.mark.parametrize('email, expected_result', email_data)
def test_email_validation(email, expected_result):
    if re.match(email_regex, email):
        assert expected_result == True
    else:
        assert expected_result == False
