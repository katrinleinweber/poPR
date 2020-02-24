import click
from github import Github, Repository

from popr.compare_in_browser import compare_in_browser
from popr.construct_base_url import construct_base_url
from popr.construct_fork_label import construct_fork_label
from popr.extract_branches import extract_branches
from popr.reduce_to_potential_pr_heads import reduce_to_potential_pr_heads
from popr.wait_for_api import wait_for_api


@click.command()
@click.option(
    "--PAT", default=None, help="Personal Access Token of your GitHub account."
)
@click.option(
    "--origin",
    default="",
    help="'owner/name'-formatted string of the origin to be analysed",
)
def open_useful_compares(pat: str, origin: str):
    gh = Github(pat)
    repo = gh.get_repo(origin)
    repo_branches = extract_branches(repo)

    pr_branches = extract_branches(repo, from_pulls=True)

    # Iterate through forks, getting each one's branches.
    # From that list, remove all branches that exist in origin,
    # and all branches in PRs
    forks: Repository = repo.get_forks()
    for f in forks:
        check_branches = reduce_to_potential_pr_heads(f, pr_branches, origin=repo)
        compare_labels = [construct_fork_label(f, b) for b in check_branches]

        for c in compare_labels:
            input("Press Enter to review potential PR from {}".format(c))
            compare_in_browser(to_compare=c, base_url=construct_base_url(repo))
            wait_for_api(gh)


if __name__ == "__main__":
    open_useful_compares()
