#!pip install PyGithub requests

from github import Github
import os
from pprint import pprint

token = os.getenv('GITHUB_TOKEN', '...')
g = Github(token)
repo = g.get_repo("MartinHeinz/python-project-blueprint")
issues = repo.get_issues(state="open")
pprint(issues.get_page(0))

#sample o/p

# [{'assignee': None,
#   'body': 'Some Markdown text...',
#   'comments': 0,
#   'comments_url': 'https://api.github.com/repos/MartinHeinz/python-project-blueprint/issues/10/comments',
#   'created_at': '2020-04-20T22:16:33Z',
#   'html_url': 'https://github.com/MartinHeinz/python-project-blueprint/issues/10',
#   'id': 603571386,
#   'labels': [],
#   'labels_url': 'https://api.github.com/repos/MartinHeinz/python-project-blueprint/issues/10/labels{/name}',
#   'milestone': None,
#   'node_id': 'MDU6SXNzdWU2MDM1NzEzODY=',
#   'repository_url': 'https://api.github.com/repos/MartinHeinz/python-project-blueprint',
#   'state': 'open',
#   'title': 'configure_project script not working',
#   'url': 'https://api.github.com/repos/MartinHeinz/python-project-blueprint/issues/10',
#   'user': {...}},
#   ...
# ]

#Create an Issue

g = Github(token)
repo = g.get_repo("MartinHeinz/python-project-blueprint")
i = repo.create_issue(
    title="Issue Title",
    body="Text of the body.",
    assignee="MartinHeinz",
    labels=[
        repo.get_label("good first issue")
    ]
)
pprint(i)

