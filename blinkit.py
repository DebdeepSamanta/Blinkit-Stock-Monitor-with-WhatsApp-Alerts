import requests
import time
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

PRODUCT_URL = os.getenv("Product_URL")
TWILIO_SID = os.getenv("Twilio_id")
TWILIO_TOKEN = os.getenv("Twilio_token")
TWILIO_NUMBER = os.getenv("Twilio_number")   # given by Twilio
YOUR_NUMBER = os.getenv("my_number")    # your Indian mobile number


session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en;q=0.9",
    "Referer": "https://blinkit.com/",
})

def is_in_stock():
    try:
        r = session.get(PRODUCT_URL, timeout=15)
        return "Add to cart" in r.text    
    except:
        return False

def send_whatsapp():
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    client.messages.create(
        body="🚨 BLINKIT IN STOCK NOW! Order immediately!",
        from_=f"whatsapp:{TWILIO_NUMBER}",
        to=f"whatsapp:{YOUR_NUMBER}"
    )
    print("✅ WhatsApp sent!")

print("🔍 Monitoring started...")
while True:
    print("Checking...")
    if is_in_stock():
        print("🟢 IN STOCK!")
        send_whatsapp()
        time.sleep(300)  # wait 5 mins before next alert
    else:
        print("🔴 Out of stock. Waiting 30s...")
    time.sleep(30)