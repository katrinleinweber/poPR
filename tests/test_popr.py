from github import Github

from popr import __version__
from popr.construct_base_url import construct_base_url
from popr.extract_branches import extract_branches

origin: str = "katrinleinweber/poPR"
repo: object = Github().get_repo(origin)


def test_version():
    assert __version__ == "0.1.0"


pr_branches = extract_branches(repo, from_pulls=True)


def test_extract_branches():
    assert ("branch-in-pr-1" and "branch-in-pr-2") in pr_branches
    assert ("master" and "12-test-branch") in extract_branches(repo)


def test_construct_base_url():
    base_url = construct_base_url(repo)
    assert base_url == "https://github.com/katrinleinweber/poPR/compare/master...{head}"
