#PyGithub
from github import Github
import os
from pprint import pprint

token = os.getenv('GITHUB_TOKEN', '...')
g = Github(token)
repo = g.get_repo("devesh-todarwal/Github-API")
issues = repo.get_issues(state="open")
pprint(issues.get_page(0))

data = {
    "public": True,
    "files": {
        "code.py": {
            "content": "print('some code')"
        },
    }
}
headers = {'Authorization': f'token {token}'}
r = requests.post(query_url, headers=headers, data=json.dumps(data))
pprint(r.json())
