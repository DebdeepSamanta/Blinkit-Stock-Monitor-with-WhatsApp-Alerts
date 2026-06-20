# Blinkit Stock Monitor with WhatsApp Alerts

A Python-based stock monitoring bot that continuously checks the availability of a Blinkit product and sends WhatsApp notifications using Twilio whenever the product comes back in stock.

## Features

* Continuous stock monitoring
* Automated WhatsApp notifications
* Environment variable based configuration
* Persistent HTTP session for efficient requests
* Custom request headers to mimic browser traffic
* Easy deployment on local machine, VPS, or cloud server

---

## Tech Stack

* Python
* Requests
* Twilio WhatsApp API
* Python Dotenv

---

## Project Structure

```text
blinkit-stock-monitor/
│
├── monitor.py
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd blinkit-stock-monitor
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
Product_URL=https://blinkit.com/prn/your-product-url

Twilio_id=YOUR_TWILIO_ACCOUNT_SID
Twilio_token=YOUR_TWILIO_AUTH_TOKEN
Twilio_number=+14155238886

my_number=+91XXXXXXXXXX
```

---

## Running the Application

```bash
python monitor.py
```

Expected output:

```text
🔍 Monitoring started...
Checking...
🔴 Out of stock. Waiting 30s...
```

When stock is available:

```text
🟢 IN STOCK!
✅ WhatsApp sent!
```

---

## Continuous Monitoring

The script runs continuously until manually stopped.

Stop monitoring using:

```bash
Ctrl + C
```

---

## Twilio WhatsApp Setup

Before receiving messages, join the Twilio WhatsApp Sandbox:

1. Open WhatsApp.
2. Send the provided sandbox code to:

```text
+1 415 523 8886
```

3. Wait for the confirmation message.

---

## Future Enhancements

* Email notifications
* Telegram alerts
* Discord alerts
* Multiple product monitoring
* Docker deployment
* Cloud deployment on Azure/AWS
* Web dashboard for monitoring

---

## Disclaimer

This project is intended for educational and personal use. Website structures may change over time, requiring updates to the stock detection logic.


## Motivation 

For hunting HotWheels, which I try to get everytime but I am always late.