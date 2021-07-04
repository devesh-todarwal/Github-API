import requests
from pprint import pprint
from secrets import GITHUB_TOKEN

API_URL = "https://api.github.com"
payload = '{"name":"Testname"}'
headers = {
    "Authorization" : "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.v3+json"
}
r = requests.post(API_URL+"/user/repos",data=payload,headers=headers)

pprint(r.json())
