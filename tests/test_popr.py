from github import Github, Repository

from popr import __version__
from popr.prep_compare_base_url import prep_compare_base_url
from popr.extract_branches import extract_branches
from popr.reduce_to_potential_pr_heads import (
    reduce_to_potential_pr_heads,
    get_compare_status,
)

# Setup test objects
repo: Repository = Github().get_repo("katrinleinweber/poPR")
fork: Repository = [f for f in repo.get_forks() if f.owner.login == "poPR-test"][0]


def test_version():
    assert __version__ == "0.1.0"


pr_branches = extract_branches(repo, from_pulls=True)


def test_extract_branches():
    assert ("branch-in-pr-1" and "branch-in-pr-2") in pr_branches
    assert ("master" and "12-test-branch") in extract_branches(repo)


def test_reduce_to_potential_pr_heads():
    potential_branches = reduce_to_potential_pr_heads(fork, pr_branches, repo)
    assert ("branch-1-without-PR" and "branch-2-without-PR") in potential_branches
    assert (
        "12-test-branch" and "branch-without-diff" and "gh-pages"
    ) not in potential_branches


def test_prep_compare_base_url():
    assert (
        prep_compare_base_url(repo)
        == "https://github.com/katrinleinweber/poPR/compare/master...{}"
    )


def test_get_compare_status():
    assert get_compare_status(repo, fork, head="gh-pages") != "diverged"
