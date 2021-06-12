from credentials import account_sid, auth_token, to_send_number, twilio_number
from twilio.rest import Client


client = Client(account_sid,auth_token)

my_msg = "Hi, I can't message you from my phone number. How are you doing?"

message = client.messages.create(to=to_send_number, from_=twilio_number, body=my_msg)

print(message.to)