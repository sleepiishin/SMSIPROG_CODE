import requests

IPROG_URL = "https://www.iprogsms.com/api/v1/sms_messages"

API_TOKEN = "f454e02b07419f74c316637d63102127ba910725"
PHONE_NUMBER = "639165998549"
MESSAGE = "Hello this is from Nelson, This message is for  SMS API For my Thesis!"

payload = {
    "phone_number": PHONE_NUMBER,
    "message": MESSAGE,
    "api_token": API_TOKEN
}

print("Sending SMS...")  # Debug message

response = requests.post(IPROG_URL, json=payload)

print("Status Code:", response.status_code)   # Show HTTP status
print("Response:", response.text)             # Show full server reply
