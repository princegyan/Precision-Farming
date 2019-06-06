from twilio.rest import Client


def callUser():
    account_sid = "AC4228efb1dd6b0ba7d00d0e2bad0755f0"
    auth_token = "5ff9d3bfb250b4777496ea4f934deb20"
    client = Client(account_sid, auth_token)
    call = client.calls.create(
        url="http://5a5fdf61.ngrok.io/answer",  # this links to voice to be played
         from_="+15866660800",
         to="+233557954540",
     )

    print(call.sid)
    #print("Hello ", parameter)
