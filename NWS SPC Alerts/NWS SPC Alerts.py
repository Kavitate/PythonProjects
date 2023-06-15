import requests
from twilio.rest import Client
import schedule
import time

# Your Twilio account SID and Auth Token.
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

# The phone number you want to send the text message to.
to_number = "YOUR_PHONE_NUMBER"

# Default Messages.
day_one_content = "Take a look at the Day One SPC Outlook https://www.pivotalweather.com/maps.php?ds=spc&p=spcd1tor&r=conus"
day_two_content = "Take a look at the Day Two SPC Outlook https://www.pivotalweather.com/maps.php?ds=spc&p=spcd2tor&r=conus"
day_three_content = "Take a look at the Day Three SPC Outlook https://www.pivotalweather.com/maps.php?ds=spc&p=spcd3prob&r=conus"

# Make a request to the website and check for "YOUR_STATE_OR_KEYWORD".
def check_outlook():
    response_day_one = requests.get("https://www.spc.noaa.gov/products/outlook/day1otlk.txt")
    response_day_two = requests.get("https://www.spc.noaa.gov/products/outlook/day2otlk.txt")
    response_day_three = requests.get("https://www.spc.noaa.gov/products/outlook/day3otlk.txt")

    if "YOUR_STATE_OR_KEYWORD" in response_day_one.text:
        send_text_message(day_one_content)

    if "YOUR_STATE_OR_KEYWORD" in response_day_two.text:
        send_text_message(day_two_content)

    if "YOUR_STATE_OR_KEYWORD" in response_day_three.text:
        send_text_message(day_three_content)

# Function to send a text message.
def send_text_message(body):
    client = Client(account_sid, auth_token)
    client.messages.create(to=to_number, from_="YOUR_TWILIO_PHONE_NUMBER", body=body)

# Schedule the task to run every 12 hours.
schedule.every(12).hours.do(check_outlook)

# Run the scheduler continuously.
while True:
    schedule.run_pending()
    time.sleep(1)
