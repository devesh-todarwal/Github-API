import requests
from pprint import pprint
from secrets import GITHUB_TOKEN
import argparse

#Parsing arguments -> Name of the repository, Visibility of the repository (Private/Public)
parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
parser.add_argument("--private", "-p", dest="is_private", action="store_true")

args = parser.parse_args()

repo_name = args.name
is_private = args.is_private

#Creating the repo based on received arguments
API_URL = "https://api.github.com"

if is_private:
    payload = '{"name":"' + repo_name + '", "private": true}'
else:
    payload = '{"name":"' + repo_name + '", "private": false}'

headers = {
    "Authorization" : "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.v3+json"
}
try:
    r = requests.post(API_URL+"/user/repos",data=payload,headers=headers)
    r.raise_for_status()
    #pprint(r.json())
except requests.exceptions.RequestException as err:
    raise SystemExit(err)

