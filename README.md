# Smart Health Care and Wellness System

## Project Overview
Smart Health Care and Wellness System is a web-based application developed using Python and Flask.
The system helps users check and analyze basic health and wellness parameters and provides a health status report with suitable suggestions.

## Problem Statement
People may not regularly monitor basic health and wellness parameters such as heart rate, temperature, oxygen level, blood pressure, weight, height, sleep, water intake, and exercise.
This project provides a simple system to enter these parameters and obtain an immediate health assessment.

## Objectives
- To collect basic health and wellness information from users.
- To analyze the entered health parameters.
- To calculate Body Mass Index (BMI).
- To identify the user's health status.
- To provide basic health and lifestyle suggestions.
- To generate a simple health report.

## Features
- User health data input
- Heart rate monitoring
- Body temperature monitoring
- Oxygen level monitoring
- Blood pressure monitoring
- Weight and height input
- BMI calculation
- Sleep monitoring
- Water intake monitoring
- Exercise monitoring
- Health status analysis
- Health and wellness suggestions
- Result report generation

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Visual Studio Code

## System Workflow
User Input → Data Processing → Health Analysis → Health Status → Suggestions → Result Display

## Project Modules
1. Input Module
2. Data Processing Module
3. Health Analysis Module
4. Decision-Making Module
5. Suggestion Module
6. Output Module

## BMI Calculation
BMI is calculated using:
BMI = Weight (kg) / Height (m)²

The calculated BMI is used as one of the parameters for health analysis.

## How to Run the Project

### Step 1: Install Python

Install Python on the system.

###Step 2: Install Flask

Open the terminal and run:

```bash
pip install flask
```
Step 3: Run the Application
Open the project folder in Visual Studio Code and run:
python app.py

Step 4: Open the Application
After running the Flask application, open the local URL displayed in the terminal in a web browser.
Example:
http://127.0.0.1:5001

Project Files
app.py – Flask application and backend logic
index.html – User input page
result.html – Displays the health analysis result
requirements.txt – Required Python dependency
README.md – Project overview and setup instructions

Requirements
The project requires Python and Flask.
Install Flask using:
pip install flask

Output
The system accepts health and wellness parameters from the user, processes the information, and displays the resulting health status and wellness suggestions.
Conclusion
The Smart Health Care and Wellness System provides a simple web-based approach for analyzing basic health and wellness information. It demonstrates the use of Python, Flask, HTML, and CSS to develop a health analysis application.
