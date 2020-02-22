from time import sleep

import click
from github import Github

from vipr.compare_in_browser import compare_in_browser
from vipr.construct_base_url import construct_base_url
from vipr.extract_branches import extract_branches
from vipr.reduce_to_potential_pr_heads import reduce_to_potential_pr_heads


@click.command()
@click.option("--PAT", default="",
              help="Personal Access Token of your GitHub account.")
@click.option("--origin", default="",
              help="'owner/name'-formatted string of the origin to be analysed")
def open_useful_compares(pat: str, origin: str):
    repo = Github(pat).get_repo(origin)
    repo_branches = extract_branches(repo)

    pr_branches = extract_branches(repo, from_pulls=True)

    # Iterate through forks, getting each one's branches.
    # From that list, remove all branches that exist in origin,
    # and all branches in PRs
    forks: object = repo.get_forks()
    wait_time = forks.totalCount
    for f in forks:
        check_branches = reduce_to_potential_pr_heads(
            extract_branches(f),
            pr_branches,
            repo_branches
        )
        compare_labels = set(
            map(lambda b: f.owner.login + ":" + b, check_branches)
        )

        for c in compare_labels:
            compare_in_browser(to_compare=c, base_url=construct_base_url(repo))
            print("Waiting for {} seconds... GitHub is regenerating your API mana ;-)".format(wait_time))
            sleep(wait_time)
            input("Press Enter to continue...")


if __name__ == '__main__':
    open_useful_compares()
