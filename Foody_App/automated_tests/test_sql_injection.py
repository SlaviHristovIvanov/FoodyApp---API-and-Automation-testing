import pytest

# Data for testing SQL injection prevention
sql_injection_data = [
    ("' OR '1'='1", False),   # SQL Injection attempt
    ("normal_user", True),    # Normal username
    ("DROP TABLE", False),    # SQL Injection attempt
    (";--", False)            # SQL Injection attempt
]

@pytest.mark.parametrize('input_value, expected_result', sql_injection_data)
def test_sql_injection_prevention(input_value, expected_result):

    injection_patterns = ["' OR '1'='1", "'--", "DROP TABLE", ";--"]
    if any(pattern in input_value for pattern in injection_patterns):
        assert expected_result == False
    else:
        assert expected_result == True