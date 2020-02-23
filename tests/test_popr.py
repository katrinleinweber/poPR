from github import Github, Repository

from popr import __version__
from popr.construct_base_url import construct_base_url
from popr.extract_branches import extract_branches
from popr.reduce_to_potential_pr_heads import reduce_to_potential_pr_heads

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
    assert ("12-test-branch" and "branch-without-diff") not in potential_branches


def test_construct_base_url():
    base_url = construct_base_url(repo)
    assert base_url == "https://github.com/katrinleinweber/poPR/compare/master...{head}"
