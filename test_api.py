
import requests


# ============================================================
# CHANGE THIS URL AFTER RENDER DEPLOYMENT
# ============================================================

BASE_URL = "http://127.0.0.1:10000"


# ============================================================
# TEST HOME ENDPOINT
# ============================================================

print("=" * 60)
print("TEST 1: HOME ENDPOINT")
print("=" * 60)

response = requests.get(
    BASE_URL + "/"
)

print("Status Code:", response.status_code)

print("Response:")
print(response.json())


# ============================================================
# TEST HEALTH ENDPOINT
# ============================================================

print("\n" + "=" * 60)
print("TEST 2: HEALTH ENDPOINT")
print("=" * 60)

response = requests.get(
    BASE_URL + "/health"
)

print("Status Code:", response.status_code)

print("Response:")
print(response.json())


# ============================================================
# TEST PREDICTION ENDPOINT
# ============================================================

print("\n" + "=" * 60)
print("TEST 3: PREDICTION ENDPOINT")
print("=" * 60)


lead = {

    "age": 25,

    "current_occupation":
        "Professional",

    "first_interaction":
        "Website",

    "profile_completed":
        "High",

    "website_visits":
        5,

    "time_spent_on_website":
        1200,

    "page_views_per_visit":
        4.5,

    "last_activity":
        "Email Activity",

    "print_media_type1":
        "No",

    "print_media_type2":
        "No",

    "digital_media":
        "Yes",

    "educational_channels":
        "Yes",

    "referral":
        "No"
}


response = requests.post(

    BASE_URL + "/predict",

    json=lead

)

print("Status Code:", response.status_code)

print("Response:")
print(response.json())
