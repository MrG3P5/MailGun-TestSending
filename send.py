import requests
import sys

try:
    key = sys.argv[1]
    domain = sys.argv[2]
    req = requests.post(f"https://api.mailgun.net/v3/{domain}/messages", auth=("api", f"{key}"), data={"from": f"Support <mailgun@{domain}>", "to": ["xmrg3p5@gmail.com"], "subject": "Test mailgun", "text": "Testing mailgun"})
    print(req.json())
except:
    print(f"Usage : python3 {sys.argv[0]} <Key> <Domain>")
