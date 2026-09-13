# Salary Prediction Model

A Flask web application that predicts salary from years of experience using a trained Linear Regression model.

## Project structure

Salary-Prediction-Deployment/
├── app.py
├── reg_model.pkl
├── requirements.txt
├── README.md
└── templates/
    └── index.html

## Run locally

Install dependencies:

    pip install -r requirements.txt

Run the application:

    python app.py

Open:

    http://127.0.0.1:5000/

## Deploy on Render

Create a new Web Service from this GitHub repository.

Build Command:

    pip install -r requirements.txt

Start Command:

    gunicorn app:app

The application uses the PORT environment variable supplied by Render.
