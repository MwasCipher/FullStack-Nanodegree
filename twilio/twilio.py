from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC8ab2eb9e63cd7bd88a5d97732fbf301b"
# Your Auth Token from twilio.com/console
auth_token  = "c30383cc855b6b749f92978ab314c863"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+254724657646", 
    from_="(772) 783-9699",
    body="Hello Mufasa, I am You From The Future, Don't Lose Interest in The Dumb bitch!!!! She is YOUR LIFE")

print(message.sid)