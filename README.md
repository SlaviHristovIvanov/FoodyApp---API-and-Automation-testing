# FoodyApp---API-Testing-Test-Management
This repository contains API test cases and test management files for the FoodyApp project.
Test Management & Bug Tracking

*** Project Overview ***

FoodyApp is a food ordering and management system that allows users to create, manage, and delete food items. This repository includes:

A Test Management & Bug Tracker (.xls) for manual testing.

A Postman API Collection (.json) for automated API testing.

The Foody1.xls file contains structured test cases for the FoodyApp application, including:

Test Case ID

Test Description

Steps to Reproduce

Expected Result

Actual Result

Bug Status

*** How to Use *** :

Open the .xls file using Microsoft Excel or Google Sheets.

Log test cases and update results as needed.

Track bug reports efficiently.

API Testing with Postman

The FoodyApp.postman_collection.json file includes API test cases for:

User Authentication (/api/User/Authentication)

Create Food Item (/api/Food/Create)

Get All Food Items (/api/Food/All)

Delete Food Item (/api/Food/Delete/{foodId})

User Registration (/api/User/Create)

*** How to Use Postman Collection ***:

Import the Collection:

Open Postman.

Click File > Import and select FoodyApp.postman_collection.json.

Set Up Environment Variables:

Ensure authentication tokens are updated in the request headers.
