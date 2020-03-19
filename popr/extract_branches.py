from typing import Set

from github import Repository


def extract_branches(repo: Repository, from_pulls: bool = False) -> Set[str]:
    """
    Returns a set of branch name strings by wrapping PyGithub's get_branches().
    See https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.get_branches
    """
    if from_pulls:
        branches: Set[str] = set(b.head.ref for b in repo.get_pulls(state="all"))
    else:
        branches: Set[str] = set(b.name for b in repo.get_branches())

    return branches
