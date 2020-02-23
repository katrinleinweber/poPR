from github import Repository


def construct_base_url(repo: Repository) -> str:
    return repo.html_url + "/compare/" + repo.default_branch + "...{head}"
