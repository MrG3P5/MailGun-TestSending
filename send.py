import requests
import sys

try:
    key = sys.argv[1]
    domain = sys.argv[2]
    to_mail = sys.argv[3]
    req = requests.post(f"https://api.mailgun.net/v3/{domain}/messages", auth=("api", f"{key}"), data={"from": f"Support <mailgun@{domain}>", "to": [to_mail], "subject": "Test mailgun", "text": "Testing mailgun"})
    print(req.json())
except:
    print(f"Usage : python3 {sys.argv[0]} <Key> <Domain> <To_Mail>")
