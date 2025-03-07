# FoodyApp API and Automation Testing
This repository contains API test cases, automation tests, and test management files for the TestHub project.

Project Overview

TestHub is a project designed to streamline the process of test automation, API testing, and test management. It includes the following:

Test Management: Structured test cases and bug tracking.
API Testing: Automated tests for testing API endpoints.
Automation Testing: Functional tests using Pytest for validating application behavior.
This repository aims to provide a comprehensive solution for testing by combining manual test management, automated API tests, and continuous integration with test automation.

 Repository Structure

FoodyApp-API-Automation
┣ 📂 automation_tests/
┃ ┣ 📜 __init__.py
┃ ┣ 📜 test_email_format_validation.py        # Email format validation tests
┃ ┣ 📜 test_field_length.py                   # Field length validation tests
┃ ┣ 📜 test_login_functionality.py            # Login functionality tests
┃ ┣ 📜 test_password_strength.py              # Password strength validation tests
┃ ┣ 📜 test_session_expiry.py                 # Session timeout validation tests
┃ ┣ 📜 test_sql_injection.py                  # SQL injection prevention tests
┣ 📜 TestHub-Test-Management.xlsx             # Test cases & bug tracking
┣ 📜 TestHub-API-Collection.postman_collection.json  # Postman API testing collection
┣ 📜 README.md                                # Project documentation
Test Management & Bug Tracking

The TestHub-Test-Management.xlsx file contains structured test cases and bug tracking for TestHub. It includes:

Test Case ID: Unique identifier for each test case.
Test Description: Brief explanation of the test.
Steps to Reproduce: Instructions to execute the test case.
Expected Result: What the test case is expected to return.
Actual Result: The actual outcome when the test is executed.
Bug Status: Track whether a bug has been found.
📌 How to Use:
Open the TestHub-Test-Management.xlsx file using Microsoft Excel or Google Sheets.
Log new test cases and update results as testing progresses.
Use the bug status section to track and manage any defects found during testing.
🔥 API Testing with Postman

The TestHub-API-Collection.postman_collection.json file contains API test cases for the TestHub project. These tests validate key functionalities of the API endpoints.

🚀 How to Use the Postman Collection:
Import the Collection:
Open Postman.
Click File > Import and select the TestHub-API-Collection.postman_collection.json file.
Set Up Authentication:
Update the Bearer Token in the request headers as per your authentication method.
Run API Tests:
Click Send to test each endpoint.
View the responses and debug issues as needed.
API Endpoints Tested:
User Authentication (/api/User/Authentication)
Create Idea (/api/Idea/Create)
Get All Ideas (/api/Idea/All)
Edit Idea (/api/Idea/Edit?ideaId={id})
Delete Idea (/api/Idea/Delete?ideaId={id})
🤖 Automation Testing with Pytest

The automation_tests/ folder contains automated test scripts written using Pytest for validating various functionalities of the TestHub application.

🧪 Implemented Tests:
Email Format Validation (test_email_format_validation.py): Validates the correct format of email addresses.
Field Length Validation (test_field_length.py): Ensures that input fields meet minimum length requirements.
Login Functionality (test_login_functionality.py): Verifies correct login functionality for valid and invalid users.
Password Strength Validation (test_password_strength.py): Tests that passwords meet the security criteria.
Session Expiry Handling (test_session_expiry.py): Ensures that the session expires correctly after a certain period of inactivity.
SQL Injection Prevention (test_sql_injection.py): Tests that inputs are protected against SQL injection attacks.

Tools & Technologies

Pytest: For automated functional testing.
Postman: For API testing and collection management.
Excel/Google Sheets: For manual test management and bug tracking.
