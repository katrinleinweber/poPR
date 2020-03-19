from typing import Set

from github import Repository

from popr.construct_fork_label import construct_fork_label
from popr.extract_branches import extract_branches


def reduce_to_potential_pr_heads(
    fork: Repository, pr_branches: Set[str], origin: Repository
) -> Set[str]:
    """
    Finds all branches in a fork and removes those which do not need to be
    passed on to compare_in_browser().

    :return: All branches contain unmerged changes, but aren't in an open PR.
    """

    fork_branches = extract_branches(fork)

    # Remove branches for which a PR is open first...
    potential_pr_branches = fork_branches.difference(pr_branches)

    # ... and those either identical or simply behind origin:default
    potential_pr_branches = potential_pr_branches.difference(
        head
        for head in potential_pr_branches
        if get_compare_status(origin, fork, head) != "diverged"
    )

    return potential_pr_branches


def get_compare_status(repo: Repository, fork: Repository, head: str) -> str:
    """
    Compares a branch in a fork to the origin's default branch.

    :return: Status of the compared branch
    """
    base = repo.default_branch
    if head == "gh-pages" and base == "master":
        return "no common ancestor"

    label = construct_fork_label(fork, head)
    compare = repo.compare(base, label)
    return compare.status
