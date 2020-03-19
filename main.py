import click
from github import Github, Repository

from popr.compare_in_browser import compare_in_browser
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
    origin = gh.get_repo(origin)
    repo_branches = extract_branches(origin)

    pr_branches = extract_branches(origin, from_pulls=True)

    # Iterate through forks, getting each one's branches.
    # From that list, remove all branches that exist in origin,
    # and all branches in all PRs
    forks: Repository = origin.get_forks()
    for fork in forks:
        heads = reduce_to_potential_pr_heads(fork, pr_branches, origin)
        heads = [construct_fork_label(fork, branch) for branch in heads]

        for head in heads:
            input("Press Enter to review potential PR from {}".format(head))
            compare_in_browser(origin, head)
            wait_for_api(gh)


if __name__ == "__main__":
    open_useful_compares()
