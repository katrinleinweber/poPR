from github import Github

from vipr import __version__
from vipr.construct_base_url import construct_base_url
from vipr.extract_branches import extract_branches

origin: str = "katrinleinweber/ViPR-test"
repo: object = Github().get_repo(origin)


def test_version():
    assert __version__ == '0.1.0'


def test_extract_branches():
    assert extract_branches(repo, from_pulls=True) == {"patch"}
    assert extract_branches(repo) == {'dev', 'master'}


def test_construct_base_url():
    base_url = construct_base_url(repo)
    assert base_url == "https://github.com/katrinleinweber/ViPR-test/compare/master...{head}"
