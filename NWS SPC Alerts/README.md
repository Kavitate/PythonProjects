<h1 align="center">:tornado: :iphone: NWS SPC Text Message Alerts :iphone: :tornado:</h1>

## :page_facing_up: About

This program uses [Twilio](https://www.twilio.com/en-us) to send you text message alerts whenever your state or keyword are utilized in an [NWS SPC Outlook](https://www.spc.noaa.gov/products/outlook/).

The program is currently set to review the SPC Outlooks every 12 hours. However, this variable can be changed as needed.
_________________________________________________________________________________________________________________________________________________
The below variables must be updated prior to running the program:

- "YOUR_ACCOUNT_SID" - Line 7
- "YOUR_AUTH_TOKEN" - Line 8
- "YOUR_STATE_OR_KEYWORD" - Lines 24, 27, and 30.
- "YOUR_TWILIO_PHONE_NUMBER" - Line 36
