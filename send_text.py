# here "from" statement lets us import specific attributes from a module.
# here "twilio.rest" refers to a directory path and
# "TwilioRestClient" is a class in that directory that we are importing. 
from twilio.rest import TwilioRestClient

account_sid = "AC006c934858afb0bb8831d325dca4bc93" # Your Account SID from www.twilio.com/console
auth_token  = "{{ auth_token }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+12345678901",    # Replace with your phone number
    from_="+12345678901") # Replace with your Twilio number

print(message.sid)
