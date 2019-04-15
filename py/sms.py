from twilio.rest import Client
from api import account_sid, auth_token, twilio_number

client = Client(account_sid, auth_token)

message = client.messages.create(from_=twilio_number,
                                 body='hello',
                                 to='+19164775363')
