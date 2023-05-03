import requests
import sys

YOUR_MAIL_HERE = "example@gmail.com"

try:
    key = sys.argv[1]
    domain = sys.argv[2]
    req = requests.post(f"https://api.mailgun.net/v3/{domain}/messages", auth=("api", f"{key}"), data={"from": f"Support <mailgun@{domain}>", "to": [YOUR_MAIL_HERE], "subject": "Test mailgun", "text": "Testing mailgun"})
    print(req.json())
except:
    print(f"Usage : python3 {sys.argv[0]} <Key> <Domain>")
