#!/usr/bin/env python3
import requests
from pprint import pprint
from secrets import GITHUB_TOKEN, REPO_PATH, GITHUB_USER
import argparse
import os

#Parsing arguments -> Name of the repository, Visibility of the repository (Private/Public)
parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
parser.add_argument("--private", "-p", dest="is_private", action="store_true")

args = parser.parse_args()

repo_name = args.name
is_private = args.is_private

#Creating the repo based on received arguments
API_URL = "https://api.github.com"
#REPO_PATH = <Insert Path To Store Repository Locally>
#GITHUB_USER= <insert Github username>

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

# Adding README to the Repo and creating a local clone + Linking local repo and remote repo.
try:
    os.chdir(REPO_PATH)
    os.system("mkdir " + repo_name)
    os.chdir(REPO_PATH + repo_name)
    os.system("git init")
    os.system("git remote add origin https://github.com/" + GITHUB_USER + "/" + repo_name + ".git")
    os.system("git branch -M main")
    os.system("echo '# " + repo_name + "' >> README.md")
    os.system("git add . && git commit -m 'Initial Commit' && git push origin main")
except FileExistsError as err:
    raise SystemExit(err)