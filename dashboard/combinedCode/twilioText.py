from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC1c805cf3f05a5ab71eb7c21e35b7af33'
auth_token = 'd26f62278aae23748d78a7122674b71a'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="This Is From IntelFarm...{{label}} needs to attended to check the latest reading {{label}}{{reading}} here {{weblink}}",
                     from_='+19513833556',
                     to='+233274008316'
                 )

print(message.sid)