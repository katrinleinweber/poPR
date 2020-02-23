from github import Repository


def construct_fork_label(fork: Repository, branch: str) -> str:
    return fork.owner.login + ":" + branch
