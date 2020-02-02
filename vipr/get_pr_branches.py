from typing import List

from github import Github


def get_pr_branches(repo: str) -> List[str]:
    pull_requests = Github() \
        .get_repo(repo) \
        .get_pulls()
    pr_branches: List[str] = [PR.head.ref for PR in pull_requests]
    return pr_branches
