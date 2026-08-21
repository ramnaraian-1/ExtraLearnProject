
# ExtraaLearn Lead Conversion Prediction API

## Business Objective

ExtraaLearn is an EdTech startup that generates a large number of
leads through different online and offline channels.

The objective of this machine learning application is to identify
leads that are more likely to convert into paid customers.

This helps ExtraaLearn prioritize sales and marketing resources
towards high-potential leads.

## Machine Learning

The project builds machine learning models to predict whether a lead
will convert into a paid customer.

The final selected model is serialized using Joblib.

The serialized model contains the required preprocessing and
machine learning pipeline.

## Backend

The machine learning model is exposed through a Flask REST API.

## Technology Stack

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Gunicorn
- Docker
- Render

## API Endpoints

### Home

GET /

### Health Check

GET /health

### Prediction

POST /predict

## Example Prediction Request

{
    "age": 25,
    "current_occupation": "Professional",
    "first_interaction": "Website",
    "profile_completed": "High",
    "website_visits": 5,
    "time_spent_on_website": 1200,
    "page_views_per_visit": 4.5,
    "last_activity": "Email Activity",
    "print_media_type1": "No",
    "print_media_type2": "No",
    "digital_media": "Yes",
    "educational_channels": "Yes",
    "referral": "No"
}

## Example Response

{
    "prediction": 1,
    "status": "Converted",
    "conversion_probability": 0.82
}

## Deployment

The Flask application is containerized using Docker and deployed
as a web service.

The deployment platform can be Render Free Web Service.
